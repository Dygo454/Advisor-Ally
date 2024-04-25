# Advisor Ally
An AI advisor that makes custom semester plans to students of any major at uf.

## Installing the app:
1. Make sure you have python and pip installed on your system. As well as node.js/npm for the front end.
2. Install the venv and requirements.txt:
```
cd backend
python -m venv venv
pip install -r requirements.txt

```
3. Ensure your API key is in you environment variables as 'OPENAI_API_KEY'.
    * This should be done before intering the virtual env.
    * This can also be done after the next step by setting the variable while in the venv (if opting for this method it would have to be done everytime you enter the venv)
```
set OPENAI_API_KEY=<insert your key here>
```
4. Next in a new Terminal/Powershell/CMD instance, navigate to the frontend directory and install the necessary packages:
```
cd frontend
npm install

```
## Running the app
0. Before running you will have to navigate to one.uf, sign in, and grab the session id from there.
   * After logging in to one.uf, open up the network tab of your browser's inspect element.
   * Then, look for one.uf http request. (if there are no displayed requests reload the page with the network tab open)
   * Go to cookies and copy the value of the "\_shibsession\_"
   * Then paste it in to line 138 of server.py in the backend.
      * (where you see "\<INSERT SHIB HERE\>")
1. Run the following commands from the root directory:
   * This hosts the back end to http://localhost:5000.
Windows (CMD):
```
cd backend
venv\Scripts\activate.bat
python server.py

```
Unix Based Systems (or Windows Powershell):
```
cd backend
./venv/Scripts/activate
python server.py

```
2. Next start the front end server with the following commands:
   * This hosts the front end to http://localhost:3000.
```
cd frontend
npm start

```
Now navigating to http://localhost:3000 in your browser (if it did not automatically open).
