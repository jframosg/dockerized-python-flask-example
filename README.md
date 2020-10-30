# dockerized-python-flask-example
## Example of a dockerized Python Flask app.

To run without Docker:
```
python3 main.py
```

In the web browser, type: http://localhost:8080

To run with Docker:

1. Create image:
```
docker build -f Dockerfile -t dockerized-python-flask-image .
```

2. Run image:
```
docker run -d -p 8080:8080 dockerized-python-flask-image
```

In the web browser, type: http://localhost:8080

Enjoy!
