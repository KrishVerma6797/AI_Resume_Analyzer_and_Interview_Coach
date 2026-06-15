from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model=SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(resume,jd):
    resume_emb=model.encode(resume)
    jd_emb=model.encode(jd)
    similarity=cosine_similarity([resume_emb],[jd_emb])
    return similarity[0][0]*100