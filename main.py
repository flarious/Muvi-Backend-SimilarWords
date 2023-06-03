from fastapi import FastAPI
from threading import Thread
from find_similar_words import find_similar_words, load_data

app = FastAPI()

@app.get("/")
async def placeholder():
    return {"status": "This is placeholder. Loading cached similar word dictionary"}

# Find similar word from query
@app.get("/find_similar/{keyword}")
async def find_similar(keyword: str):
    similar_words = find_similar_words(keyword)
    return {"similar_words": similar_words}

# Workaround in case of loading cache take too long
def load_model_at_startup():
    print("Cached similar word dictionary is loading")

    load_data()

    print("Cached similar word dictionary has been loaded")

Thread(target=load_model_at_startup).start()