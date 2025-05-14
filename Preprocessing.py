import pickle
import nltk
import string # remove punctuation
nltk.download('stopwords')
from nltk.corpus import stopwords
 #spell correction
from textblob import TextBlob
from nltk.corpus import wordnet #lemm
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('omw-1.4')

#parameter : words : list of strings
#Return : string ( concating all the strings in the parameter passed )
def words2text(words):
    text = ''
    for i in words:
        text += i + ' '
    return text

# parameter : text : string
# Return : lowercase of parameter text
def textTolower(text):
    return text.lower()

# parameter : text : string
# Return : returns the text after removing new line character
def removeslashn(text):
    words = text.split('\n')
    return words2text(words)

## parameter : text : string
# Return : returns the text after removing Punctuations
def removePunctuation(text):
    punct = string.punctuation
    text_p = [i for i in text if i not in punct]
    text = ''
    for i in text_p:
        text += i
    return text


## parameter : text : string
# Return : returns the text after removing stopwords
def removeStopWords(text):
    stopword = stopwords.words('english')
    words = text.split(' ')
    words = [i for i in words if i not in stopword]
    text = words2text(words)
    return text

#parameter : text : string
# Return : returns the text after spellCorrection of each word in the text passed
def spellCorrection(text):
    text = TextBlob(text).correct()
    return str(text)

#parameter : tag
#return : returns Part Of Speech
def getPOS(tag):
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    if tag in tag_dict:
        return tag_dict[tag]
    else:
        return wordnet.NOUN

## parameter : text : string
# Return : returns the text after performing lemmatization
def lemmatize(text):
    words = text.split(' ')
    lem = []
    lemmatizer = WordNetLemmatizer()
    for i in words:
        tag = getPOS(nltk.pos_tag([i])[0][1][0].upper())
        lem.append(lemmatizer.lemmatize(i, pos=tag))
    text = words2text(lem)
    return text

## parameter : text : string
# Return : cleaned text data
def TextPreprocessing(text):
    text = textTolower(text)
    text = removeslashn(text)
    text = spellCorrection(text)
    text = removePunctuation(text)
    text = removeStopWords(text)
    text = lemmatize(text)
    return text


