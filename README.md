# Advisor Ally
An AI advisor that makes custom semester plans to students of any major at uf.

Running the app:
1. Make sure you have python and pip installed on your system.
2. Install the venv and requirements.txt:
```
cd backend
python -m venv venv
pip install -r requirements.txt

```
3. Ensure your API key is in you environment variables as 'OPENAI_API_KEY'.
    * This can be done with the following code (not in the venv)
    * This can also be done after the next step by setting the variable while in the venv (this would have to be done everytime)
```
set OPENAI_API_KEY=<insert your key here>
```
4. Run the following commands from the root directory:
Windows (CMD):
```
cd backend
venv\Scripts\activate.bat
python server.py

```
Unix Based Systems:
```
cd backend
./venv/Scripts/activate
python server.py

```
5. This hosts the back end to http://localhost:5000.
