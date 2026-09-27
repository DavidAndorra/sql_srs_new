import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "Group by","Windows Functions"),
    index=None,
    placeholder="Select contact method ...",
)

st.write('You selected', option)


data = {"a":[1, 2, 3], "b":[4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat",'Dog','Owl'])

with tab1:
    st.header('Cat')
    query_text = st.text_area(label="Enter SQL command")
    st.dataframe(df)
    st.write(f'Your query was {query_text}')
    db2=duckdb.query(query_text)
    st.dataframe(db2)
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3:
    st.header('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')