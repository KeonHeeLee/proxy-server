from flask import Flask, make_response
import requests

app = Flask(__name__)

@app.route("/naver", methods=["GET"])
def naver_redirection():
    res = requests.request("GET", "https://www.naver.com")
    body = res.content
    response = make_response(body, 200)
    response.headers["test_proxy"] = "naver-proxy"
    return response

@app.route("/daum", methods=["GET"])
def daum_redirection():
    res = requests.request("GET", "https://www.daum.net")
    body = res.content
    response = make_response(body, 200)
    response.headers["test_proxy"] = "daum-proxy"
    return body, 200

if __name__ == "__main__":
    app.run('0.0.0.0', 8000, debug=True)