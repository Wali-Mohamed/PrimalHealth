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



### Disclaimer

This application is for informational purposes only and is not a substitute for professional health advice. Always consult with a qualified healthcare provider before making any significant dietary or health decisions.
