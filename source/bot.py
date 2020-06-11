import pandas as pd
import nltk
import re
from nltk.stem import wordnet
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import pos_tag
from sklearn.metrics import pairwise_distances
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

data_frame = pd.read_excel('data/dialog_talk_agent.xlsx')

data_frame.ffill(axis=0, inplace=True)


def text_normalization(text: str) -> str:
    text = str(text).lower()
    char_text = re.sub(r'[^ a-z]', '', text)
    tokens = word_tokenize(char_text)
    lemma = wordnet.WordNetLemmatizer()
    tags_list = pos_tag(tokens)
    lemma_words = []
    for token, pos_token in tags_list:
        if pos_token.startswith('V'):
            pos_val = 'v'
        elif pos_token.startswith('J'):
            pos_val = 'a'
        elif pos_token.startswith('R'):
            pos_val = 'r'
        else:
            pos_val = 'n'
        lemma_token = lemma.lemmatize(token, pos_val)
        lemma_words.append(lemma_token)
    return ' '.join(lemma_words)


data_frame['lemmatized_text'] = data_frame['Context'].apply(text_normalization)

tfidf = TfidfVectorizer()
x_tfidf = tfidf.fit_transform(data_frame['lemmatized_text']).toarray()
df_tfidf = pd.DataFrame(x_tfidf, columns=tfidf.get_feature_names())


def chat_tfidf(text: str) -> str:
    lemma = text_normalization(text)
    tf = tfidf.transform([lemma]).toarray()
    cos = 1 - pairwise_distances(df_tfidf, tf, metric='cosine')
    index_val = cos.argmax()
    return data_frame['Text Response'].loc[index_val]


def _stopword(text: str) -> str:
    tag_list = pos_tag(nltk.word_tokenize(text))
    stop = stopwords.words('english')
    lemma = wordnet.WordNetLemmatizer()
    lemma_word = []
    for token, pos_token in tag_list:
        if token in stop:
            continue
        if pos_token.startswith('V'):
            pos_val = 'v'
        elif pos_token.startswith('J'):
            pos_val = 'a'
        elif pos_token.startswith('R'):
            pos_val = 'r'
        else:
            pos_val = 'n'
        lemma_token = lemma.lemmatize(token, pos_val)
        lemma_word.append(lemma_token)
    return ' '.join(lemma_word)


cv = CountVectorizer()
X = cv.fit_transform(data_frame['lemmatized_text']).toarray()
features = cv.get_feature_names()
data_frame_bow = pd.DataFrame(X, columns=features)


def chat_bow(text: str) -> str:
    s = _stopword(text)
    lemma = text_normalization(s)
    bow = cv.transform([lemma]).toarray()
    cos = 1 - pairwise_distances(data_frame_bow, bow, metric='cosine')
    index_val = cos.argmax()
    return data_frame['Text Response'].loc[index_val]
