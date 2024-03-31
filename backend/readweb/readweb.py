import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import json

client = OpenAI()

def generateInput():
    # Step 1: Send an HTTP GET request
    url = 'https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CPS_BSCS/#modelsemesterplantext'
    response = requests.get(url)

    # Step 2: Parse the HTML content
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text data from the page (excluding HTML tags)
        text_data = soup.get_text()

        # Step 3: Save the text data to a .txt file
        with open('data.txt', 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_data)

    else:
        print(f"Failed to fetch the web page. Status code: {response.status_code}")

    # Open the input text file for reading
    with open('data.txt', 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # Find the "Required Courses" section
    start_index = content.find("Required Courses")
    end_index = content.find("Total Credits", start_index)

    if start_index != -1 and end_index != -1:
        class_info = content[start_index:end_index]
    else:
        print("Required Courses section not found in the text.")
        class_info = ""

    # Save the class-related information to a new text file named "updated-data.txt"
    print("Filtered class information saved to updated-data.txt.")
    return class_info




def read_input_file(file_path):
    # if not os.path.isfile(file_path):
    #     print(f"File not found: {file_path}")
    #     return None
    
    try:
        with open(file_path, 'r') as file:
            data = file.read()  # Read the whole file content as a single string
            print(data)
            return data
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None

def generate_semester_plan(prompt):

    try:
        # Append a task description to the prompt
        prompt += f"""\n\n{generateInput()}\n\nPlease generate a model semester plan based on the information above.
The first line is the user input and the second is the information scraped off of the major info website.
This information will come in a weird format but classes will probably be as follows:
    ABC 123SOME TITLE HERE0
In that example:
    'ABC 123' is the course code
    'SOME TITLE HERE' is the course title
    '0' is the credits (if you can't find the number of credits do not include the credits and credits should never be zero)
Labs are typically 1 credit so if there is a 1 at the end of a lab course you may try to assume that it is refering to the credit and not the title.
The second should be used to fullfil the initial request and give a detailed semester plan strictly in the format below.
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
you should generate 4 years based on the given information.
"""
        
        # Generate a semester plan using GPT-3
        response = client.chat.completions.create(  #text-davinci-003
            #engine="text-davinci-003",  # or "text-davinci-004" or other available versions
            model="gpt-3.5-turbo",
            messages=[{"role":"system","content":prompt}]
        )
        plan = json.loads(response.choices[0].message.model_dump_json())["content"]
        # jsonPlan = json.loads()
        return plan[(plan.find("Output:")+8):]
    except Exception as e:
        print(f"An error occurred while generating the semester plan:\n{e}")
        return None

# def write_to_file(content, file_path):
#     try:
#         with open(file_path, 'w') as file:
#             file.write(content)
#     except Exception as e:
#         print(f"An error occurred while writing to the file: {e}")
    
def makeJson(plan):
    return {"error":"", "data":{"message":plan}}
    # return {"error":"placeholder... dont be mad pwease", "data":{}}

async def getSemesterPlan(prompt):
    # input_file_path = "input.txt"
    # prompt = read_input_file(input)
    if prompt:
        plan = generate_semester_plan(prompt)
        if plan:
            plan_json = makeJson(plan)
            return plan_json
        else:
            return {"error":"Couldn\'t generate response from prompt!", "data":{}}
    else:
        return {"error":"No input detected!", "data":{}}
