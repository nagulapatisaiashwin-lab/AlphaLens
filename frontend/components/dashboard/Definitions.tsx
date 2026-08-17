"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";

import SectionCard from "./SectionCard";


const categories = {


  Performance: [

    {
      title: "Total Return",

      formula:
        "((Ending Value / Starting Value) - 1) × 100",

      explanation:
        "Measures the absolute growth of the portfolio during the investment period.",

      insight:
        "Positive values indicate portfolio growth.",

    },


    {
      title: "Annualized Return (CAGR)",

      formula:
        "(Ending Value / Starting Value)^(252/N) - 1",

      explanation:
        "Represents the compounded yearly return assuming 252 trading days.",

      insight:
        ">15% Strong | 5-15% Moderate | <5% Weak",

    },


    {
      title: "Sharpe Ratio",

      formula:
        "(Rp - Rf) / σp",

      explanation:
        "Measures excess return generated per unit of total risk.",

      insight:
        ">2 Excellent | >1.5 Good | >1 Acceptable | <1 Weak",

    },


    {
      title: "Sortino Ratio",

      formula:
        "(Rp - Rf) / Downside Deviation",

      explanation:
        "Risk-adjusted return measure that penalizes only negative volatility.",

      insight:
        ">2 Strong downside-adjusted performance",

    },

  ],




  Risk: [

    {
      title: "Volatility",

      formula:
        "σ(Returns) × √252",

      explanation:
        "Annualized standard deviation of portfolio returns.",

      insight:
        "<15% Low | 15-25% Moderate | >25% High",

    },


    {
      title: "Maximum Drawdown",

      formula:
        "Min((Portfolio Value - Peak Value) / Peak Value)",

      explanation:
        "Largest decline from a historical peak before recovery.",

      insight:
        "Lower drawdown indicates better capital preservation.",

    },


  ],




  Benchmark: [

    {
      title: "Alpha",

      formula:
        "Rp - [Rf + β(Rm-Rf)]",

      explanation:
        "Measures excess return generated beyond expected market return.",

      insight:
        "Positive alpha indicates benchmark outperformance.",

    },


    {
      title: "Beta",

      formula:
        "Cov(Rp,Rm) / Var(Rm)",

      explanation:
        "Measures portfolio sensitivity to market movements.",

      insight:
        "Beta >1 means higher market sensitivity.",

    },

  ],





  Distribution:[


    {
      title:"Skewness",

      formula:
        "E[(R-μ)³] / σ³",

      explanation:
        "Measures asymmetry of return distribution.",

      insight:
        "Positive skew indicates larger upside opportunities.",

    },


    {
      title:"Kurtosis",

      formula:
        "E[(R-μ)⁴] / σ⁴",

      explanation:
        "Measures probability of extreme return events.",

      insight:
        "Higher kurtosis indicates heavier tails.",

    },


  ],





  "Factor Models":[


    {
      title:"CAPM",

      formula:
        "Rp - Rf = α + β(Rm - Rf)",

      explanation:
        "Explains portfolio returns using market exposure.",

      insight:
        "Separates market-driven returns from alpha.",

    },



    {
      title:"Fama-French",

      formula:
        "Rp-Rf = α + βMKT + βSMB + βHML",

      explanation:
        "Multi-factor model explaining size and value effects.",

      insight:
        "Used for professional factor attribution.",

    },



    {
      title:"Carhart Four Factor",

      formula:
        "Fama-French + Momentum Factor",

      explanation:
        "Adds momentum exposure to factor analysis.",

      insight:
        "Commonly used in quantitative equity research.",

    },


  ],



};





export default function Definitions(){


const [open,setOpen] =
useState<string | null>(null);



return (

<SectionCard

title="Definitions & Formulae"

subtitle="Quantitative methodology, formulas and metric interpretation"

>


<div className="space-y-3">


{
Object.entries(categories).map(

([category,items])=>(


<div

key={category}

className="
rounded-xl
border
border-border/60
"

>


<button

className="
flex
w-full
items-center
justify-between
p-4
"

onClick={()=>setOpen(
open===category
?null
:category
)}

>


<span className="font-semibold">

{category}

</span>



<ChevronDown

className={`
transition-transform
${open===category
?"rotate-180"
:""
}`}

/>


</button>




{
open===category && (

<div

className="
space-y-3
border-t
p-4
"

>


{
items.map(item=>(


<div

key={item.title}

className="
rounded-lg
bg-muted/40
p-4
"

>


<h3 className="font-semibold">

{item.title}

</h3>



<div

className="
mt-3
rounded-md
bg-background
p-3
font-mono
text-sm
"

>

{item.formula}

</div>




<p

className="
mt-3
text-sm
text-muted-foreground
"

>

{item.explanation}

</p>




<div

className="
mt-3
rounded-md
border
p-3
text-sm
"

>

<b>
Interpretation:
</b>

{" "}

{item.insight}

</div>



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