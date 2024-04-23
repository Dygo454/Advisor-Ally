# import asyncio
import json
import requests
from flask import Flask, make_response, redirect, request, Response
from selenium import webdriver

app = Flask(__name__)
shib="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f"

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
        <h1>Sign in with your uf username and password, then accept the duo push!</h1><br>
        <a href="/signin">Sign in page!</a><br><br>
        <button onclick="getWhatIf()">Get what if! (will currently be CSE major + DAS minor)</button><br>
        <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
    </body>
</html>"""

@app.route("/signin")
def signIn():
    if "failed_login" in request.args.keys() and request.args.get("failed_login") == "true":
        return """<!doctype html>
<html>
    <head></head>
    <body>
        <h1>Your One.UF sign in below:</h1>
        <h2 style="color:red;">Username or password were incorrect!</h2>
        <form action="/setsessioncookie" method="get">
            <!--<label for="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f">Log In:</label><br>-->
            <!--<input type="text" id="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" name="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" value="" required><br>-->
            <input type="text" id="USERNAME" name="USERNAME" value="" required><br>
            <input type="password" id="PASSWORD" name="PASSWORD" value="" required><br>
            <input type="submit" value="Use ID">
        </form>
    </body>
</html>"""
    return """<!doctype html>
<html>
    <head></head>
    <body>
        <h1>Your One.UF sign in below:</h1>
        <form action="/setsessioncookie" method="post">
            <!--<label for="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f">Log In:</label><br>-->
            <!--<input type="text" id="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" name="_shibsession_68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f68747470733a2f2f73702e6c6f67696e2e75666c2e6564752f75726e3a6564753a75666c3a70726f643a30303734312f" value="" required><br>-->
            <input type="text" id="USERNAME" name="USERNAME" value="" required><br>
            <input type="password" id="PASSWORD" name="PASSWORD" value="" required><br>
            <input type="submit" value="Log In">
        </form>
    </body>
</html>"""

@app.route("/login", methods=['POST'])
def setCookie():
    resp = make_response(redirect('/'))

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome()
    driver.get("https://one.uf.edu/shib/login")
    driver.find_element(value="username").send_keys(request.form.get('USERNAME'))
    driver.find_element(value="password").send_keys(request.form.get('PASSWORD'))
    driver.find_element(value='submit').click()
    while driver.current_url != "https://one.uf.edu/":
        if driver.current_url == "https://login.ufl.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2":
            if len(driver.find_elements(by="class name", value="error")) > 0:
                driver.close()
                return redirect("/signin?failed_login=true")
        try:
            driver.find_element(value="dont-trust-browser-button").click()
        except:
            pass
    resp.set_cookie(shib, driver.get_cookie(shib)["value"])
    driver.close()
    return resp

@app.route("/whatif")
def getWhatIf():
    s = requests.session()
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

def make_prompts(whatIf, userPrompt):
    career = whatIf["careers"][0]
    planGroups = career["planGroups"]
    coursesLeft = []
    for group in planGroups:
        if group["met"]:
            continue
        groupCheckList = {"title":group["title"],"requirements":[]}
        for req in group["requirements"]:
            if req["met"]:
                continue
            reqCheckList = {"title":req["title"],"subrequrements":[]}
            for subReq in req["subrequirements"]:
                if subReq["met"]:
                    continue
                subReqCheckList = {"title":req["title"],"description":subReq["description"]}
                if subReq["unitsRequired"] != 0:
                    subReqCheckList["credits"] = subReq["unitsNeeded"]
                elif subReq["courseRequired"] != 0:
                    subReqCheckList["courses"] = subReq["courseNeeded"]
                reqCheckList["subrequrements"] += subReqCheckList
            groupCheckList["requirements"] += reqCheckList
        coursesLeft += groupCheckList
    initializerPrompt = """You will recieve a list of the student's remaining requirements.
For your response make a list of necessary catalog searches.
\tIf there is a category without specific course codes (such as elective categories):
\t\tUsing the subrequirement description, add to the list a course code to search.
\t\tAn example:
\t\t\tCAP
\t\t\tCIS
\t\t\tEEL
\tIf there isn't a need to search for course codes (all remaining requirements are specific classes or a single class of a category, like quest classes):
\t\tThen say exactly: "None"
"""
    reqPrompt = ""
    for group in coursesLeft:
        reqPrompt += group["title"]
        for req in group["requirements"]:
            reqPrompt += "\t"+req["title"]
            for subreq in req["requirements"]:
                reqPrompt += "\t\t"+req["title"]
                reqPrompt += "\t\tDescription: "+req["description"]
                reqPrompt += "\t\t"+("Credits: "+subreq["credits"] if subreq.get("credits") else "Courses: "+subreq["courses"])
    return reqPrompt

if __name__ == "__main__":
    app.run(debug=True)