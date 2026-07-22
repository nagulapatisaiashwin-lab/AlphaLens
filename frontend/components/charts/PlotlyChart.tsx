"use client";

import dynamic from "next/dynamic";

import type { Layout, Data } from "plotly.js";


const Plot = dynamic(
  () => import("react-plotly.js"),
  {
    ssr: false,
  }
);



interface PlotlyChartProps {

  figure: {

    data: Data[];

    layout?: Partial<Layout>;

  };


  height?: number;

}



export default function PlotlyChart({

  figure,

  height = 450,

}: PlotlyChartProps) {


  return (

    <div className="w-full overflow-hidden rounded-xl">


      <Plot


        data={figure.data}



        layout={{

          autosize: true,


          height,



          // Remove internal Plotly title
          // SectionCard handles titles

          title: {
            text: "",
          },


          paper_bgcolor: "transparent",

          plot_bgcolor: "transparent",



          margin: {

            l: 60,

            r: 30,

            t: 25,

            b: 55,

          },



          legend: {

            orientation: "h",

            yanchor: "bottom",

            y: 1.02,

            xanchor: "right",

            x: 1,

          },



          hoverlabel: {

            bgcolor: "#111827",

          },



          ...figure.layout,


        }}



        config={{

          responsive: true,

          displaylogo: false,



          modeBarButtonsToRemove: [

            "lasso2d",

            "select2d",

          ],

        }}



        style={{

          width: "100%",

          height: `${height}px`,

        }}



        useResizeHandler={true}


      />


    </div>

  );

}