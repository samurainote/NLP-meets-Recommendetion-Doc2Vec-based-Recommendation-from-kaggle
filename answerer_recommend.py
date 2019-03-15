
from query_preprocessing import text_cleaner

import gensim
from gensim.models import doc2vec
from gensim.models.doc2vec import TaggedDocument

def answerer_recommender(query_title, query_body, data1, data2, w1=60, w2=20, w3=20):

    # preprocessing
    query = query_title + "\n" + query_body
    clean_query = text_cleaner(query)
    tokens =  TaggedDocument(words=clean_query.split(), tags=["101"])

    pretrained_doc2vec = doc2vec.Doc2Vec.load('my_doc2vec.model')
    # document_vector = pretrained_doc2vec.infer_vector(tokens)
    top500_past_query = pretrained_doc2vec.docvecs.most_similar(tokens, topn=500)

    for row in data1.itertuples():
