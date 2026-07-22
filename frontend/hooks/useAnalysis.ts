import { useMutation } from "@tanstack/react-query";

import { uploadPortfolio } from "@/services/report";
import { AnalysisResponse } from "@/types/report";


interface UploadPayload {
  portfolioFile: File;
  factorFile?: File | null;
}


export function useAnalysis() {

  return useMutation<
    AnalysisResponse,
    Error,
    UploadPayload
  >({

    mutationFn: ({
      portfolioFile,
      factorFile,
    }) =>
      uploadPortfolio(
        portfolioFile,
        factorFile
      ),

  });

}