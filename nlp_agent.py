import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data files (only once)
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def extract_keywords(query):
    tokens = word_tokenize(query.lower())
    keywords = [word for word in tokens if word.isalnum() and word not in stop_words]
    return keywords

def match_intent(keywords):
    if 'noise' in keywords:
        return 'reduce_noise'
    elif 'filter' in keywords or 'low-pass' in keywords:
        return 'design_filter'
    elif 'distortion' in keywords:
        return 'reduce_distortion'
    else:
        return 'unknown'