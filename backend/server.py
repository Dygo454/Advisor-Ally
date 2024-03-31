from flask import Flask, request
from readweb.readweb import getSemesterPlan
import json

app = Flask(__name__)

@app.route("/")
def root():
    return """
<!doctype html>
<html>
    <head>
        <title>Advisor Ally</title>
        <script>
            let i = 0;
            let loadInterval;
            function test() {
                const prompt = document.getElementById("promptInput").value;
                if (prompt=="") {
                    document.getElementById("response").innerHTML = "No prompt provided!";
                    return;
                }
                document.getElementById("response").innerHTML = "loading";
                loadInterval = setInterval(() => {
                    document.getElementById("response").innerHTML += ".";
                    if (i >= 3) {
                        document.getElementById("response").innerHTML = "loading.";
                        i = 0;
                    }
                    i++;
                }, 500);
                fetch('/response?prompt='+prompt).then(async (response) => {
                    clearInterval(loadInterval);
                    const jsonResponse = await response.json();
                    if (jsonResponse.error != "") {
                        document.getElementById("response").innerHTML = jsonResponse.error;
                        return;
                    }
                    document.getElementById("response").innerHTML = jsonResponse.data.message;
                });
            }
        </script>
    </head>
    <body>
        <h1>TESTING!!!</h1>
        <input name="prompt" type="text" maxlength="512" id="promptInput">
        <button onclick="test()">Test API!</button>
        <p id="response" style="white-space: pre-wrap">NO RESPONSE YET!</p>
    </body>
</html>
"""

@app.route("/response")
async def response():
    prompt = request.args.get('prompt')
    currResponse = {"error":"Response not yet generated!", "data":{}}
    if prompt:
        return json.dumps(await getSemesterPlan(prompt))
    else:
        return json.dumps({"error":"No input prompt detected!", "data":{}})

if __name__ == "__main__":
    app.run(debug=True)