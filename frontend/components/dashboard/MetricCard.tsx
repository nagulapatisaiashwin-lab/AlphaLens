import { TrendingDown, TrendingUp } from "lucide-react";

interface MetricCardProps {
  title: string;
  value: string;
  change?: string;
  positive?: boolean;
}

export default function MetricCard({
  title,
  value,
  change,
  positive,
}: MetricCardProps) {
  return (
    <div className="group rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
      <p className="text-sm font-medium uppercase tracking-wide text-muted-foreground">
        {title}
      </p>

      <h3 className="mt-4 text-3xl font-bold tracking-tight">
        {value}
      </h3>

      {change && (
        <div
          className={`mt-5 inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-medium ${
            positive
              ? "bg-green-500/10 text-green-600 dark:text-green-400"
              : "bg-red-500/10 text-red-600 dark:text-red-400"
          }`}
        >
          {positive ? (
            <TrendingUp className="h-4 w-4" />
          ) : (
            <TrendingDown className="h-4 w-4" />
          )}

          <span>{change}</span>
        </div>
      )}
    </div>
  );
}