# Docker
``sh
; Build and up
docker-compose up -d --build
docker-compose up -d --up
; Force up
docker-compose -f docker-compose.yml up
; Rebuild python int
docker-compose -f docker-compose.yml build api 
``

**Redis clients:**
https://tableplus.com/blog/2019/10/tableplus-linux-installation.html
https://resp.app/


Server log get /http://localhost:5000/universities/
```
/home/he/Projects/projects/api/server/flask/001_caching_w_docker/app.py: 2.4757
INFO:werkzeug:127.0.0.1 - - [23/Nov/2022 01:07:42] "GET /universities/ HTTP/1.1" 200 -
/home/he/Projects/projects/api/server/flask/001_caching_w_docker/app.py: 0.0048
INFO:werkzeug:127.0.0.1 - - [23/Nov/2022 01:07:47] "GET /universities/ HTTP/1.1" 200 -
/home/he/Projects/projects/api/server/flask/001_caching_w_docker/app.py: 0.0055
INFO:werkzeug:127.0.0.1 - - [23/Nov/2022 01:07:49] "GET /universities/ HTTP/1.1" 200 -
```