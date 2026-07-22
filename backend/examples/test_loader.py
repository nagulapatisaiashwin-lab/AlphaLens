from app.io.loader import load_csv

df = load_csv("examples/sample_returns.csv")

print("=" * 50)
print("CSV Loaded Successfully")
print("=" * 50)

print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print(f"\nRows: {len(df)}")