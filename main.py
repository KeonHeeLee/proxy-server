from flask import Flask, make_response
import requests

app = Flask(__name__)

'''
Proxy Redirection Step
1. Recieve HTTP-request from client.
2. This server connect to other server. (request to other server)
3. Get response by other server.
4. Send this response to client with header what you customize.
'''

@app.route("/naver", methods=["GET"])
def naver_redirection():
    '''
    - GET method test 1
    - redirect to naver web-site
    '''
    res = requests.request("GET", "https://www.naver.com")
    body = res.content
    response = make_response(body, 200)
    response.headers["test_proxy"] = "naver-proxy"
    return response

@app.route("/daum", methods=["GET"])
def daum_redirection():
    '''
    - GET method test 1
    - redirect to naver web-site
    '''
    res = requests.request("GET", "https://www.daum.net")
    body = res.content
    response = make_response(body, 200)
    response.headers["test_proxy"] = "daum-proxy"
    return body, 200

if __name__ == "__main__":
    app.run('0.0.0.0', 8000, debug=True)
