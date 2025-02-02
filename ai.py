from langchain_groq.chat_models import ChatGroq
# from langchain_ollama.chat_models import ChatOllama
from dotenv import load_dotenv
load_dotenv()
import sqlite3
import os
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

llm=ChatGroq(model_name="llama-3.3-70b-versatile")

def generate_sql_response(request):
    prompt=f"""You are a SQL expert with decades of experience.using your experience and skills generate 
    a sql query that generates the correct output for the below request.\n
    <INST>You have access to two tables:[Employees (ID, Name, Department, Salary, Hire_Date), Departments (ID, Name, Manager)].
    Return just the sql query, NO DESCRIPTION, NO DELIMITER</INST>\n\n
    
    <request>{request}</request>"""

    response=llm.invoke(prompt)
    return response.content
def execute_query(query):
    cur=sqlite3.connect("company.db").cursor()
    res=cur.execute(query)
    data=[]
    for e in res:
        data.append(e)
    
    return data

def print_table(data):
    prompt=f"""You are given a python list in which each element represents the output of an executed sql query.
    your task is to format this data and return in tabular manner titled "Output".
    Don't give the code for the same, only the output.
    In case the list is empty simply return "No Matching Entities found.
    <list>{data}</list>"""

    response=llm.invoke(prompt)

    return response.content

