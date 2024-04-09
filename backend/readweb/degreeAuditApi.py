# import asyncio
import json
import requests
from flask import Flask, make_response, redirect, request
import requests_oauthlib

app = Flask(__name__)

# @app.route("/")
# def root():
#     return """
# <!doctype html>
# <html>
#     <head>
#         <title>Advisor Ally</title>
#         <script>
#             let i = 0;
#             let loadInterval;
#             function test() {
#                 document.getElementById("response").innerHTML = "loading";
#                 loadInterval = setInterval(() => {
#                     document.getElementById("response").innerHTML += ".";
#                     if (i >= 3) {
#                         document.getElementById("response").innerHTML = "loading.";
#                         i = 0;
#                     }
#                     i++;
#                 }, 500);
#                 fetch('/response').then(async (response) => {
#                     clearInterval(loadInterval);
#                     const jsonResponse = await response.json();
#                     console.log(jsonResponse);
#                     document.getElementById("response").innerHTML = JSON.stringify(jsonResponse);
#                 });
#             }
#         </script>
#     </head>
#     <body>
#         <h1>TESTING!!!</h1>
#         <button onclick="test()">Test API!</button>
#         <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
#     </body>
# </html>
# """

# @app.route("/test")
# def test():
#     return """
# <!doctype html>
# <html>
#     <head>
#         <title>Advisor Ally</title>
#         <script>
#             let i = 0;
#             let loadInterval;
#             function test() {
#                 document.getElementById("response").innerHTML = "loading";
#                 loadInterval = setInterval(() => {
#                     document.getElementById("response").innerHTML += ".";
#                     if (i >= 3) {
#                         document.getElementById("response").innerHTML = "loading.";
#                         i = 0;
#                     }
#                     i++;
#                 }, 500);
#                 fetch('http://localhost:8080/https://one.uf.edu/api/csrfToken', {
#                     //method: "GET", // *GET, POST, PUT, DELETE, etc.
#                     //mode: "no-cors", // no-cors, *cors, same-origin
#                     //cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
#                     //credentials: "omit", // include, *same-origin, omit
#                     //headers: {
#                     //    'Access-Control-Allow-Origin': '*',
#                     //    'User-Agent': 'python-requests/2.31.0',
#                     //    'Accept-Encoding': 'gzip, deflate',
#                     //    'Accept': '*/*',
#                     //    'Connection': 'keep-alive'
#                     //},
#                     redirect: "follow", // manual, *follow, error
#                     //referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
#                 }).then(async (response) => {
#                     //myHeaders.append("Cookie", response.headers.get("x-set-cookie"));
#                     const token = await response.json();
#                     console.log(token['CSRFToken']);
#                     //for (const key of response.headers.entries()) {
#                     //    console.log(key);
#                     //}
#                     //myHeaders.append("X-Csrf-Token", token.CSRFToken);
#                     fetch('http://localhost:8080/https://one.uf.edu/api/degreeaudit/getwhatifselectoptions/', {
#                         redirect: "follow",
#                         headers: {
#                             'xbypass': true,
#                             'xtok': token['CSRFToken'],
#                             'xcook': response.headers.get('X-Set-Cookie')
#                         }
#                     }).then(async (response) => {
#                         console.log(response);
#                         clearInterval(loadInterval);
#                         const jsonResponse = await response.json();
#                         console.log(jsonResponse);
#                         document.getElementById("response").innerHTML = JSON.stringify(jsonResponse);
#                     });
#                 });
#             }
#         </script>
#     </head>
#     <body>
#         <h1>TESTING!!!</h1>
#         <button onclick="test()">Test API!</button>
#         <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
#     </body>
# </html>
# """

@app.route("/")
def root():
    return """<!doctype html>
<html>
    <head>
        <title>Advisor Ally</title>
        <script>
            let i = 0;
            let loadInterval;
            function getWhatIf() {
                document.getElementById("response").innerHTML = "loading";
                loadInterval = setInterval(() => {
                    document.getElementById("response").innerHTML += ".";
                    if (i >= 3) {
                        document.getElementById("response").innerHTML = "loading.";
                        i = 0;
                    }
                    i++;
                }, 500);
                fetch('/whatif').then(async (response) => {
                    clearInterval(loadInterval);
                    const jsonResponse = await response.json();
                    console.log(jsonResponse);
                    document.getElementById("response").innerHTML = JSON.stringify(jsonResponse);
                });
            }
        </script>
    </head>
    <body>
        <h1>Sign in on one.uf and input your '_shibsession_' cookie in the signin page.</h1><br>
        <a href="/signin">Sign in page!</a><br><br>
        <button onclick="getWhatIf()">Get what if! (will currently be CSE major + DAS minor)</button><br>
        <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
    </body>
</html>"""

@app.route("/signin")
def signIn():
    return """<!doctype html>
<html>
    <head></head>
    <body>
        <h1>Your One.UF sign in below:</h1>
        <form action="/setsessioncookie" method="get">
            <label for="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f">SessionID:</label><br>
            <input type="text" id="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" name="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" value="" required><br>
            <input type="submit" value="Use ID">
        </form>
    </body>
</html>"""

@app.route("/setsessioncookie", methods=['GET'])
def setCooikie():
    resp = make_response(redirect('/'))
    print(request)
    shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f"
    resp.set_cookie(shib,request.args.get(shib))
    return resp

@app.route("/whatif")
def getWhatIf():
    s = requests.session()
    shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f"
    s.cookies.set(shib,request.cookies.get(shib))
    user = s.get("https://one.uf.edu/api/uf/user/")
    if "error" in user.json().keys():
        print(user.json())
        return """<!doctype html>
<html>
    <head></head>
    <body><h1>User not signed in!</h1></body>
</html>
"""
    whatIfAuditStack = {"WhatIfAuditStack" : [
        {"ACAD_STACK": "UGRD|UGENG|CPE_BSCO", "acadStackDescr": "Computer Engineering - BS in Computer Engineering"},
        {"ACAD_STACK": "UGRD|UGACT|DAR_UMN", "acadStackDescr": "Digital Arts and Sciences - Undergraduate Minor"}
    ]}
    csrf = s.get("https://one.uf.edu/api/csrftoken/")
    s.headers["X-Csrf-Token"] = csrf.json()["CSRFToken"]
    response = s.post("https://one.uf.edu/api/degreeaudit/getwhatifaudit", json=whatIfAuditStack)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)