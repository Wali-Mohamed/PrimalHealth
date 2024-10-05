import streamlit as st
import pickle
import json
import time
#from elasticsearch import Elasticsearch
from openai import OpenAI
import minsearch

import os
#st.write("Current working directory:", os.getcwd())
# Construct the full path to the file


st.write(os.getcwd())
file_path = os.path.join(os.getcwd(), r'data\clean_data\documents.json')
st.write(file_path)



client = OpenAI(
    
)

with open(file_path, 'r') as file:
    documents=json.load(file)
st.write(documents[0])

index = minsearch.Index(
    text_fields=['Chunked_Content'],
    keyword_fields=[]
)
index.fit(documents)
def search(query):
    boost = {
        'Chunked_Content': 1.9366969407339725   
    }

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results

def build_prompt(query, search_results):
    prompt_template = """
You're a primal health adviser. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
        context = context + f"Chunked_Content: {doc['Chunked_Content']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    time.sleep(1) # Simulating a delay for the function to work
    return answer


def main():
    st.title("Dietary Assistant LLM by W Mohamed")
    st.write("Ask anything related to your diet and health!")

    user_input = st.text_input("Ask your question:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)

if __name__ == "__main__":
    main()