from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from joblib import load

embedding_dict = None
similar_dict = None

def load_data():
    global similar_dict
    similar_dict = load("cache_similar_words.joblib")

def find_similar_words_from_embedding_dict(keyword):
    if keyword in similar_dict:             # If query already in cache, return query's similar words from cache
        return similar_dict[keyword]
    else:                                   # If not, return the query back
        print(keyword)
        new_word_result = [keyword]
        similar_dict[keyword] = new_word_result
        return new_word_result
    
def text_preprocess(txt):
    lemmatizer = WordNetLemmatizer()
    stops = set(stopwords.words('english'))

    tokens = word_tokenize(txt.lower())                                             # Split text into tokens
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]                  # Lemmatize tokens
    removed_stopword = [word.lower() for word in lemmatized if word not in stops]   # Filter out stopwords from tokens
    words = ' '.join(removed_stopword)                                              # Put tokens back into text
    return words

def find_similar_words(text):
    query_preprocessed = text_preprocess(text)
    query_tokens = word_tokenize(query_preprocessed.lower())
    similar_words = [find_similar_words_from_embedding_dict(word) for word in query_tokens]
    
    return similar_words