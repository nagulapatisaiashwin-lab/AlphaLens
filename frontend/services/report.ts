import { api } from "./api";
import { AnalysisResponse } from "@/types/report";


export async function uploadPortfolio(
  portfolioFile: File,
  factorFile?: File | null
): Promise<AnalysisResponse> {


  const formData = new FormData();


  formData.append(
    "portfolio_file",
    portfolioFile
  );


  if (factorFile) {

    formData.append(
      "factor_file",
      factorFile
    );

  }


  const response =
    await api.post<AnalysisResponse>(
      "/api/analyze",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },

        timeout: 120000,
      }
    );


  return response.data;
}
