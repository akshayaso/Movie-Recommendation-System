import pandas as pd

def clean(filename: str) -> pd.DataFrame:

    df = pd.read_csv(filename)
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')

    df["Runtime"] = df["Runtime"].str.replace("min", "").str.strip()
    df["Runtime"] = pd.to_numeric(df["Runtime"], errors='coerce')

    df["Runtime"] = df["Runtime"].fillna(df["Runtime"].median()).astype(int)

    if "Gross" in df.columns:
        df["Gross"] = df["Gross"].replace("-", 0)
        df["Gross"] = df["Gross"].str.replace(",", "").astype(float, errors='ignore')
        df["Gross"] = df["Gross"].fillna(0)

    if "Meta_score" in df.columns:
        df["Meta_score"] = pd.to_numeric(df["Meta_score"], errors='coerce')
        df["Meta_score"] = df["Meta_score"].fillna(df["Meta_score"].mean())

    if "IMDB_Rating" in df.columns:
        df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors='coerce')
        df["IMDB_Rating"] = df["IMDB_Rating"].fillna(df["IMDB_Rating"].mean())

    if "Released_Year" in df.columns:
        df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors='coerce')
        df["Released_Year"] = df["Released_Year"].fillna(df["Released_Year"].median()).astype(int)

    text_cols = ["Series_Title", "Certificate", "Genre", "Overview", "Director", "Star1", "Star2", "Star3", "Star4"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown").astype(str)

    df["Genre"] = df["Genre"].apply(lambda x: [g.strip() for g in x.split(",")] if x != "Unknown" else [])

    df["Stars"] = df[["Star1", "Star2", "Star3", "Star4"]].values.tolist()

    df = df.reset_index(drop=True)

    return df

if __name__ == "__main__":
    movies_df = clean("imdb_dataset.csv")
    print("Dataset loaded and cleaned successfully!")
    print(movies_df.head(10))

    for i, genres in enumerate(movies_df["Genre"].head(10)):
        print(f"Movie {i + 1} genres:", genres, type(genres))
    for i, stars in enumerate(movies_df["Stars"].head(10)):
        print(f"Movie {i + 1} stars:", stars, type(stars))