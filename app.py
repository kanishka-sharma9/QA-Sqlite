import streamlit as st
from db import main
from ai import generate_sql_response,execute_query,print_table

st.set_page_config(
    page_title="Ajackus Assignment",
)
if "db" not in st.session_state:
    st.session_state['db']=True
    main()
user_input=st.text_area(label="Enter:")
if st.button("Generate"):
    query=generate_sql_response(user_input)
    query_op=execute_query(query)
    response=print_table(query_op)

    st.write(response)