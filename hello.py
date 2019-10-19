from flask import Flask
import json
app = Flask(__name__)

name = "Sathyanarayana"

@app.route("/")
def helloIndex():
    return json.dumps({"name":name})


if __name__ == "__main__":
    app.run()
