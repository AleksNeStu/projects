### Desc



### Tree

```sh
    - celery_uncovered/
      # to be ensured that Celery will start together with Django
      - celery_uncovered/__init__.py
      # contains different applications that we will cover
      - celery_uncovered/{toyex,tricks,advex}
      # defines a Celery instance
      - celery_uncovered/celery.py
      # is the source of configuration for our app and Celery.
      # Depending on the execution environment, Django will launch corresponding settings:
      # local.py for development or test.py for testing.
      # DJANGO_SETTINGS_MODULE entry point (marker) for that
      - config/settings/{base,local,test}.py
      - config/urls.py
    - manage.py
```


### Django Apps
`start` - contains widely used (simple) examples of using celery to solve background tasks.
Run: run/01_start

`extra` - contains generic patterns of using celery to facilitate workflow execution and many others
Run: run/02_extra

`tricks` - contains generic examples of extending default ```celery.app.Task``` and some undocument tricks such as: verbose logging; scope injection; freezing task
Run: run/03_tricks

### Email server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.


With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

How to deploy and run it via docker you can refer to its [README.md](docker/mailhog/README.md).

Further configuration options are available in `MailHog`_.


### Tests
```sh
$ chmod +x utility/unittest.sh
$ ./utility/unittest.sh
```
