# game-stats-analyser.py
# Activity: Gaming Leaderboard Analyser
# Lesson: Introduction to Pandas

import pandas as pd

# PART 1 - Create a Pandas Series of top player scores
print('--- PART 1: Pandas Series ---')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['Nightwolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])
print(players)

# PART 2 - Create a DataFrame of gaming stats
print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player': ['Nightwolf', 'StarBlaze', 'PixelKing', 'CyberFox','ironstorm'],
    'level': [42,38,35,30,27],
    'score': [98500,87200,76400,65100,54800],
    'wins' : [210,185,162,140,118]
}
df = pd.DataFrame(data)
print(df)

#PART-3 acces data.loc

print()
print('--------- PART 3: Accessing Rows------------ ')
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:1')
print(df.loc[2:31])

#part4 load leaderboard

print()
print('----PART4:Reading csv file----')
full_df = pd.read_csv('leaderboard.csv')
print(full_df.head())
print()
print('last 3 rows(tail):')
print(full_df.tail(3))
print()
print('dataset info:')
print(full_df.info())

# PART 5 - Clean the data
print()
print('--- PART 5: Cleaning Data ---')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print("missing values filled with 0(fillna):")
filled_df = full_df.fillna(0)
print(filled_df.to_string())

