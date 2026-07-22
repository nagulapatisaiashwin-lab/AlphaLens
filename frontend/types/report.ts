export interface AnalysisResponse {
  dataset_type: string;
  frequency: string;
  observations: number;

  metrics: Record<string, any>;

  charts: Record<string, any>;

  metadata: Record<string, any>;
}