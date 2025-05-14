# import Preprocessing
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import Preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
# return cosine similarity
def cosine_Sim(t1, t2):
    cv = CountVectorizer(max_features=1000)
    # x = {}
    # x['index'] = int(1)
    # x['text'] = t1
    # z = {}
    # z['index'] = int(2)
    # z['text'] = t2
    x = {'index': int(1), 'text': t1}
    z = {'index': int(2), 'text': t2}
    
    # Create a list of DataFrames to concatenate
    d = pd.DataFrame([x,z])
    # d = d.append(x, ignore_index=True)
    # d = d.append(z, ignore_index=True)

    vectors = cv.fit_transform(d['text']).toarray()
    similarity_cntv = cosine_similarity(vectors)[0][1]

    tfidfvectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
    tfidf_wm = tfidfvectorizer.fit_transform(d['text']).toarray()
    tfidf_tokens = tfidfvectorizer.get_feature_names_out()
    df_tfidfvect = pd.DataFrame(data=tfidf_wm, index=['Doc1', 'Doc2'], columns=tfidf_tokens)

    similarity_tfidf = cosine_similarity(tfidf_wm)[0][1]

    return (similarity_tfidf+similarity_cntv)/2




# score for skills
def skillMatching(skills,res):

    skills = skills.lower()
    skills = skills.split(',')
    print(skills)
    words = res.split(',')
    res = Preprocessing.words2text(words)
    words = [ i.strip() for i in res.split(' ')]
    cnt = 0
    for i in skills :
        if i in words:
            cnt += 1

  #print(cnt,len(skills))
    return cnt/len(skills)
# score for Experience
def CheckExpr(e,exp):
    if e >= exp:
        return (e-exp+1)/(e+exp+1)
    else:
        return 0

# return Jaccard Similarity
def Jaccard_Similarity(doc1, doc2):
    # List the unique words in a document
    words_doc1 = set(doc1.lower().split())
    words_doc2 = set(doc2.lower().split())

    # Find the intersection of words list of doc1 & doc2
    intersection = words_doc1.intersection(words_doc2)

    # Find the union of words list of doc1 & doc2
    union = words_doc1.union(words_doc2)

    # Calculate Jaccard similarity score
    # using length of intersection set divided by length of union set
    return float(len(intersection)) / len(union)