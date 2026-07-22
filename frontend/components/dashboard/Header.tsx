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


    if (file) {

      setPortfolioFile(file);

    }

  }



  function handleFactorChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {

    const file =
      event.target.files?.[0];


    if (file) {

      setFactorFile(file);

    }

  }



  function handleAnalyze() {


    if (!portfolioFile) {

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

        onSuccess: (data) => {

          setReport(data);

        },

        onError: (error) => {

          console.error(
            error
          );

          alert(
            "Analysis failed. Check backend logs."
          );

        },

      }

    );

  }



  return (

    <header className="sticky top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-xl">

      <div className="flex items-center justify-between py-6">


        {/* Branding */}

        <div className="flex items-center gap-4">

          <div className="flex h-12 w-12 items-center justify-center rounded-xl border border-border bg-card shadow-sm">

            <BarChart3 className="h-6 w-6" />

          </div>


          <div>

            <h1 className="text-3xl font-bold tracking-tight">
              AlphaLens
            </h1>


            <p className="mt-1 text-sm text-muted-foreground">
              Professional Quantitative Portfolio Analytics Platform
            </p>

          </div>

        </div>




        {/* Upload Actions */}

        <div className="flex items-center gap-3">


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
          >

            <Upload className="mr-2 h-4 w-4" />

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
          >

            <Upload className="mr-2 h-4 w-4" />

            {
              factorFile
                ? factorFile.name
                : "Upload Factor (Optional)"
            }

          </Button>




          <Button
            size="lg"
            onClick={handleAnalyze}
            disabled={analysis.isPending}
          >

            <FileText className="mr-2 h-4 w-4" />

            {
              analysis.isPending
                ? "Analyzing..."
                : "Generate Analysis"
            }

          </Button>


        </div>

      </div>

    </header>

  );

}