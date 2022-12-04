# Scenario 1 - Report generation and export**

### Desc

Report generation and export. Define a task that produces a CSV report and schedule it at regular intervals with [celerybeat](https://django-celery-beat.readthedocs.io/en/latest/).

**Use case description:** fetch the 500 hottest repositories from GitHub per chosen period (day, week, month), group them by topics, and export the result to the CSV file.

If provide an HTTP service that will execute this feature triggered by clicking a button labeled “Generate Report,” the application would stop and wait for the task to complete before sending an HTTP response back. This is bad. We want our web application to be fast and we don’t want our users to wait while our back-end computes the results. Instead of waiting for the results to be produced, would rather queue the task to worker processes via a registered queue in Celery and respond with a `task_id` to the front-end. Then the front-end would use the `task_id` to query the task result in an asynchronous fashion (e.g., AJAX) and will keep the user updated with the task progress. Finally, when the process finishes, the results can be served as a file to download via HTTP.

### Implementation Details

First of all, let us decompose the process into its smallest possible units and create a pipeline:

**A pipeline of workers with Celery and Python:**

1.  **Fetchers** are the workers that are responsible for getting repositories from the GitHub service.
2.  The **Aggregator** is the worker that is responsible for consolidating results into one list.
3.  The **Importer** is the worker that is producing CSV reports of the hottest repositories in GitHub.

![A pipeline of Celery Python workers](https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/191391/image-1582290925096-33c2162219031ca2cd9445e91c3b0a12.png)


Fetching repositories is an HTTP request using the [GitHub Search API](https://developer.github.com/v3/search/) `GET /search/repositories`. However, there is a limitation of the GitHub API service that should be handled: The API returns up to 100 repositories per request instead of 500\. We could send five requests one at a time, but we don’t want to keep our user waiting for five individual requests since HTTP requests are an I/O bound operation. Instead, we can execute five concurrent HTTP requests with an appropriate page parameter. So the page will be in the range [1..5]. Let’s define a task called `fetch_hot_repos` in the `toyex/tasks.py` module:


Next define a master task that will be responsible for aggregating results and exporting them into a CSV file: produce_hot_repo_report_task/->filepath:










Uses Celery Groups for execute multiple requests to github and store report in CSV-file

In order to launch and check an actual behavior of the task, first start the Celery process:

.. code-block:: bash

    $ celery -A celery_uncovered worker -l info


Then you will be able to test functionality via Shell:

.. code-block:: python

    from celery_uncovered.toyex.tasks import produce_hot_repo_report
    produce_hot_repo_report('day')


Finally, to see the result, navigate to the `celery_uncovered/media` directory and open the corresponding log file called similar to `github-hot-repos-2017-08-29.csv`. You might see something similar as below after running this task multiple times:

.. code-block:: bash

    1C Enterprise,arkuznetsov/scenex
    ASP,carsio/Projeto-Unity
    ActionScript,nicothezulu/EveryplayANE
    Arduino,braindead1/WemosD1_HomeMatic_StatusDisplay
    ...


You also can test it by passing a kwarg `ref_date`. Task will fetch only repositories created after referred date:

.. code-block:: python

    from celery_uncovered.toyex.tasks import produce_hot_repo_report
    produce_hot_repo_report(None, '2017-08-30')


You will find the report in file called `github-hot-repos-2017-08-30.csv`.
