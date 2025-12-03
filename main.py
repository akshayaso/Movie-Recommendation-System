# main.py

from all_movies import clean
from build_graph import build_movie_graph
from search_algorithms import bfs_recommend, dfs_cluster
from heap_ranking import top_rated_movies

def main():

    # Function clean from all_movies
    print("Loading and cleaning dataset")
    movies_df = clean("imdb_dataset.csv")
    print(f"Dataset loaded successfully! Total movies: {len(movies_df)}\n")

    # Function build_movie_graph from build_graph
    print("Building movie similarity graph")
    movie_graph = build_movie_graph(movies_df)
    print(f"Graph built successfully! Total movies in graph: {len(movie_graph)}\n")

    # User input of movie name
    movie_name = input("Enter a movie name to get recommendations: ").strip()

    # Function bfs_recommend from search_algorithms
    recommended_movies = bfs_recommend(movie_graph, movie_name, max_depth=2)
    if not recommended_movies:
        print(f"No recommendations found for '{movie_name}'.")
        return

    # Function top_rated_movies from heap_ranking
    top_movies = top_rated_movies(recommended_movies, movies_df, n=5)

    # Printing the Results
    print(f"\nTop 5 recommended movies similar to '{movie_name}':")
    for i, movie in enumerate(top_movies, 1):
        rating = movies_df[movies_df["Series_Title"] == movie].iloc[0]["IMDB_Rating"]
        print(f"{i}. {movie} (IMDb Rating: {rating})")

    movie = "Iron Man"
    recs = bfs_recommend(movie_graph, movie, max_depth=2)
    print(f"Movies recommended for '{movie}': {recs[:10]}")

    cluster = dfs_cluster(movie_graph, movie)
    print(f"Movies in the '{movie}' cluster: {cluster[:10]}")


if __name__ == "__main__":
    main()
