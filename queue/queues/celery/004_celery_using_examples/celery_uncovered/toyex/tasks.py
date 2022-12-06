from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task, group, chord, current_task
from django.core.mail import mail_admins
from django.conf import settings
from django.http import JsonResponse

from .utils import make_csv, strf_date
from .models import Repository
import datetime


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
def fetch_hot_repos(since, per_page, page):
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
    resp = requests.get(
        'https://api.github.com/search/repositories',
        params=params,
        headers=headers,
        timeout=(connect_timeout, read_timeout))
    resp_j = resp.json()
    items = resp_j.get(u'items', [])

    return items

# from celery_uncovered.celery import app
# @app.task(ignore_result=True)
@shared_task
def produce_hot_repo_report_task(period, ref_date=None):
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
        fetch_hot_repos.s(ref_date_str, 20, 1),
        # fetch_hot_repos.s(ref_date_str, 100, 2),
        # fetch_hot_repos.s(ref_date_str, 100, 3),
        # fetch_hot_repos.s(ref_date_str, 100, 4),
        # fetch_hot_repos.s(ref_date_str, 100, 5)
    ])
    # 3. group by language and
    # 4. create csv
    # return chord(fetch_jobs)(build_report_task.s(ref_date_str)).get()
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

    filename = '{media}/github-hot-repos-{date}.csv'.format(media=settings.MEDIA_ROOT, date=ref_date)
    return make_csv(filename, lines)

'''
Tis task uses celery.canvas.group to execute five concurrent calls of fetch_hot_repos/3. Those results are waited for and then reduced to a list of repository objects. Then our result set is grouped by topic and finally exported into a generated CSV file under the MEDIA_ROOT/ directory.
'''


"""
I) Desc:
Create a logging handler that will be able to track Server errors (50X) and report them to admins through via celery.
I advice to thoroughly understand https://docs.djangoproject.com/en/1.11/howto/error-reporting/

Seems like you need to extend default  'django.utils.log.AdminEmailHandler',

II) Implementation Details:
1. Create self containable task called `report_error_task/4 similar to `self.send_mail(subject, message,
fail_silently=True, html_message=html_message)``
2. Extend 'django.utils.log.AdminEmailHandler' in the way it will call report_error_task.delay with the
required parameters
3. Return nothing (Ensure that ignore_result flag set to True)
4. Provide http tests that ensures that it is called

III) Extra:
1. Modify code so that task could be scheduled once per time range (1 hour, 6 hours) and all bugs will be collected and
send as one email, rather than notifying often.
Hint: you also need to create models.py that will store the HttpErrorEntries

IV) Required Libraries:
    django.core.mail
    django.util.log
    mailhog
    pytest
"""

@shared_task
def report_error_task(subject, message, *args, **kwargs):
    mail_admins(subject, message, *args, **kwargs)
