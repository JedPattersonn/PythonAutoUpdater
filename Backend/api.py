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
