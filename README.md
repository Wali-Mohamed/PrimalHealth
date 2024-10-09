# Primal Insight

![Alt text](/images/Primal_Diet_App_Interface.jpeg)


### Problem Description

Primal Insight is a Retrieval-Augmented Generation (RAG) application that helps individuals seeking guidance on the Primal Diet, a dietary approach focused on consuming raw, unprocessed foods. The problem this project addresses is the difficulty in extracting valuable and contextually accurate diet and health advice from large volumes of unstructured online conversations. Information shared within health-focused communities can be overwhelming, and users struggle to find specific, relevant insights in real time.

This project solves the problem by using machine learning models to analyze and retrieve diet-related insights from extensive Telegram group discussions about the Primal Diet. It provides users with precise and actionable responses based on community conversations, improving accessibility to advice on this niche diet.

### Data Description

The data comes from a Telegram group where members discuss various aspects of the Primal Diet, collected between February 14, 2019, and September 14, 2024. Each conversation is transformed into a structured dataset with fields for timestamp and content. An example of the dataset looks like this:

|    Date       |    Time  | Content                                                 |
|---------------|----------|---------------------------------------------------------|
| 2024-09-14    | 03:15    | are wild animals safe to eat raw?                        |
| 2024-09-14    | 01:16    | I saw this on eat raw meat channel. I wouldn’t...        |
| 2024-09-14    | 00:31    | You got vaxxed even after listening to aajonus...        |
| 2024-09-14    | 08:00    | Is it possible for a detox to last 4 months or...        |
| 2024-09-14    | 03:50    | What to do with 10L of raw milk that are alrea...        |

### Topic Analysis

Using a Gensim LDA (Latent Dirichlet Allocation) model, we identified key topics discussed within the dataset. These topics reflect the core areas of interest in the Primal Diet community, which include:

1. **Water Usage**: Discussions about hydration and how people use water in their daily habits.

2. **Diet Preferences**: Focus on various diet approaches, including those advocated by figures like Aajonus Vonderplanitz.

3. **Primal Diet**: Conversations about the Primal diet and influencers like Sv3rige promoting raw food.

4. **Raw Dairy and Meat**: Emphasis on consuming raw milk, meat, and cheese for health benefits.

5. **Raw Food and Health**: Discussion on the impact of raw food, especially meat, on the body and overall health.


### Project Solution

Primal Insight processes these conversations, transforming them into an easily accessible and structured knowledge base. This enables users to retrieve relevant advice on diet and health directly from the community's discussions, making it easier to stay informed and follow the Primal Diet. By filtering out irrelevant content and providing targeted responses, Primal Insight offers a streamlined experience for users seeking guidance on raw and natural food consumption.
You will all the data used in data folder and it two sub folders: raw and clean.

# Project Technologies

- **Python 3.12**  
  For general programming and application logic.

- **Docker and Docker Compose**  
  Used for containerization and orchestration of services such as PostgreSQL, Flask, Grafana, etc.

- **Beautiful Soup**  
  For web scraping and parsing HTML data.

- **gensim (LDA)**  
  Used for topic modeling through Latent Dirichlet Allocation (LDA).

- **NLTK**  
  Natural Language Toolkit used for various NLP tasks such as tokenization, stemming, and more.

- **tqdm**  
  A progress bar tool for showing the progress of loops and operations.

- **Minsearch**  
  Full-text search engine used for efficient information retrieval.

- **LanceDB**  
  Vector database used for managing embeddings and performing similarity searches.

- **Sentence Transformers Pretrained Model ('multi-qa-MiniLM-L6-cos-v1')**  
  A transformer-based model for generating sentence embeddings, particularly used for similarity search and question-answering tasks.

- **Flask**  
  API interface used to expose your application logic and interact with other services.

- **Grafana**  
  For monitoring your services and visualizing key performance indicators.

- **PostgreSQL**  
  Backend for Grafana, used to store and retrieve data in a relational format.

- **OpenAI**  
  Large language model (LLM) integrated for natural language understanding and processing tasks.

#### Preparation
Since we use OpenAI, you need to provide the API key:

Install direnv. If you use Ubuntu, run sudo apt install direnv and then direnv hook bash >> ~/.bashrc.
create file name .envrc and insert your key there. Use export openain_api='yourkey'
For OpenAI, it's recommended to create a new project and use a separate key.
Run direnv allow to load the key into your environment.
For dependency management, we use pipenv, so you need to install it:

#### Method 1

pip install requirements
I used venv environments and therefore you can pip install requirements.txt
Once installed, you can install the app dependencies:


Before the application starts for the first time, the database needs to be initialized.

- First, run postgres:
- change directory
cd Flask_App

Then run the db_prep.py script:
```
python db_prep.py
```
then 
```
python local_app.py
```
### Method 2

docker-compose up

export POSTGRES_HOST=localhost
python db_prep.py
To check the content of the database, use pgcli (already installed with pipenv):
```

```
\d conversations;
And select from this table:

select * from conversations;



# Application Code Structure

The code for the application is located in the `fitness_assistant` folder:

- **`local_app.py`** - The Flask API, the main entry point to the application.
- **`local_rag.py`** - The main RAG logic for retrieving the data and building the prompt.
- **`local_ingest.py`** - Handles loading the data into the knowledge base.
- **`minsearch.py`** - An in-memory search engine.
- **`db.py`** - Contains the logic for logging the requests and responses to PostgreSQL.
- **`db_prep.py`** - Script for initializing the database.


### Experiments

For experiments, we use Jupyter notebooks, which are located in the `notebooks` folder.

To start Jupyter, run the following commands:

```bash
cd notebooks
you can active the environment where you installed requirements

### Notebooks

We have the following notebooks:

- **`rag-test.ipynb`**: The RAG flow and system evaluation.
- **`evaluation-data-generation.ipynb`**: Generates the ground truth dataset for retrieval evaluation.

### Retrieval Evaluation

The basic approach — using Minsearch without any boosting — produced the following metrics:

- **Hit rate**: 76%
- **MRR**: 56%

The improved version (with tuned boosting) gave:

same result with no improvement

#### The Best Boosting Parameters:

```python
boost = {
    'content': 1.591310685457374,
    
}

### RAG Flow Evaluation

We used the **LLM-as-a-Judge** metric to evaluate the quality of our RAG flow.

For **gpt-3.5-turbo**, in a sample of 200 records, we observed:

- **126 (63%)** RELEVANT
- **62 (31%)** PARTLY_RELEVANT
- **12 (6%)** NON_RELEVANT

We also tested **gpt-4o-mini**, and the results were:

- **141 (70.5%)** RELEVANT
- **51 (25.5%)** PARTLY_RELEVANT
- **8 (4%)** NON_RELEVANT

The difference between the two models is minimal, so we opted for **gpt-4o-mini**.

I tested **gp 40** but it was lower
We also tested **gpt-4o-mini**, with lanceDB semanctic vector search and the results were:

- **143 (71.5%)** RELEVANT
- **54 (27%)** PARTLY_RELEVANT
- **3 (1.5%)** NON_RELEVANT


### Disclaimer

This application is for informational purposes only and is not a substitute for professional health advice. Always consult with a qualified healthcare provider before making any significant dietary or health decisions.
