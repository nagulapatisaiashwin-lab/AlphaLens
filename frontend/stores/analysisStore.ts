"use client";

import { create } from "zustand";

import { AnalysisResponse } from "@/types/report";


interface AnalysisStore {

  portfolioFile: File | null;

  factorFile: File | null;

  report: AnalysisResponse | null;


  setPortfolioFile: (
    file: File
  ) => void;


  setFactorFile: (
    file: File | null
  ) => void;


  setReport: (
    report: AnalysisResponse
  ) => void;


  clearReport: () => void;

}



export const useAnalysisStore =
  create<AnalysisStore>((set) => ({

    portfolioFile: null,

    factorFile: null,

    report: null,


    setPortfolioFile: (file) =>
      set({
        portfolioFile: file,
      }),


    setFactorFile: (file) =>
      set({
        factorFile: file,
      }),


    setReport: (report) =>
      set({
        report,
      }),


    clearReport: () =>
      set({
        report: null,
      }),

  }));