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
  {
    name: "Dashboard",
    icon: LayoutDashboard,
    href: "#dashboard",
  },
  {
    name: "Performance",
    icon: TrendingUp,
    href: "#performance",
  },
  {
    name: "Risk",
    icon: ShieldAlert,
    href: "#risk",
  },
  {
    name: "Drawdown",
    icon: Activity,
    href: "#drawdown",
  },
  {
    name: "Reports",
    icon: FileText,
    href: "#reports",
  },
  {
    name: "Upload",
    icon: Upload,
    href: "#upload",
  },
];



export default function Sidebar() {


  return (

    <aside
      className="
        flex
        min-h-screen
        w-64
        flex-col
        border-r
        bg-background
      "
    >


      {/* Brand */}

      <div className="border-b p-6">


        <h1
          className="
            text-2xl
            font-bold
            tracking-tight
          "
        >
          AlphaLens
        </h1>



        <p
          className="
            mt-1
            text-sm
            text-muted-foreground
          "
        >
          Quant Analytics Platform
        </p>


      </div>





      {/* Navigation */}

      <nav
        className="
          flex-1
          space-y-2
          p-4
        "
      >


        {
          navigation.map((item)=>{


            const Icon = item.icon;


            return (

              <a
                key={item.name}
                href={item.href}

                className="
                  flex
                  w-full
                  items-center
                  gap-3
                  rounded-lg
                  px-3
                  py-2
                  text-left
                  transition-colors
                  hover:bg-accent
                "
              >

                <Icon
                  className="h-5 w-5"
                />


                <span>
                  {item.name}
                </span>


              </a>

            );


          })
        }


      </nav>





      {/* Bottom */}

      <div
        className="
          border-t
          p-4
        "
      >


        <a
          href="#settings"

          className="
            flex
            w-full
            items-center
            gap-3
            rounded-lg
            px-3
            py-2
            hover:bg-accent
          "
        >

          <Settings
            className="h-5 w-5"
          />

          <span>
            Settings
          </span>


        </a>





        <div
          className="
            mt-5
            border-t
            pt-4
          "
        >


          <p
            className="
              text-xs
              text-muted-foreground
            "
          >
            Created by
          </p>



          <p
            className="
              mt-1
              text-sm
              font-semibold
            "
          >
            Sai Ashwin Nagulapati
          </p>



          <p
            className="
              text-xs
              text-muted-foreground
            "
          >
            IIT Jodhpur
          </p>


        </div>


      </div>


    </aside>

  );

}