'''
import spacy

nlp = spacy.load("en_core_web_sm")
results = './m3/data/docs/related_docs.json'
evaluation = './m3/evaluation/mlt/evaluation.json'
plots = './m3/evaluation/mlt'

def similarity(plot, similar_plots):
    doc1 = nlp(plot)
    similarities = []
    
    for plot in similar_plots:
        doc2 = nlp(plot)
        similarity = round(doc1.similarity(doc2), 3)
        similarities.append(similarity)
    
    return similarities

def plot_evaluation(results):
    
'''