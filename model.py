import numpy as np
import pickle
import nltk
import config
from langdetect import detect
from deep_translator import GoogleTranslator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import contractions

import warnings
warnings.filterwarnings('ignore')

class Model:

    def __init__(self):

        self.model = pickle.load(open(config.MODEL_FILE_PATH,'rb'))
        self.vector = pickle.load(open(config.VECTOR_FILE_PATH,'rb'))

    def result(self,data):

        def lang_converter(data):
            lang = detect(data)
            if lang == 'en':
                return data
            else:
                output = GoogleTranslator(source='auto',target='en').translate(data)
                return output
            
        def remove_spaces(text):
            clean_text = text.replace('\n',' ').replace('\t',' ').replace('  ',' ')
            return clean_text
        
        def split_words(data):
            text = contractions.fix(data)
            return text
        
        stopword_list = stopwords.words('english')
        stopword_list.remove('no')
        stopword_list.remove('nor')
        stopword_list.remove('not')
        
        def clean_text(data):
            token = word_tokenize(data)
            text = [word.lower() for word in token if (word.lower() not in stopword_list) and (word not in punctuation) and (len(word)>2) and (word.isalpha())]
            return " ".join(text)
        
        text = lang_converter(data)
        print("Input text:",text)
        text = remove_spaces(text)
        text = split_words(text)
        text = clean_text(text)
        test_array = self.vector.transform([text]).A
        test_array = np.asarray(test_array)
        
        prediction = self.model.predict(test_array)
        if prediction[0] == 0:
            print("This is negative review".upper())
        else:
            print("this is positive review".upper())

        return prediction[0]
