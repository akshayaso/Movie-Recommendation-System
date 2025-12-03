import heapq
from typing import List, Dict
import pandas as pd


def top_rated_movies(recommended_movies: List[str], df: pd.DataFrame, n: int = 5) -> List[str]:

    heap = []
    for title in recommended_movies:
        row = df[df["Series_Title"] == title]
        if not row.empty:
            rating = row.iloc[0]["IMDB_Rating"]
            heapq.heappush(heap, (-rating, title))

    top_movies = []
    for _ in range(min(n, len(heap))):
        rating, title = heapq.heappop(heap)
        top_movies.append(title)

    return top_movies


if __name__ == "__main__":
    from all_movies import clean
    from build_graph import build_movie_graph
    from search_algorithms import bfs_recommend

    df = clean("imdb_dataset.csv")
    graph = build_movie_graph(df)

    movie = "Iron Man"
    recommended = bfs_recommend(graph, movie, max_depth=2)

    top_movies = top_rated_movies(recommended, df, n=5)
    print(f"Top rated movies similar to '{movie}': {top_movies}")
