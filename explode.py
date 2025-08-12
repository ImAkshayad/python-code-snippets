import pandas as pd
df = pd.read_csv(r'python-code-snippets\csv_data\csv_data.csv')
print(df)
df['Team'] = df['Team'].str.split(',')
exploded_df = df.explode('Team')

print(exploded_df)