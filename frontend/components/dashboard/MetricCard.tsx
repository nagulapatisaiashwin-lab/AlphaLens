"use client";


interface MetricCardProps {

  title: string;

  value: unknown;

}




function getNormalizedValue(
  title: string,
  rawValue: number
) {

  const metric = title.toLowerCase();


  /*
    Backend stores returns/risk metrics
    as decimals.

    Example:
    0.2068 -> 20.68%
  */

  if (
    metric.includes("return") ||
    metric.includes("cagr") ||
    metric.includes("drawdown") ||
    metric.includes("volatility") ||
    metric.includes("vol") ||
    metric.includes("std")
  ) {

    if (Math.abs(rawValue) < 1) {

      return rawValue * 100;

    }

  }


  return rawValue;

}





function getMetricColor(
  title: string,
  rawValue: number
) {


  const metric = title.toLowerCase();


  const value = getNormalizedValue(
    title,
    rawValue
  );



  // Debug
  console.log(
    "METRIC COLOR",
    title,
    rawValue,
    value
  );





  /*
    Volatility
    <15%       Green
    15-25%     Yellow
    >25%       Red
  */

  if (
    metric.includes("volatility") ||
    metric.includes("vol") ||
    metric.includes("std")
  ) {


    if (value < 15)
      return "text-green-500";


    if (value <= 25)
      return "text-yellow-500";


    return "text-red-500";

  }





  /*
    Drawdown
    Always red
  */

  if (
    metric.includes("drawdown")
  ) {

    return "text-red-500";

  }





  /*
    Annual Return
  */

  if (
    metric.includes("annualized") ||
    metric.includes("cagr")
  ) {


    if (value > 15)
      return "text-green-500";


    if (value >= 5)
      return "text-yellow-500";


    return "text-red-500";

  }





  /*
    Total Return
  */

  if (
    metric.includes("total return")
  ) {


    return value > 0
      ? "text-green-500"
      : "text-red-500";

  }





  /*
    Sharpe
  */

  if (
    metric.includes("sharpe")
  ) {


    if (value > 1.5)
      return "text-green-500";


    if (value >= 1)
      return "text-yellow-500";


    return "text-red-500";

  }





  /*
    Sortino
  */

  if (
    metric.includes("sortino")
  ) {


    if (value > 2)
      return "text-green-500";


    if (value >= 1)
      return "text-yellow-500";


    return "text-red-500";

  }




  return "text-foreground";

}







function extractNumber(
  value: unknown
): number {


  if (
    typeof value === "number"
  ) {

    return value;

  }



  if (
    typeof value === "string"
  ) {

    return Number(
      value.replace("%", "")
    );

  }



  return 0;

}







function formatValue(
  title: string,
  value: unknown
) {


  const metric = title.toLowerCase();



  if (
    typeof value === "number"
  ) {


    if (

      metric.includes("return") ||
      metric.includes("cagr") ||
      metric.includes("drawdown") ||
      metric.includes("volatility") ||
      metric.includes("vol") ||
      metric.includes("std")

    ) {

      return `${(value * 100).toFixed(2)}%`;

    }



    return value.toFixed(2);

  }



  return String(value);

}







export default function MetricCard({

  title,

  value,

}: MetricCardProps) {



  const numericValue =
    extractNumber(value);



  return (

    <div
      className="
        rounded-xl
        border
        bg-card
        p-8
      "
    >


      <p
        className="
          text-sm
          uppercase
          tracking-wide
          text-muted-foreground
        "
      >

        {title}

      </p>




      <h2
        className={`
          mt-6
          text-4xl
          font-bold
          ${getMetricColor(
            title,
            numericValue
          )}
        `}
      >

        {formatValue(
          title,
          value
        )}

      </h2>


    </div>

  );

}