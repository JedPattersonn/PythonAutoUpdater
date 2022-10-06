# Python Auto Updater
My solution to automatically download the newest build of your python app. Will work in other languages but sytnax will need to be changed.

# Backend / API
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


# Application Code
We have now covered the basics of the API we need. Below I will detail what is needed in the code of your application.

I will include the snippet below of the code required. You should call this first function alongside any other checks you do upon startup of the app, such as license authentication and any file checks.
```python
def checkVersion():
  print("Checking for updates...")
  r = requests.get("https://name.herokuapp.com/version")
  newestVersion = r.text
  if newestVersion == currentVersion:
     print("No updates found")
  else:
    downloadUpdate(newestVersion)
```
You may notice the `currentVersion` variable and that it hasn't been delcared yet. I hardcode that in the startup checks as a variable and change the value for every update I push. The logic behind the function is very simple, call the version endpoint and if it matches the hardcoded current version, proceed. If not, call the download function which is seen below.

```python
 def downloadUpdate(newestVersion):
  print("Update found, downloading...")
  url = "https://name.herokuapp.com/download"

  output_file = f"Application Name V{newestVersion}.exe"
  with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

  input("Check your folder for the latest version. Press any key to close this window...")
  sys.exit()
```
So here we are telling the user that we have found a new update, and that we are downloading it. The `output_file` variable we are declaring is what the file will be called. Due to some permission issues when trying to delete the file you have open, we need to create a new one. Change `Application Name` to whatever your software is called. The file will then be called `Name V0.2.9.1.exe`. We then make the request and put the file we get in the same directory as the current version. After that it is just a simple line saying we have downloaded the new file and where you can find it. Once the user presses a key acknowledging this, the window will close.

# Conclusion
I am no way saying this is the optimal solution, but this is what I use and it works well for my needs. Setting up a Heroku server is very easy and there are loads of videos online going through the setup process. 

If you have any improvements or questions about this, don't hesitate to reach out.

Discord - PolarOrb5705#3951
