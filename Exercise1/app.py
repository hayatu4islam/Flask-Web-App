from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
# def show_quote():
def index():
    url = "https://gist.github.com/robatron/a66acc0eed3835119817"
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()
    #
    #     # Save binary content to a local file
    #     with open("quotes.txt", "wb") as file:
    #         file.write(response.content)
    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)
    return "Pass"


# @app.route("/a")
# def index():
#     now = datetime.now()
#     return now.strftime("%d %m %Y %H:%M:%S")
