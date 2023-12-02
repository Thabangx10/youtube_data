import pandas as pd

df_music = pd.read_csv('music-library-songs.csv')

df_sub = pd.read_csv('subscriptions.csv')

print(df_music.isnull().sum())

print(df_sub.isnull().sum())

print(df_music.duplicated().sum())

print(df_sub.duplicated().sum())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
df_music['Song Title'].value_counts().head(20).plot(kind='bar', color='skyblue')
plt.title('Top 20 Song Titles Distribution')
plt.xlabel('Song Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.figure(figsize=(12, 6))
df_music['Album Title'].value_counts().head(20).plot(kind='bar', color='lightgreen')
plt.title('Top 20 Album Titles Distribution')
plt.xlabel('Album Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.figure(figsize=(12, 6))
df_music['Artist Names'].value_counts().head(20).plot(kind='bar', color='salmon')
plt.title('Top 20 Artist Names Distribution')
plt.xlabel('Artist Name')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.figure(figsize=(12, 6))
df_sub['Channel Title'].value_counts().head(20).plot(kind='bar', color='lightcoral')
plt.title('Top 20 Subscriptions Distribution by Channel Title')
plt.xlabel('Channel Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.show()

top_artists = df_music['Artist Names'].value_counts().head(10)
top_albums = df_music['Album Title'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_artists.values, y=top_artists.index, palette='viridis')
plt.title('Top 10 Most Popular Artists')
plt.xlabel('Number of Songs')
plt.ylabel('Artist')
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=top_albums.values, y=top_albums.index, palette='magma')
plt.title('Top 10 Most Popular Albums')
plt.xlabel('Number of Songs')
plt.ylabel('Album')
plt.show()