import pandas as pd

# Load the keyword data
csv_path = "my_seo_pipeline/data/initial_keywords.csv"
df = pd.read_csv(csv_path)

# Print basic stats
print("Keyword Data Overview:")
print(df.head())
print("\nSearch Volume Statistics:")
print(df["Volume"].describe()) #Keyword,Intent,Volume,Keyword Difficulty,CPC (USD),Competitive Density,SERP Features

# Sort by search volume
df_sorted = df.sort_values(by="Volume", ascending=False)
print("\nTop Keywords:")
print(df_sorted.head())
