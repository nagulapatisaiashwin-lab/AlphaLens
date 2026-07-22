from app.io.loader import load_csv
from app.io.detector import detect_dataset_type

df = load_csv("examples/sample_returns.csv")

dataset = detect_dataset_type(df)

print("=" * 40)
print("DATASET DETECTOR")
print("=" * 40)

print(dataset)