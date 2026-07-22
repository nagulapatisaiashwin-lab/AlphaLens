import pandas as pd

from app.report import (
    analyze_strategy,
    print_report,
)

returns = pd.Series([
    0.01,
    -0.02,
    0.015,
    0.03,
    -0.01,
])

report = analyze_strategy(returns)

print_report(report)