from collections import defaultdict
from typing import Dict, List
import pandas as pd


def build_movie_graph(df: pd.DataFrame) -> Dict[str, List[str]]:

    graph = defaultdict(list)

    movies = df.to_dict(orient='records')

    for i in range(len(movies)):
        movie_i = movies[i]
        title_i = movie_i["Series_Title"]
        genres_i = set(movie_i["Genre"])
        stars_i = set(movie_i["Stars"])

        for j in range(i + 1, len(movies)):
            movie_j = movies[j]
            title_j = movie_j["Series_Title"]
            genres_j = set(movie_j["Genre"])
            stars_j = set(movie_j["Stars"])

            if genres_i.intersection(genres_j) or stars_i.intersection(stars_j):
                graph[title_i].append(title_j)
                graph[title_j].append(title_i)

    return graph


if __name__ == "__main__":

    from all_movies import clean

    df = clean("imdb_dataset.csv")
    movie_graph = build_movie_graph(df)

    for movie, neighbors in list(movie_graph.items())[:5]:
        print(f"{movie} --> {neighbors[:5]}")
