from app.io.loader import load_csv
from app.io.normalizer import extract_returns

df = load_csv("examples/sample_returns.csv")

returns = extract_returns(df)

print("=" * 50)
print("NORMALIZED RETURNS")
print("=" * 50)

print(returns.head())