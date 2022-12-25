# Create your tasks here
import requests
from celery import shared_task, group, chord
from django.conf import settings
from django.core.mail import mail_admins

from .models import Repository
from .utils import make_csv, strf_date, is_exists
from datetime import datetime

"""
Use case description: fetch the five hundred hottest repositories from GitHub per chosen period (day, week, month), group them by topics, and export the result to the CSV file.
If we provide an HTTP service that will execute this feature triggered by clicking a button labeled “Generate Report,” the application would stop and wait for the task to complete before sending an HTTP response back. This is bad. We want our web application to be fast and we don’t want our users to wait while our back-end computes the results. Instead of waiting for the results to be produced, we would rather queue the task to worker processes via a registered queue in Celery and respond with a task_id to the front-end. Then the front-end would use the task_id to query the task result in an asynchronous fashion (e.g., AJAX) and will keep the user updated with the task progress. Finally, when the process finishes, the results can be served as a file to download via HTTP.
"""


# The @shared_task decorator lets you create tasks without having any concrete app
# https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#django-first-steps
@shared_task
def send_test_email_task():
    mail_admins(
        'MailHog Test',
        'Hello from Mailhog.',
        fail_silently=False,)

"""
Desc:
Create a task that will fetch hottest repositories from github per day, week, month (say 500),
group them by language and put the result to the csv file

Implementation Details:
1. Create self containable task called `produce_hot_repo_report_task(ref_date, period='week')`
2. Investigate how and then use github api service https://developer.github.com/v3/search/#search-repositories
3. Return filepath where the result is stored /media/...
4. Define method `produce_hot_repo_report_task_for_week(period='week')`
that will call produce_hot_repo_report_task with date today()

Extra:
1. Modify code so that if the result for that date is already exists, no need to send external
request
2. What if we need to produce csv per language?
hint: For that you need to use celery.canvas.group and modify
`produce_hot_repo_report_task(language/topic, ref_date, period='week')`
3. Probably your client wants it to be automatically callable each day at 00:00, generate report
 for previous date and send it to dummy email.
hint: periodic tasks

IV) Required Libraries:
    requests
    django.core.mail
"""

@shared_task
def fetch_hot_repos_v1(since, per_page, page):
    """
    The fetch_hot_repos function fetches the top-N most popular repositories on GitHub
    that were created after a given date. The function accepts three parameters:
    since, per_page, and page. Since is a string representing the earliest date from which
    we want to fetch repositories (e.g., '2017-01-01'). Per_page is an integer representing
    how many repos we want to fetch per request (e.g., 100). Page is an integer indicating
    which page of search results we are currently requesting (starting at 1).

    :param since: Filters repositories on the date of creation. (Filter the results by date
    :param per_page: Limit the number of repos that are returned per page (limited by 100
    :param page: Requested page number (in the range [1..5]) - paginate the results
    :return: A list of dictionaries where each dictionary contains information about a single repository
    :note: In order to use GitHub Search API, you need an OAuth Token to pass authentication checks GITHUB_OAUTH
    """



    # django.db.utils.OperationalError: database is locked to avoid error:
    # [2022-12-11 20:08:42,614: ERROR/ForkPoolWorker-3] Chord 'c4f2828b-32be-4ff1-9401-99ae2d10a907' raised: OperationalError('database is locked')
    # django.db.utils.OperationalError: database is locked
    # https://docs.djangoproject.com/en/4.1/ref/databases/
    # import time
    # time.sleep(1)

    params = {
        'sort': 'reactions',
        'order': 'desc',
        'q': f'created:>={since}',
        'per_page': per_page,
        'page': page,
    }
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {settings.GITHUB_OAUTH}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    connect_timeout, read_timeout = 5.0, 30.0
    # https://docs.github.com/en/rest/search#search-repositories
    req_kwargs = dict(
        url='https://api.github.com/search/repositories',
        params=params,
        headers=headers,
        timeout=(connect_timeout, read_timeout),
    )
    resp = requests.get(**req_kwargs)
    resp_j = resp.json()
    items = resp_j.get(u'items', [])
    if not items:
        raise RuntimeError(f'No items for git repositories, req: {req_kwargs}, resp: {str(resp)}')

    return items

# from celery_uncovered.celery import app
# @app.task(ignore_result=True)
@shared_task
def produce_hot_repo_report_task_v1(period, ref_date=None):
    """
    Master task that will be responsible for aggregating results and exporting them into a CSV file:
    The produce_hot_repo_report_task function :
        1. parses the date from a given period string, e.g., 'last-week'
        2. fetches and joins hot repos for each of the 5 time periods (5 days) in that period, e.g., last week's hot repos are all fetched and joined together
        3. groups by language and creates a CSV report

    :param period: Specify the time period for which we want to fetch the data
    :param ref_date=None: Pass the reference date to the function
    :return: A list of dictionaries
    """
    # 1. parse date
    ref_date_str = strf_date(period, ref_date=ref_date)

    # 2. fetch and join
    fetch_jobs = group([
        fetch_hot_repos_v1.s(ref_date_str, 100, 1),
        fetch_hot_repos_v1.s(ref_date_str, 100, 2),
        fetch_hot_repos_v1.s(ref_date_str, 100, 3),
        fetch_hot_repos_v1.s(ref_date_str, 100, 4),
        fetch_hot_repos_v1.s(ref_date_str, 100, 5),
    ])
    # 3. group by language and
    # 4. create csv
    # return chord(fetch_jobs)(build_report_task.s(ref_date_str)).get()
    # chord(header)(callback)
    return chord(fetch_jobs)(build_report_task.s(ref_date_str))


@shared_task
def build_report_task(results, ref_date):
    """
    The build_report_task function takes in a list of repositories and returns a CSV file.
    The CSV file contains the top 10 most popular repos for each language, based on stars.

    :param results: Pass the result of the task to the function
    :param ref_date: Create the filename
    :return: A csv file with the repositories grouped by language
    """
    all_repos = []
    for repos in results:
        all_repos += [Repository(repo) for repo in repos]

    # 3. group by language
    grouped_repos = {}
    for repo in all_repos:
        if repo.language in grouped_repos:
            grouped_repos[repo.language].append(repo.name)
        else:
            grouped_repos[repo.language] = [repo.name]

    # 4. create csv
    lines = []
    for lang in sorted(grouped_repos.keys()):
        lines.append([lang] + grouped_repos[lang])

    filename = f'{settings.MEDIA_ROOT}/github-hot-repos-{ref_date}-{datetime.now()}.csv'
    return make_csv(filename, lines)

'''
Tis task uses celery.canvas.group to execute five concurrent calls of fetch_hot_repos/3. Those results are waited for and then reduced to a list of repository objects. Then our result set is grouped by topic and finally exported into a generated CSV file under the MEDIA_ROOT/ directory.
'''


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# ======================tasks01v2=================================
@shared_task
def fetch_hot_repos_v2(language, since, per_page, page):
    print('lllllllllllllllllllllllllllllllllll', language, since, per_page, page)
    query = 'created:>={date}'.format(date=since)
    if language:
        query += ' language:{lang}'.format(lang=language)
    params = {
        'sort': 'reactions',
        'order': 'desc',
        'q': query,
        'per_page': per_page,
        'page': page,
    }
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {settings.GITHUB_OAUTH}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    connect_timeout, read_timeout = 5.0, 30.0
    # https://docs.github.com/en/rest/search#search-repositories
    req_kwargs = dict(
        url='https://api.github.com/search/repositories',
        params=params,
        headers=headers,
        timeout=(connect_timeout, read_timeout),
    )
    resp = requests.get(**req_kwargs)
    resp_j = resp.json()
    items = resp_j.get(u'items', [])
    if not items:
        raise RuntimeError(
            f'No items for git repositories, req: {req_kwargs}, resp: {str(resp)}')
    return [Repository(item) for item in items]


@shared_task
def fetch_hot_repos_group(group_params):
    print(f'group_params: {group_params}')
    job = group(fetch_hot_repos_v2.s(*params) for params in group_params)
    # result = job.apply_async()
    # res =  result.get()
    # The RuntimeError('Never call result.get() within a task!') error is raised when the result.get() method is called inside a Celery task. This is generally considered an anti-pattern because the result.get() method blocks the current task until the result is ready, which can cause performance issues and lead to deadlocks.
    # print(res)
    # return res
    return job()


@shared_task
def store_hot_repos_group(repos_group, filename):
    print(repos_group)
    repos_flattened = []
    for repo in repos_group:
        repos_flattened += repo

    reponames_by_lang = {}
    for repo in repos_flattened:
        if repo.language in reponames_by_lang:
            reponames_by_lang[repo.language].append(repo.name)
        else:
            reponames_by_lang[repo.language] = [repo.name]

    lines = []
    for lang in sorted(reponames_by_lang.keys()):
        lines.append([lang] + reponames_by_lang[lang])
    result = make_csv.delay(filename, lines)
    return result.get()


@shared_task
def produce_hot_repo_report_task_v2(ref_date, period=None):
    # parse date
    ref_date_str = strf_date(period, ref_date)

    # check if results exist
    filename = f'{settings.MEDIA_ROOT}/github-hot-repos-{ref_date}-{datetime.now()}.csv'
    # if is_exists(filename):
    #     return filename

    group_params = map(lambda i: (None, ref_date_str, 10, i), range(1, 6))

    chain = fetch_hot_repos_group.s(list(group_params)) | store_hot_repos_group.s(filename)
    result = chain()
    return result


@shared_task
def produce_hot_repo_report_task_for_languages(languages, ref_date, period=None):
    # 1. parse date
    ref_date_str = strf_date(period, ref_date)

    # 1b. generate filenames, skip if exists
    filenames_by_lang = {}

    for language in languages:
        filename = '{media}/github-hot-repos-{date}-{lang}-{datetime}.csv'.format(
            media=settings.MEDIA_ROOT,
            date=ref_date_str,
            lang=language,
            datetime=datetime.now()
        )
        if not is_exists(filename):
            filenames_by_lang[language] = filename

    # 2. fetch and join
    languages = filenames_by_lang.keys()
    job_fetch = group([fetch_hot_repos_v1.s(lang, ref_date_str, 100, 1) for lang in languages])
    result = job_fetch.apply_async()
    repo_names_by_lang = {}
    for index, repos in enumerate(result.get()):
        language = languages[index]
        repo_names_by_lang[language] = [repo.name for repo in repos]

    # 3. create csv per language
    filename_repos = [(filenames_by_lang[lang], repo_names_by_lang[lang]) for lang in languages]
    job_store = group( [make_csv.s(filename, [repo_names]) for filename, repo_names in filename_repos] )
    result = job_store.apply_async()
    return result.get()