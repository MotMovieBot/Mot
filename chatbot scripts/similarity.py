
import nltk, nltk.tokenize, nltk.corpus, nltk.stem
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords, wordnet
import pandas as pd

#lowercase text
def to_lower(text):
    return ' '.join([w.lower() for w in word_tokenize(text)])

#remove stopwords
def remove_stopwords(text):
    no_stop = text.split()
    stopwordz = stopwords.words('english')
    for word in no_stop:
        for stopword in stopwordz:
            if word == stopword:
                no_stop.remove(word)
    return ' '.join(no_stop)

#remove punctuation
def strip_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return ' '.join(tokenizer.tokenize(text))

#preprocess text
def preprocess(text):
    lower_text = to_lower(text)
    text_no_stopwords = remove_stopwords(lower_text)
    text_no_punct = strip_punctuation(text_no_stopwords)
    return text_no_punct

#application of the function preprocess(text) to our corpus 
verses_no_punct=[]
db = pd.read_csv("data_chatbotACTION.csv", sep=";")

for x in db['description']:
    x_preprocessed= preprocess(x)
    verses_no_punct.append(x_preprocessed)


new_data= {'title': db["title"], 'description': verses_no_punct}
new_df=pd.DataFrame(new_data)

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
TfidfVec = TfidfVectorizer(ngram_range=(1,2))
#Convert the text to a matrix of TF-IDF features
tfidf = TfidfVec.fit_transform(new_df['description'])
feature_names = TfidfVec.get_feature_names()

#Creating a cosine similarity matrix from TF-IDF vectors
cosine_sim = cosine_similarity(tfidf, tfidf)

def response(title):
    recommended_content_titles=[]
    content_titles = pd.Series(new_df['title'])
    content_index = content_titles[content_titles == title].index[0]
    similarity_scores_list = pd.Series(cosine_sim[content_index]).sort_values(ascending=False)
    similar_content_indices = list(similarity_scores_list.iloc[1:2].index)
    for content in similar_content_indices:
        recommended_content_titles.append(str(new_df['title'][content]).upper())
    return(', '.join(recommended_content_titles))



