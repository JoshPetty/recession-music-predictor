import pandas as pd
import numpy as np

# Load chart data
charts = pd.read_csv(r"C:\Users\joshu\OneDrive\Desktop\CS74\Final_Project\Hot Stuff.csv")

# Critical inspection questions:
print("=" * 50)
print("CHART DATA INSPECTION")
print("=" * 50)

# 1. Shape and completeness
print(f"\nTotal rows: {len(charts):,}")
print(f"Columns: {charts.columns.tolist()}")
print(f"\nMissing values:\n{charts.isnull().sum()}")

# 2. Time range
print(f"\nDate range: {charts['WeekID'].min()} to {charts['WeekID'].max()}")
print(f"Number of unique weeks: {charts['WeekID'].nunique()}")

# 3. Song coverage
print(f"\nUnique songs (SongID): {charts['SongID'].nunique():,}")
print(f"Unique performers: {charts['Performer'].nunique():,}")

# 4. Chart position distribution
print(f"\nWeek Position range: {charts['Week Position'].min()} - {charts['Week Position'].max()}")
print(f"Positions per week (should be ~100):\n{charts.groupby('WeekID')['Week Position'].count().describe()}")

# 5. Instance variable (critical for breaks)
print(f"\nInstance values: {sorted(charts['Instance'].unique())}")
print(f"Songs with multiple instances: {(charts.groupby('SongID')['Instance'].max() > 1).sum()}")

# 6. Sample inspection
print("\n=== First few rows ===")
print(charts.head())

print("\n=== Random song's full chart run ===")
sample_song = charts['SongID'].value_counts().index[10]  # Pick 10th most common
print(charts[charts['SongID'] == sample_song].sort_values('WeekID'))