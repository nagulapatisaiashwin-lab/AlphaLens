from app.io.loader import load_csv
from app.io.normalizer import extract_returns
from app.visualization.heatmap import plot_monthly_heatmap


df = load_csv("examples/realistic_returns.csv")

returns = extract_returns(df)

plot_monthly_heatmap(returns)