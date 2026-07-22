import numpy as np
import pandas as pd

np.random.seed(42)

returns = np.random.normal(
    loc=0.0008,      # ~20% annual drift
    scale=0.012,     # daily volatility
    size=252,        # one trading year
)

df = pd.DataFrame({
    "Returns": returns
})

df.to_csv("examples/sample_returns.csv", index=False)

print("Sample dataset created!")