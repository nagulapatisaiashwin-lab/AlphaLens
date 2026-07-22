import { ReactNode } from "react";

interface SectionCardProps {
  title: string;
  subtitle?: string;
  actions?: ReactNode;
  children: ReactNode;
}

export default function SectionCard({
  title,
  subtitle,
  actions,
  children,
}: SectionCardProps) {
  return (
    <section className="rounded-2xl border border-border bg-card shadow-sm">
      <div className="flex items-start justify-between border-b border-border px-6 py-5">
        <div>
          <h2 className="text-xl font-semibold tracking-tight">
            {title}
          </h2>

          {subtitle && (
            <p className="mt-1 text-sm text-muted-foreground">
              {subtitle}
            </p>
          )}
        </div>

        {actions && (
          <div className="flex items-center gap-2">
            {actions}
          </div>
        )}
      </div>

      <div className="p-6">
        {children}
      </div>
    </section>
  );
}