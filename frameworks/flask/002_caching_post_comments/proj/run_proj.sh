docker build -t my-flask-app .
docker stop my-flask-app
#docker rm my-flask-app
docker run -p 5000:5000 my-flask-app