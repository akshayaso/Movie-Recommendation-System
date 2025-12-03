from collections import deque
from typing import Dict, List, Set


def bfs_recommend(graph: Dict[str, List[str]], start_movie: str, max_depth: int = 2) -> List[str]:

    if start_movie not in graph:
        print(f"Movie '{start_movie}' not found in graph.")
        return []

    visited: Set[str] = set()
    queue = deque([(start_movie, 0)])
    recommendations: List[str] = []

    while queue:
        current_movie, depth = queue.popleft()

        if current_movie not in visited:
            visited.add(current_movie)

            if depth > 0:
                recommendations.append(current_movie)

            if depth < max_depth:
                for neighbor in graph[current_movie]:
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1))

    return recommendations


def dfs_cluster(graph: Dict[str, List[str]], start_movie: str) -> List[str]:
    visited = set()
    cluster = []

    def dfs(movie: str):
        visited.add(movie)
        cluster.append(movie)

        for neighbor in graph[movie]:
            if neighbor not in visited:
                dfs(neighbor)

    if start_movie not in graph:
        print(f"Movie '{start_movie}' not found in graph.")
        return []

    dfs(start_movie)
    return cluster




if __name__ == "__main__":
    from all_movies import clean
    from build_graph import build_movie_graph

    df = clean("imdb_dataset.csv")
    graph = build_movie_graph(df)

    movie = "Iron Man"
    recs = bfs_recommend(graph, movie, max_depth=2)
    print(f"Movies recommended for '{movie}': {recs[:10]}")

    cluster = dfs_cluster(graph, movie)
    print(f"Movies in the '{movie}' cluster: {cluster[:10]}")
