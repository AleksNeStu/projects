[Source](https://github.com/veryacademy/YT_FastAPI_Celery_Redis_Flower_Introduction)

Flower - http://127.0.0.1:5556/dashboard

Pgadmin - http://127.0.0.1:5050/browser/

FastAPI-Swagger: http://127.0.0.1:8000/docs#/default/run_task_ex1_post

### Add task

```curl
curl -X 'POST' \
  'http://127.0.0.1:8000/ex1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"amount": 4,
"x": 22,
"y": 33
}'
```


### TODO:
1) Hide sensitive password and keys data
2) Separate containers, code and packages
3) Update tech stack via docker compose
4) Update packages
5) Add doc

# pip freeze > requirements.txt