# Python Auto Updater
My solution to automatically download the newest build of your python app. Will work in other languages but sytnax will need to be changed.

# Backend
To fetch the newest build, you will need to setup a Flask server and host it. This can be done for free using [Heroku](https://www.heroku.com). Below is the simple code needed for it, you will also find this in the files above.
```python
from flask import (
  Flask,
  request,
  send_file
)
app = Flask(__name__, static_folder=".",
static_url_path="", template_folder=".")

@app.route("/version", methods=["GET"])
def checkVersion():
  return "0.2.9.1"
  
@app.route("/download", methods=["GET"])
def download():
  return send_file('file.exe')
  
 if __name__ == "__main__":
  app.run(port=3333)
```

Let's break down the code.

```python
from flask import (
  Flask,
  request,
  send_file
)
```
Here we are importing the Flask library as well as some components of it. The most important one is the `send_file` one as we need this to return a file from the API

Next we need the application to check what version the newest application is. Here is the code for that:
```python
@app.route("/version", methods=["GET"])
def checkVersion():
  return "0.2.9.1"
```
By using the `/version` endpoint on our API, we will get a number returned to us. In this example, we are on version 0.2.9.1. Everytime a new file is uploaded to the API, we will update this number.

Let's get to the most important part of the code, sending the file to the user.
```python
@app.route("/download", methods=["GET"])
def download():
  return send_file('file.exe')
```
If we call the `/download` endpoint, we will get a file returned to us. We need to rename the paramater in `return send_file()` to the name of the application in the folder. It will be easier to keep the file name the same the whole time.

