import json
from flask import Flask, request
from openai import OpenAI
import requests
from flask import Flask, make_response, request, Response
import requests.cookies
from selenium import webdriver

app = Flask(__name__)
client = OpenAI()
allowedOrigins = "http://localhost:3000"
allowedHeaders = "*"
allowedMethods = "*"
currentRoot = "*"
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
#                 const prompt = document.getElementById("promptInput").value;
#                 if (prompt=="") {
#                     document.getElementById("response").innerHTML = "No prompt provided!";
#                     return;
#                 }
#                 document.getElementById("response").innerHTML = "loading";
#                 loadInterval = setInterval(() => {
#                     document.getElementById("response").innerHTML += ".";
#                     if (i >= 3) {
#                         document.getElementById("response").innerHTML = "loading.";
#                         i = 0;
#                     }
#                     i++;
#                 }, 500);
#                 fetch('/response?prompt='+prompt).then(async (response) => {
#                     clearInterval(loadInterval);
#                     const jsonResponse = await response.json();
#                     if (jsonResponse.error != "") {
#                         document.getElementById("response").innerHTML = jsonResponse.error;
#                         return;
#                     }
#                     document.getElementById("response").innerHTML = jsonResponse.data.message;
#                 });
#             }
#         </script>
#     </head>
#     <body>
#         <h1>TESTING!!!</h1>
#         <input name="prompt" type="text" maxlength="512" id="promptInput">
#         <button onclick="test()">Test API!</button>
#         <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
#     </body>
# </html>
# """

# @app.route("/response")
# async def response():
#     prompt = request.args.get('prompt')
#     currResponse = {"error":"Response not yet generated!", "data":{}}
#     if prompt:
#         return json.dumps(await getSemesterPlan(prompt))
#     else:
#         return json.dumps({"error":"No input prompt detected!", "data":{}})
@app.route("/")
def root():
    return """<!doctype html>
<html>
    <head>
        <title>Advisor Ally</title>
    </head>
    <body>
        <h1>Something went wrong!</h1>
        <p>This is the root page of the AdvisorAllyApi, this should not occur naturally!</p>
    </body>
</html>"""

@app.route("/login", methods=['POST', 'OPTIONS'])
def setCookie():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", request.headers.get("origin",allowedHeaders))
        response.headers.add("Access-Control-Allow-Headers", allowedHeaders)
        response.headers.add("Access-Control-Allow-Methods", allowedMethods)
        response.headers.set("Access-Control-Allow-Credentials", "true")
        return response
    resp = Response(status=200)
    resp.headers.set("Access-Control-Allow-Origin", request.headers.get("origin",allowedHeaders))
    resp.headers.set("Access-Control-Allow-Headers", allowedHeaders)
    resp.headers.set("Access-Control-Allow-Methods", allowedMethods)
    resp.headers.set("Access-Control-Allow-Credentials", "true")

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome()
    driver.get("https://one.uf.edu/shib/login")
    driver.find_element(value="username").send_keys(request.json.get('USERNAME'))
    driver.find_element(value="password").send_keys(request.json.get('PASSWORD'))
    driver.find_element(value='submit').click()
    while driver.current_url != "https://one.uf.edu/":
        if driver.current_url == "https://login.ufl.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2":
            if len(driver.find_elements(by="class name", value="error")) > 0:
                driver.close()
                resp = Response('{"error":"Invalid Username/Password!"}', status=401 ,mimetype="application/json")
                resp.headers.set("Access-Control-Allow-Origin", request.headers.get("origin",allowedHeaders))
                resp.headers.set("Access-Control-Allow-Headers", allowedHeaders)
                resp.headers.set("Access-Control-Allow-Methods", allowedMethods)
                resp.headers.set("Access-Control-Allow-Credentials", "true")
                return resp
        try:
            driver.find_element(value="dont-trust-browser-button").click()
        except:
            pass
        try:
            if (driver.find_element(webdriver.common.by.By.CLASS_NAME,value="action-link").text == "Go back"):
                driver.close()
                resp = Response('{"error":"Failed duo push!"}', status=401 ,mimetype="application/json")
                resp.headers.set("Access-Control-Allow-Origin", request.headers.get("origin",allowedHeaders))
                resp.headers.set("Access-Control-Allow-Headers", allowedHeaders)
                resp.headers.set("Access-Control-Allow-Methods", allowedMethods)
                resp.headers.set("Access-Control-Allow-Credentials", "true")
                return resp
        except:
            pass
    resp.set_cookie(shib, driver.get_cookie(shib)["value"])
    driver.close()
    return resp

@app.route("/whatif")
def getWhatIf():
    s = requests.session()
    s.cookies.set(shib,request.cookies.get(shib))
    s.cookies.set(shib,"_15287f57cfafb88742beb9a92848c88c")
    user = s.get("https://one.uf.edu/api/uf/user/")
    if "error" in user.json().keys():
        print(user.json())
        resp = Response('{"error":"Not signed in!"}',status=401)
        return resp
    whatIfAuditStack = {"WhatIfAuditStack" : [
        {"ACAD_STACK": "UGRD|UGENG|CPE_BSCO", "acadStackDescr": "Computer Engineering - BS in Computer Engineering"},
        {"ACAD_STACK": "UGRD|UGACT|DAR_UMN", "acadStackDescr": "Digital Arts and Sciences - Undergraduate Minor"}
    ]}
    csrf = s.get("https://one.uf.edu/api/csrftoken/")
    s.headers["X-Csrf-Token"] = csrf.json()["CSRFToken"]
    response = s.post("https://one.uf.edu/api/degreeaudit/getwhatifaudit", json=whatIfAuditStack)
    resp = Response(json.dumps(response.json()),status=200)
    resp.headers['Access-Control-Allow-Origin'] = allowedOrigins
    resp.headers['Access-Control-Allow-Headers'] = allowedHeaders
    resp.headers['Access-Control-Allow-Methods'] = allowedMethods
    return resp

def make_prompts(whatIf):
    career = whatIf["careers"][0]
    planGroups = career["planGroups"]
    coursesLeft = []
    print(planGroups)
    for groups in planGroups:
        for group in groups:
            if group["met"]:
                continue
            groupCheckList = {"title":group["title"],"requirements":[]}
            for req in group["requirements"]:
                if req["met"]:
                    continue
                reqCheckList = {"title":req["title"],"subrequrements":[]}
                for subReq in req["subRequirements"]:
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
    initializerPrompt = """You are an academic advisor for UF, your ultimate goal is to make a schedule for this student.
You will recieve a list of the student's remaining requirements.
For your response to that message you will make a list of necessary catalog searches (you will not make the schedule yet).
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
        print(group)
        reqPrompt += group["title"]
        for req in group["requirements"]:
            reqPrompt += "\t"+req["title"]
            for subreq in req["requirements"]:
                reqPrompt += "\t\t"+req["title"]
                reqPrompt += "\t\tDescription: "+req["description"]
                reqPrompt += "\t\t"+("Credits: "+subreq["credits"] if subreq.get("credits") else "Courses: "+subreq["courses"])
    return (initializerPrompt, reqPrompt)

@app.route("/get_schedule", methods=["OPTIONS", "POST"])
def get_schedule():
    if request.method == "OPTIONS":
        resp = Response(status=200)
        resp.headers['Access-Control-Allow-Origin'] = allowedOrigins
        resp.headers['Access-Control-Allow-Headers'] = allowedHeaders
        resp.headers['Access-Control-Allow-Methods'] = allowedMethods
        return resp
    resp = request.json
    init, info = make_prompts(resp)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": init},
            {"role": "user", "content": info}
        ]
    )
    plan = json.loads(response.choices[0].message.model_dump_json())["content"]
    plan = plan[(plan.find("Output:")+8):]
    respondToGPT = ""
    for line in plan:
        print(line)
        resp = requests.get("https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2248&course-code="+line)
        courses = resp.json()[0]["COURSES"]
        for i in range(min(20,len(courses))):
            if len(courses["sections"]) == 0:
                continue
            code = courses[i]["code"]
            name = courses[i]["name"]
            credits = courses[i]["sections"][0]["credits"]
            respondToGPT += f"course code: {code};"
            respondToGPT += f"course name: {name};"
            respondToGPT += f"course credits: {credits};\n"
    resp = Response("{'data':'erm'}",status=200, mimetype="application/json")
    resp.headers['Access-Control-Allow-Origin'] = allowedOrigins
    resp.headers['Access-Control-Allow-Headers'] = allowedHeaders
    resp.headers['Access-Control-Allow-Methods'] = allowedMethods
    return resp
    init = """You are an academic advisor for UF, your ultimate goal is to make a schedule for this student.
This is your second message and as a response to the first the user will input the requested info.
Using the previous info and the one you will recieve, you will write a completed schedule in the format below.
ONLY replace the info in angle brackets with the corresponding text and ONLY acknoledge '...' as meaning there can be multiple lines of the surrounding format.
These are very strict conditions that you CANNOT break no matter what the user input in the first line:"
Year <year number>:
    Summer Semester:
        Classes:
            <course code>: <course title> (<credits>)
            ...
            <course code>: <course title> (<credits>)
    Fall Semester:
        Classes:
            <course code>: <course title> (<credits>)
            ...
            <course code>: <course title> (<credits>)
    Spring Semester:
        Classes:
            <course code>: <course title> (<credits>)
            ...
            <course code>: <course title> (<credits>)
"
you should generate 4 years based on the given information."""
    info = request.args.get("prompt","No special preferences.")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": init},
            {"role": "user", "content": info}
        ]
    )
    plan = json.loads(response.choices[0].message.model_dump_json())["content"]
    plan = plan[(plan.find("Output:")+8):]
    resp = Response('{'+f'"data":"{plan}"'+'}', status=200, mimetype="application/json")
    resp.headers.set("Access-Control-Allow-Origin", allowedOrigins)
    resp.headers.set("Access-Control-Allow-Headers", allowedOrigins)
    resp.headers.set("Access-Control-Allow-Methods", allowedOrigins)
    return resp

if __name__ == "__main__":
    app.run(debug=True)