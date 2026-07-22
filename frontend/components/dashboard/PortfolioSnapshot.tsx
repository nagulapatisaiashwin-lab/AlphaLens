"use client";

import SectionCard from "./SectionCard";

import { useAnalysisStore } from "@/stores/analysisStore";

export default function PortfolioSnapshot() {
  const report = useAnalysisStore(
    (state) => state.report
  );

  if (!report) {
    return (
      <SectionCard
        title="Portfolio Snapshot"
        subtitle="Overview of the uploaded portfolio and analysis configuration."
      >
        <div className="rounded-xl border border-dashed border-border p-6 text-center">
          <p className="text-muted-foreground">
            Upload a portfolio dataset to generate analysis.
          </p>
        </div>
      </SectionCard>
    );
  }

  const items = [
    {
      label: "Dataset Type",
      value: report.dataset_type,
    },
    {
      label: "Frequency",
      value: report.frequency,
    },
    {
      label: "Observations",
      value: report.observations.toLocaleString(),
    },
    {
      label: "Charts Generated",
      value: Object.keys(report.charts).length.toString(),
    },
    {
      label: "Analysis Status",
      value: "Completed",
    },
    {
      label: "Metadata",
      value:
        Object.keys(report.metadata).length > 0
          ? "Available"
          : "None",
    },
  ];

  return (
    <SectionCard
      title="Portfolio Snapshot"
      subtitle="Overview of the uploaded portfolio and analysis configuration."
    >
      <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {items.map((item) => (
          <div
            key={item.label}
            className="rounded-xl border border-border/60 bg-muted/30 p-5 transition-all duration-300 hover:-translate-y-1 hover:bg-muted/50"
          >
            <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              {item.label}
            </p>

            <p className="mt-2 text-lg font-semibold tracking-tight">
              {item.value}
            </p>
          </div>
        ))}
      </div>
    </SectionCard>
  );
}