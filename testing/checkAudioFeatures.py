# Load audio features
audio = pd.read_csv('billboard_audio_features.csv')

print("\n" + "=" * 50)
print("AUDIO FEATURES INSPECTION")
print("=" * 50)

# 1. Shape and completeness
print(f"\nTotal rows: {len(audio):,}")
print(f"Columns: {audio.columns.tolist()}")
print(f"\nMissing values:\n{audio.isnull().sum()}")

# 2. Unique songs
print(f"\nUnique Performer-Song combinations: {len(audio):,}")

# 3. Feature distributions
print("\n=== Audio Feature Statistics ===")
feature_cols = ['danceability', 'energy', 'valence', 'tempo', 
                'acousticness', 'loudness', 'speechiness', 
                'instrumentalness', 'liveness']
print(audio[feature_cols].describe())

# 4. Categorical features
print(f"\nExplicit tracks: {audio['spotify_track_explicit'].value_counts()}")
print(f"\nMode distribution: {audio['mode'].value_counts()}")
print(f"\nTime signatures: {audio['time_signature'].value_counts()}")

# 5. Genre inspection (critical - may need cleaning)
print(f"\nGenre field sample:")
print(audio['spotify_genre'].value_counts().head(20))
print(f"\nSongs with multiple genres: {audio['spotify_genre'].str.contains(',', na=False).sum()}")

# 6. Check for duplicates
print(f"\nDuplicate Performer-Song pairs: {audio.duplicated(subset=['Performer', 'Song']).sum()}")