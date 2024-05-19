import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.utils import shuffle
import joblib

df_movies = pd.read_csv("TMDB_movie_dataset_v11.csv")
df_movies["overview"] = df_movies["overview"].fillna("")

df_movies_shuffled = shuffle(df_movies)
subset_size = 20000 
df_subset = df_movies_shuffled.head(subset_size)

tfidf = TfidfVectorizer(stop_words="english", min_df=5, max_df=0.8)
tfidf_matrix = tfidf.fit_transform(df_subset["overview"])

# Compute cosine similarity
cosine_sim_subset = linear_kernel(tfidf_matrix, tfidf_matrix)

# mapping movie titles to indices
indices = pd.Series(df_movies.index, index=df_movies['title']).drop_duplicates()

# Save the model
joblib.dump((indices, cosine_sim_subset), "recommendation_model.pkl")

def get_recommendations(title, cosine_sim=None, indices=None):
    if cosine_sim is None or indices is None:
        
        indices, cosine_sim = joblib.load("recommendation_model.pkl")
    idx = indices[title]
    sim_scores = enumerate(cosine_sim[idx])
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    sim_index = [i[0] for i in sim_scores]
    return df_movies["title"].iloc[sim_index].tolist()
