"""
Factor analytics for AlphaLens.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import statsmodels.api as sm


@dataclass
class RegressionResult:
    """
    Container for regression outputs.
    """

    coefficients: dict[str, float]
    r_squared: float
    adjusted_r_squared: float
    p_values: dict[str, float]
    standard_errors: dict[str, float]


def _validate_factor_data(
    factor_data: pd.DataFrame,
    required_columns: list[str],
) -> None:
    """
    Validate factor dataset.
    """

    if factor_data.empty:
        raise ValueError("Factor data is empty.")

    missing = [
        column
        for column in required_columns
        if column not in factor_data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing factor columns: {', '.join(missing)}"
        )

    if factor_data.index.hasnans:
        raise ValueError(
            "Factor data index contains missing values."
        )

    if factor_data[required_columns].isna().any().any():
        raise ValueError(
            "Factor data contains missing values."
        )


def _align_data(
    portfolio_returns: pd.Series,
    factor_data: pd.DataFrame,
) -> tuple[pd.Series, pd.DataFrame]:
    """
    Align portfolio returns with factor data.
    """

    aligned = pd.concat(
        [portfolio_returns.rename("portfolio"), factor_data],
        axis=1,
        join="inner",
    ).dropna()

    if aligned.empty:
        raise ValueError(
            "No overlapping dates between returns and factor data."
        )

    return (
        aligned["portfolio"],
        aligned.drop(columns="portfolio"),
    )


def _run_regression(
    y: pd.Series,
    X: pd.DataFrame,
) -> RegressionResult:
    """
    Run an OLS regression.
    """

    X = sm.add_constant(X)

    model = sm.OLS(
        y,
        X,
    ).fit()

    return RegressionResult(
        coefficients=model.params.to_dict(),
        r_squared=float(model.rsquared),
        adjusted_r_squared=float(model.rsquared_adj),
        p_values=model.pvalues.to_dict(),
        standard_errors=model.bse.to_dict(),
    )

def _capm(
    portfolio_returns: pd.Series,
    factor_data: pd.DataFrame,
) -> RegressionResult:
    """
    Run CAPM regression.
    """

    _validate_factor_data(
        factor_data,
        ["MKT_RF", "RF"],
    )

    portfolio, factors = _align_data(
        portfolio_returns,
        factor_data,
    )

    excess_returns = portfolio - factors["RF"]

    return _run_regression(
        excess_returns,
        factors[["MKT_RF"]],
    )


def _fama_french(
    portfolio_returns: pd.Series,
    factor_data: pd.DataFrame,
) -> RegressionResult:
    """
    Run Fama-French 3-Factor regression.
    """

    _validate_factor_data(
        factor_data,
        ["MKT_RF", "SMB", "HML", "RF"],
    )

    portfolio, factors = _align_data(
        portfolio_returns,
        factor_data,
    )

    excess_returns = portfolio - factors["RF"]

    return _run_regression(
        excess_returns,
        factors[
            ["MKT_RF", "SMB", "HML"]
        ],
    )


def _carhart(
    portfolio_returns: pd.Series,
    factor_data: pd.DataFrame,
) -> RegressionResult:
    """
    Run Carhart 4-Factor regression.
    """

    _validate_factor_data(
        factor_data,
        ["MKT_RF", "SMB", "HML", "MOM", "RF"],
    )

    portfolio, factors = _align_data(
        portfolio_returns,
        factor_data,
    )

    excess_returns = portfolio - factors["RF"]

    return _run_regression(
        excess_returns,
        factors[
            ["MKT_RF", "SMB", "HML", "MOM"]
        ],
    )
    
def factor_analysis(
    portfolio_returns: pd.Series,
    factor_data: pd.DataFrame,
) -> dict[str, dict]:
    """
    Run all supported factor models.

    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns.

    factor_data : pd.DataFrame
        Factor return data.

    Returns
    -------
    dict
        Dictionary containing all successfully computed factor models.
    """

    models: dict[str, dict] = {}

    columns = set(factor_data.columns)

    # --------------------------------------------------
    # CAPM
    # --------------------------------------------------

    if {"MKT_RF", "RF"}.issubset(columns):

        result = _capm(
            portfolio_returns,
            factor_data,
        )

        models["CAPM"] = {
            "Alpha": result.coefficients["const"],
            "Market Beta": result.coefficients["MKT_RF"],
            "R²": result.r_squared,
            "Adjusted R²": result.adjusted_r_squared,
            "Alpha p-value": result.p_values["const"],
            "Market p-value": result.p_values["MKT_RF"],
        }

    # --------------------------------------------------
    # Fama-French
    # --------------------------------------------------

    if {
        "MKT_RF",
        "SMB",
        "HML",
        "RF",
    }.issubset(columns):

        result = _fama_french(
            portfolio_returns,
            factor_data,
        )

        models["Fama-French 3 Factor"] = {
            "Alpha": result.coefficients["const"],
            "Market Beta": result.coefficients["MKT_RF"],
            "SMB": result.coefficients["SMB"],
            "HML": result.coefficients["HML"],
            "R²": result.r_squared,
            "Adjusted R²": result.adjusted_r_squared,
        }

    # --------------------------------------------------
    # Carhart
    # --------------------------------------------------

    if {
        "MKT_RF",
        "SMB",
        "HML",
        "MOM",
        "RF",
    }.issubset(columns):

        result = _carhart(
            portfolio_returns,
            factor_data,
        )

        models["Carhart 4 Factor"] = {
            "Alpha": result.coefficients["const"],
            "Market Beta": result.coefficients["MKT_RF"],
            "SMB": result.coefficients["SMB"],
            "HML": result.coefficients["HML"],
            "Momentum": result.coefficients["MOM"],
            "R²": result.r_squared,
            "Adjusted R²": result.adjusted_r_squared,
        }

    return models    
    
        