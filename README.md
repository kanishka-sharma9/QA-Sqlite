# QA-Sqlite
  This is a chatbot assistant that understands Natural Language queries to extract required information form the Sqlite database.<br>
  <a href="https://huggingface.co/spaces/sharma-kanishka/QA-Sqlite">Project link<a/>

# An explanation of how the assistant works.
  1. User enters the required information in natural language.
  2. The request gets converted into a Sqlite query and is executed on the tables.
  3. The result is formatted and output to the user in tabular manner.
  
# Steps to run the project locally.
  1. Clone the repo.
  2. Create .env file or use <b>setx</b> to set your GROQ_API_KEY as an environment variable.
  3. Go to the command prompt and run `streamlit run app.py`

# Known limitations or suggestions for improvement.
  1. Use auto prompting to improve DB understanding by the assistant, and to account for any future changes in the schema.
  2. use HUB for better contextual understanding and less hallucinations.
  3. Use agents to execute all subprocesses simultaneously.
