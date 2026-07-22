"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";

import SectionCard from "./SectionCard";


const categories = {

  Performance: [

    {
      title: "Total Return",
      formula:
        "((Ending Value - Starting Value) / Starting Value)",
      explanation:
        "Measures absolute portfolio growth over the investment period.",
    },

    {
      title: "CAGR",
      formula:
        "(Ending Value / Starting Value)^(1/Years)-1",
      explanation:
        "Annualized growth rate of the portfolio.",
    },

    {
      title: "Sharpe Ratio",
      formula:
        "(Rp - Rf) / σp",
      explanation:
        "Return generated per unit of total risk.",
    },

  ],



  Risk: [

    {
      title: "Volatility",
      formula:
        "Standard Deviation(Returns) × √252",
      explanation:
        "Measures portfolio return fluctuation.",
    },

    {
      title: "Maximum Drawdown",
      formula:
        "Largest peak-to-trough decline",
      explanation:
        "Measures worst historical loss.",
    },

    {
      title: "Sortino Ratio",
      formula:
        "(Rp-Rf)/Downside Deviation",
      explanation:
        "Risk-adjusted return considering only downside volatility.",
    },

  ],



  Benchmark: [

    {
      title:"Alpha",

      formula:
        "Portfolio Return - Expected Return",

      explanation:
        "Measures excess performance beyond benchmark expectation.",
    },


    {
      title:"Beta",

      formula:
        "Cov(Rp,Rm)/Var(Rm)",

      explanation:
        "Measures sensitivity to market movements.",
    },

  ],



  Distribution:[

    {
      title:"Skewness",

      formula:
        "E[(R-μ)^3]/σ³",

      explanation:
        "Measures return asymmetry.",
    },


    {
      title:"Kurtosis",

      formula:
        "E[(R-μ)^4]/σ⁴",

      explanation:
        "Measures extreme tail events.",
    },

  ],



  "Factor Models":[

    {
      title:"CAPM",

      formula:
        "Rp-Rf = α + β(Rm-Rf)",

      explanation:
        "Explains returns using market exposure.",
    },


    {
      title:"Fama-French",

      formula:
        "Market + Size + Value + Profitability + Investment",

      explanation:
        "Multi-factor attribution model.",
    },


    {
      title:"Carhart Model",

      formula:
        "Fama-French + Momentum",

      explanation:
        "Adds momentum as a return factor.",
    },

  ],


};



export default function Definitions(){


const [open,setOpen] = useState<string | null>(null);



return (

<SectionCard

title="Definitions & Formulae"

subtitle="Quantitative concepts and mathematical interpretation"

>


<div className="space-y-3">


{
Object.entries(categories).map(
([category,items])=>(


<div

key={category}

className="rounded-xl border border-border/60"

>


<button

className="flex w-full items-center justify-between p-4"

onClick={()=>setOpen(
open===category ? null : category
)}

>


<span className="font-semibold">

{category}

</span>


<ChevronDown

className={`transition-transform ${
open===category
?"rotate-180"
:""
}`}

/>


</button>



{
open===category && (

<div className="space-y-3 border-t p-4">


{
items.map(item=>(


<div

key={item.title}

className="rounded-lg bg-muted/40 p-4"

>


<h3 className="font-semibold">

{item.title}

</h3>


<p className="mt-2 font-mono text-sm">

{item.formula}

</p>


<p className="mt-2 text-sm text-muted-foreground">

{item.explanation}

</p>


</div>


))

}


</div>

)

}


</div>


)

)

}


</div>


</SectionCard>


)

}