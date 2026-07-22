"use client";

import SectionCard from "./SectionCard";


const definitions = [

  // -------------------------
  // Performance
  // -------------------------

  {
    category: "Performance",

    title: "Total Return",

    formula:
      "Total Return = (Ending Value - Starting Value) / Starting Value",

    explanation:
      "Measures the absolute growth of the portfolio over the entire investment period.",

    interpretation:
      "Higher return indicates stronger portfolio growth, but should always be evaluated with risk metrics.",
  },


  {
    category: "Performance",

    title: "Annualized Return (CAGR)",

    formula:
      "CAGR = (Ending Value / Starting Value)^(1/Years) - 1",

    explanation:
      "Converts total return into an equivalent yearly growth rate.",

    interpretation:
      "Useful for comparing strategies with different investment horizons.",
  },


  {
    category: "Performance",

    title: "Sharpe Ratio",

    formula:
      "Sharpe = (Rp - Rf) / σp",

    explanation:
      "Measures excess return generated per unit of total portfolio volatility.",

    interpretation:
      "Higher Sharpe indicates better risk-adjusted performance.",
  },



  // -------------------------
  // Risk
  // -------------------------


  {
    category: "Risk",

    title: "Volatility",

    formula:
      "σ = Standard Deviation of Returns × √252",

    explanation:
      "Measures the variability of portfolio returns.",

    interpretation:
      "Higher volatility means larger fluctuations and higher uncertainty.",
  },


  {
    category: "Risk",

    title: "Maximum Drawdown",

    formula:
      "MDD = Maximum decline from historical peak",

    explanation:
      "Measures the largest loss experienced from a portfolio peak to a subsequent trough.",

    interpretation:
      "Lower drawdown indicates better downside protection.",
  },


  {
    category: "Risk",

    title: "Sortino Ratio",

    formula:
      "Sortino = (Rp - Rf) / Downside Deviation",

    explanation:
      "Similar to Sharpe ratio but considers only negative volatility.",

    interpretation:
      "Useful for strategies where downside risk matters more than total volatility.",
  },


  {
    category: "Risk",

    title: "Value at Risk (VaR)",

    formula:
      "VaRα = Loss threshold at confidence level α",

    explanation:
      "Estimates the maximum expected loss under normal market conditions.",

    interpretation:
      "Example: 95% VaR represents a loss level expected not to be exceeded 95% of the time.",
  },


  {
    category: "Risk",

    title: "Conditional VaR (CVaR)",

    formula:
      "CVaR = Expected loss beyond VaR threshold",

    explanation:
      "Measures the average loss during the worst-case scenarios beyond VaR.",

    interpretation:
      "More sensitive to extreme downside events than VaR.",
  },



  // -------------------------
  // Benchmark
  // -------------------------


  {
    category: "Benchmark",

    title: "Beta",

    formula:
      "β = Cov(Rp,Rm) / Var(Rm)",

    explanation:
      "Measures portfolio sensitivity relative to benchmark movements.",

    interpretation:
      "Beta > 1 means higher market sensitivity; Beta < 1 means lower sensitivity.",
  },


  {
    category: "Benchmark",

    title: "Alpha",

    formula:
      "Alpha = Portfolio Return - Expected Market Return",

    explanation:
      "Measures excess return generated beyond benchmark expectations.",

    interpretation:
      "Positive alpha indicates value added by the strategy.",
  },


  {
    category: "Benchmark",

    title: "Information Ratio",

    formula:
      "IR = Active Return / Tracking Error",

    explanation:
      "Measures excess benchmark return relative to active risk.",

    interpretation:
      "Higher values indicate more consistent benchmark outperformance.",
  },



  // -------------------------
  // Distribution
  // -------------------------


  {
    category: "Distribution",

    title: "Skewness",

    formula:
      "Skew = E[(R-μ)^3] / σ³",

    explanation:
      "Measures asymmetry of return distribution.",

    interpretation:
      "Positive skew indicates greater probability of large positive returns.",
  },


  {
    category: "Distribution",

    title: "Kurtosis",

    formula:
      "Kurtosis = E[(R-μ)^4] / σ⁴",

    explanation:
      "Measures tail heaviness of return distribution.",

    interpretation:
      "Higher kurtosis indicates greater probability of extreme events.",
  },



  // -------------------------
  // Factor Models
  // -------------------------


  {
    category: "Factor Models",

    title: "CAPM",

    formula:
      "Rp - Rf = α + β(Rm - Rf)",

    explanation:
      "Models portfolio return using market risk exposure.",

    interpretation:
      "Separates market-driven returns from manager skill.",
  },


  {
    category: "Factor Models",

    title: "Fama-French Three Factor Model",

    formula:
      "Rp-Rf = α + βMKT(MKT-RF)+βSMB(SMB)+βHML(HML)",

    explanation:
      "Extends CAPM using size and value factors.",

    interpretation:
      "Identifies whether returns are explained by market, size, or value exposure.",
  },


  {
    category: "Factor Models",

    title: "Fama-French Five Factor Model",

    formula:
      "MKT + SMB + HML + RMW + CMA",

    explanation:
      "Adds profitability and investment factors.",

    interpretation:
      "Provides deeper attribution of portfolio performance.",
  },


  {
    category: "Factor Models",

    title: "Carhart Four Factor Model",

    formula:
      "FF3 + Momentum Factor",

    explanation:
      "Adds momentum as an additional return driver.",

    interpretation:
      "Useful for analysing momentum-based strategies.",
  },

];



export default function Definitions() {


  return (

    <SectionCard
      title="Definitions & Formulae"
      subtitle="Quantitative concepts, mathematical formulas and interpretation"
    >


      <div className="space-y-6">


        {definitions.map((item) => (

          <div

            key={item.title}

            className="rounded-xl border border-border/60 p-5"

          >


            <div className="mb-2 text-xs uppercase tracking-wide text-muted-foreground">

              {item.category}

            </div>


            <h3 className="text-lg font-semibold">

              {item.title}

            </h3>


            <div className="mt-3 rounded-lg bg-muted p-4 font-mono text-sm">

              {item.formula}

            </div>


            <p className="mt-3 text-sm text-muted-foreground">

              <strong>
                Explanation:
              </strong>{" "}

              {item.explanation}

            </p>


            <p className="mt-2 text-sm text-muted-foreground">

              <strong>
                Interpretation:
              </strong>{" "}

              {item.interpretation}

            </p>


          </div>


        ))}


      </div>


    </SectionCard>

  );

}