"use client";

import MetricCard from "./MetricCard";

import { useAnalysisStore } from "@/stores/analysisStore";

export default function MetricGrid() {
  const report = useAnalysisStore(
    (state) => state.report
  );

  if (!report) {
    return (
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <MetricCard
          title="Total Return"
          value="--"
        />

        <MetricCard
          title="Annualized Return"
          value="--"
        />

        <MetricCard
          title="Sharpe Ratio"
          value="--"
        />

        <MetricCard
          title="Volatility"
          value="--"
        />

        <MetricCard
          title="Maximum Drawdown"
          value="--"
        />

        <MetricCard
          title="Sortino Ratio"
          value="--"
        />
      </div>
    );
  }


  const performance =
    report.metrics["Performance"] ?? {};

  const risk =
    report.metrics["Risk"] ?? {};


  const formatPercentage = (
    value: number | undefined
  ) => {
    if (value === undefined) return "--";

    return `${(value * 100).toFixed(2)}%`;
  };


  const formatNumber = (
    value: number | undefined
  ) => {
    if (value === undefined) return "--";

    return value.toFixed(2);
  };


  const metrics = [
    {
      title: "Total Return",
      value: formatPercentage(
        performance["Total Return"]
      ),
      positive:
        (performance["Total Return"] ?? 0) > 0,
    },

    {
      title: "Annualized Return",
      value: formatPercentage(
        performance["Annualized Return"]
      ),
      positive:
        (performance["Annualized Return"] ?? 0) > 0,
    },

    {
      title: "Sharpe Ratio",
      value: formatNumber(
        performance["Sharpe Ratio"]
      ),
      positive:
        (performance["Sharpe Ratio"] ?? 0) > 1,
    },

    {
      title: "Volatility",
      value: formatPercentage(
        risk["Annualized Volatility"]
      ),
      positive: false,
    },

    {
      title: "Maximum Drawdown",
      value: formatPercentage(
        risk["Maximum Drawdown"]
      ),
      positive: false,
    },

    {
      title: "Sortino Ratio",
      value: formatNumber(
        risk["Sortino Ratio"]
      ),
      positive:
        (risk["Sortino Ratio"] ?? 0) > 1,
    },
  ];


  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {metrics.map((metric) => (
        <MetricCard
          key={metric.title}
          title={metric.title}
          value={metric.value}
          positive={metric.positive}
        />
      ))}
    </div>
  );
}