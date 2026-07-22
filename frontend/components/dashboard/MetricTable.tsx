"use client";


interface MetricTableProps {

  title: string;

  data: Record<string, any>;

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


      <table className="w-full">

        <tbody>

          {Object.entries(data).map(
            ([key, value]) => (

              <tr
                key={key}
                className="border-b last:border-none"
              >

                <td className="p-3 text-sm text-muted-foreground">
                  {key}
                </td>


                <td className="p-3 text-right font-medium">

                  {
                    typeof value === "number"
                    ? value.toFixed(4)
                    : String(value)
                  }

                </td>

              </tr>

            )
          )}

        </tbody>

      </table>


    </div>

  );
}