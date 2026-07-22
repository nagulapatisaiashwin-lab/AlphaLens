"use client";

export default function Topbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-background px-8">
      <div>
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <p className="text-sm text-muted-foreground">
          Professional Portfolio Analytics
        </p>
      </div>

      <div className="text-sm text-muted-foreground">
        AlphaLens v1
      </div>
    </header>
  );
}