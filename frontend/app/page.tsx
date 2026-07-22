"use client";

import DashboardLayout from "@/components/layout/DashboardLayout";

import Header from "@/components/dashboard/Header";
import PortfolioSnapshot from "@/components/dashboard/PortfolioSnapshot";
import MetricGrid from "@/components/dashboard/MetricGrid";
import SectionCard from "@/components/dashboard/SectionCard";
import Definitions from "@/components/dashboard/Definitions";

import PlotlyChart from "@/components/charts/PlotlyChart";
import MetricTable from "@/components/tables/MetricTable";

import { useAnalysisStore } from "@/stores/analysisStore";


export default function Home() {


  const report = useAnalysisStore(
    (state) => state.report
  );


  return (

    <DashboardLayout>


      <Header />


      <main className="mx-auto max-w-7xl space-y-8 p-6">


        <PortfolioSnapshot />



        {/* Metrics */}

        {
          report?.metrics && (

            <MetricGrid
              metrics={report.metrics}
            />

          )
        }





        <SectionCard
          title="Equity Curve"
          subtitle="Portfolio growth over time"
        >

          {
            report?.charts?.equity ? (

              <PlotlyChart
                figure={report.charts.equity}
                height={450}
              />

            ) : (

              <Placeholder text="Upload portfolio data to view equity curve" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Benchmark Comparison"
          subtitle="Portfolio performance versus benchmark"
        >

          {
            report?.charts?.benchmark_comparison ? (

              <PlotlyChart

                figure={
                  report.charts.benchmark_comparison
                }

                height={400}

              />

            ) : (

              <Placeholder text="Benchmark chart will appear after analysis" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Monthly Returns Heatmap"
          subtitle="Monthly portfolio performance"
        >

          {
            report?.charts?.heatmap ? (

              <PlotlyChart

                figure={
                  report.charts.heatmap
                }

                height={350}

              />

            ) : (

              <Placeholder text="Heatmap unavailable" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Portfolio Drawdown"
          subtitle="Historical drawdown profile"
        >

          {
            report?.charts?.drawdown ? (

              <PlotlyChart

                figure={
                  report.charts.drawdown
                }

                height={350}

              />

            ) : (

              <Placeholder text="Drawdown unavailable" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Rolling Metrics"
          subtitle="Rolling Sharpe • Volatility • Returns"
        >

          {
            report?.charts?.rolling ? (

              <PlotlyChart

                figure={
                  report.charts.rolling
                }

                height={450}

              />

            ) : (

              <Placeholder text="Rolling metrics unavailable" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Return Distribution"
          subtitle="Distribution of portfolio returns"
        >

          {
            report?.charts?.distribution ? (

              <PlotlyChart

                figure={
                  report.charts.distribution
                }

                height={400}

              />

            ) : (

              <Placeholder text="Distribution unavailable" />

            )

          }


        </SectionCard>





        <SectionCard
          title="Factor Exposure"
          subtitle="CAPM / Fama-French / Carhart analysis"
        >

          {
            report?.charts?.factor_exposure ? (

              <PlotlyChart

                figure={
                  report.charts.factor_exposure
                }

                height={400}

              />

            ) : (

              <Placeholder text="Upload factor data for factor analysis" />

            )

          }


        </SectionCard>





        {
          report?.metrics && (

            <div className="grid gap-6 lg:grid-cols-2">


              {
                Object.entries(report.metrics)
                  .map(([section, data]) => (


                    typeof data === "object" &&
                    data !== null ? (


                      <MetricTable

                        key={section}

                        title={section}

                        data={data}

                      />


                    ) : null


                  ))

              }


            </div>


          )
        }





        <Definitions />



      </main>


    </DashboardLayout>

  );

}





function Placeholder({
  text,
}: {
  text: string;
}) {


  return (

    <div className="
      flex
      h-72
      items-center
      justify-center
      rounded-xl
      border
      border-dashed
      border-border
      text-muted-foreground
    ">

      {text}

    </div>

  );

}