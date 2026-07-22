"use client";


interface MetricTableProps {

  title: string;

  data: Record<string, any>;

}



function formatValue(value: any) {

  if (typeof value === "number") {

    if (Math.abs(value) < 1) {
      return `${(value * 100).toFixed(2)}%`;
    }

    return value.toFixed(4);

  }


  return String(value);

}



export default function MetricTable({

  title,

  data,

}: MetricTableProps) {


  return (

    <div className="overflow-hidden rounded-xl border border-border/60">


      <div className="border-b bg-muted/30 p-4">

        <h3 className="font-semibold">
          {title}
        </h3>

      </div>



      <div className="divide-y">


        {
          Object.entries(data).map(
            ([key, value]) => (


              typeof value === "object" &&
              value !== null ? (


                <div
                  key={key}
                  className="p-4"
                >


                  <h4 className="mb-3 font-medium">

                    {key}

                  </h4>



                  <table className="w-full">


                    <tbody>


                      {
                        Object.entries(value).map(
                          ([metric, metricValue]) => (

                            <tr
                              key={metric}
                              className="border-b last:border-none"
                            >

                              <td className="p-3 text-sm text-muted-foreground">

                                {metric}

                              </td>


                              <td className="p-3 text-right font-medium">

                                {
                                  formatValue(
                                    metricValue
                                  )
                                }

                              </td>


                            </tr>

                          )
                        )
                      }


                    </tbody>


                  </table>


                </div>


              ) : (


                <div
                  key={key}
                  className="flex justify-between p-3"
                >

                  <span className="text-sm text-muted-foreground">

                    {key}

                  </span>


                  <span className="font-medium">

                    {formatValue(value)}

                  </span>


                </div>


              )

            )
          )
        }


      </div>


    </div>

  );

}