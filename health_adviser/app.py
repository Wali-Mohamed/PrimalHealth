import streamlit as st
import pickle
import time

from elasticsearch import Elasticsearch
from openai import OpenAI

# load the data
with open('semantic_vector_search.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

item=loaded_data[0]['text_vector']
print(item)

client = OpenAI(
    
)


# Connect to the Elasticsearch running in Docker on EC2
es = Elasticsearch(['http://18.170.222.70:9200'])

# Test connection
if es.ping():
    st.success("Connected to Elasticsearch!")
else:
    st.error("Could not connect to Elasticsearch.")




def elastic_search(query, index_name ="diet-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["Chunked_Content"],
                        "type": "best_fields"
                    }
                },
                
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    
    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    return result_docs


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
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    time.sleep(3) # Simulating a delay for the function to work
    return answer


def main():
    st.title("Dietary Assistant LLM")
    st.write("Ask anything related to your diet and health!")

    user_input = st.text_input("Ask your question:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)

if __name__ == "__main__":
    main()