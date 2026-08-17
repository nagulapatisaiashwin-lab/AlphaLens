"use client";

import { useRef } from "react";

import { Button } from "@/components/ui/button";

import {
  BarChart3,
  FileText,
  Upload,
} from "lucide-react";

import { useAnalysis } from "@/hooks/useAnalysis";

import { useAnalysisStore } from "@/stores/analysisStore";



export default function Header() {


  const portfolioInputRef =
    useRef<HTMLInputElement>(null);


  const factorInputRef =
    useRef<HTMLInputElement>(null);



  const analysis = useAnalysis();



  const {
    portfolioFile,
    factorFile,
    setPortfolioFile,
    setFactorFile,
    setReport,
  } = useAnalysisStore();





  function handlePortfolioClick() {

    portfolioInputRef.current?.click();

  }



  function handleFactorClick() {

    factorInputRef.current?.click();

  }





  function handlePortfolioChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {

    const file =
      event.target.files?.[0];


    if(file){

      setPortfolioFile(file);

    }

  }





  function handleFactorChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {


    const file =
      event.target.files?.[0];


    if(file){

      setFactorFile(file);

    }

  }





  function handleAnalyze(){


    if(!portfolioFile){

      alert(
        "Please upload a portfolio file first."
      );

      return;

    }



    analysis.mutate(

      {
        portfolioFile,
        factorFile,
      },


      {

        onSuccess:(data)=>{

          setReport(data);

        },


        onError:(error)=>{

          console.error(error);

          alert(
            "Analysis failed. Check backend logs."
          );

        },

      }

    );

  }





  return (

    <header
      className="
        border-b
        border-border/60
        bg-background/80
        backdrop-blur-xl
      "
    >


      <div
        className="
          flex
          items-center
          justify-between
          px-6
          py-4
        "
      >





        {/* Branding */}


        <div
          className="
            flex
            items-center
            gap-4
          "
        >


          <div
            className="
              flex
              h-10
              w-10
              items-center
              justify-center
              rounded-xl
              border
              bg-card
            "
          >

            <BarChart3
              className="h-5 w-5"
            />

          </div>





          <div>


            <h1
              className="
                text-3xl
                font-bold
                tracking-tight
              "
            >

              AlphaLens

            </h1>



            <p
              className="
                text-sm
                text-muted-foreground
              "
            >

              Professional Quantitative Portfolio Analytics Platform

            </p>



            <p
              className="
                mt-1
                text-xs
                font-medium
                text-muted-foreground
              "
            >

              Created by Sai Ashwin Nagulapati • IIT Jodhpur

            </p>


          </div>


        </div>







        {/* Upload Actions */}


        <div
          className="
            flex
            flex-col
            items-end
            gap-3
          "
        >

          <div
            className="
              text-xs
              text-muted-foreground
              text-right
              mb-1
            "
          >
            <div className="font-medium">Accepted Formats:</div>
            <div>CSV (.csv), Excel (.xlsx, .xls)</div>
            <div className="mt-1 font-medium">Required Columns:</div>
            <div>Date, Portfolio Value (required), Benchmark Value (optional)</div>
          </div>

          <div
            className="
              flex
              items-center
              gap-3
            "
          >



          <input

            ref={portfolioInputRef}

            type="file"

            accept=".csv,.xlsx,.xls"

            hidden

            onChange={handlePortfolioChange}

          />



          <input

            ref={factorInputRef}

            type="file"

            accept=".csv,.xlsx,.xls"

            hidden

            onChange={handleFactorChange}

          />






          <Button

            variant="outline"

            size="lg"

            onClick={handlePortfolioClick}

            title="Accepts CSV (.csv) and Excel (.xlsx, .xls) files with columns: Date, Portfolio Value (required), Benchmark Value (optional)"

          >

            <Upload
              className="mr-2 h-4 w-4"
            />


            {
              portfolioFile
              ? portfolioFile.name
              : "Upload Portfolio"
            }


          </Button>






          <Button

            variant="outline"

            size="lg"

            onClick={handleFactorClick}

            title="Accepts CSV (.csv) and Excel (.xlsx, .xls) files with factor data"

          >

            <Upload
              className="mr-2 h-4 w-4"
            />

            {
              factorFile
              ? factorFile.name
              : "Upload Factor"
            }


          </Button>






          <Button

            size="lg"

            onClick={handleAnalyze}

            disabled={analysis.isPending}

          >


            <FileText
              className="mr-2 h-4 w-4"
            />


            {
              analysis.isPending
              ? "Analyzing..."
              : "Generate Analysis"
            }


          </Button>




          </div>

        </div>



      </div>


    </header>

  );

}