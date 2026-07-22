"use client";

import MetricCard from "./MetricCard";


interface MetricGridProps {
  metrics: Record<string, any>;
}



const allowedMetrics = [
  "Total Return",
  "Annualized Return",
  "CAGR",

  "Sharpe Ratio",
  "Sortino Ratio",

  "Volatility",
  "Annualized Volatility",

  "Maximum Drawdown",
  "Max Drawdown",
];



export default function MetricGrid({
  metrics,
}: MetricGridProps) {


  const flatMetrics: Record<string, string | number> = {};



  Object.values(metrics).forEach((section) => {


    if (
      typeof section === "object" &&
      section !== null &&
      !Array.isArray(section)
    ) {


      Object.entries(section).forEach(
        ([key, value]) => {


          if (
            allowedMetrics.includes(key) &&
            (
              typeof value === "number" ||
              typeof value === "string"
            )
          ) {

            flatMetrics[key] = value;

          }


        }
      );


    }


  });



  return (

    <div
      className="
        grid
        gap-6
        sm:grid-cols-2
        lg:grid-cols-3
      "
    >

      {
        Object.entries(flatMetrics).map(
          ([title, value]) => (

            <MetricCard
              key={title}
              title={title}
              value={value}
            />

          )
        )
      }


    </div>

  );

}