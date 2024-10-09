import os
import pandas as pd

import minsearch

project=os.getenv('Project_Path')
DATA_PATH = os.path.join(project, r'./data/clean_data/data_chunked_5s.csv')  # use this line when running locally




def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    
    documents = df.to_dict(orient="records")

    index = minsearch.Index(
        text_fields=[
            
            "content",
        ],
        keyword_fields=[],
    )

    index.fit(documents)
    return index