"use client";

import {
  LayoutDashboard,
  TrendingUp,
  ShieldAlert,
  Activity,
  FileText,
  Upload,
  Settings,
} from "lucide-react";

const navigation = [
  { name: "Dashboard", icon: LayoutDashboard },
  { name: "Performance", icon: TrendingUp },
  { name: "Risk", icon: ShieldAlert },
  { name: "Drawdown", icon: Activity },
  { name: "Reports", icon: FileText },
  { name: "Upload", icon: Upload },
];

export default function Sidebar() {
  return (
    <aside className="flex h-screen w-64 flex-col border-r bg-background">
      <div className="border-b p-6">
        <h1 className="text-2xl font-bold">AlphaLens</h1>
        <p className="text-sm text-muted-foreground">
          Quant Analytics Platform
        </p>
      </div>

      <nav className="flex-1 space-y-2 p-4">
        {navigation.map((item) => {
          const Icon = item.icon;

          return (
            <button
              key={item.name}
              className="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-left transition-colors hover:bg-accent"
            >
              <Icon className="h-5 w-5" />
              <span>{item.name}</span>
            </button>
          );
        })}
      </nav>

      <div className="border-t p-4">
        <button className="flex w-full items-center gap-3 rounded-lg px-3 py-2 transition-colors hover:bg-accent">
          <Settings className="h-5 w-5" />
          <span>Settings</span>
        </button>
      </div>
    </aside>
  );
}