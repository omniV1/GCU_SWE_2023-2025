import { Outlet, useLocation } from "react-router";
import { useEffect } from "react";
import { Link } from "react-router";
import { Navbar } from "./Navbar";
import { Footer } from "./Footer";
import { MouseGlow } from "./MouseGlow";

function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  return null;
}

function AvailabilityBanner() {
  return (
    <div
      className="fixed top-12 left-0 right-0 z-40 border-b border-primary/20"
      style={{ backgroundColor: "rgba(0,255,212,0.04)", backdropFilter: "blur(8px)" }}
    >
      <div className="max-w-[1200px] mx-auto px-6 md:px-20 py-1.5 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <span
            className="w-1.5 h-1.5 rounded-full bg-primary"
            style={{
              boxShadow: "0 0 6px #00FFD4",
              animation: "data-pulse 2s infinite",
            }}
          />
          <span
            className="text-primary/80 tracking-widest"
            style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.58rem" }}
          >
            OPEN TO WORK · Full-time / Contract / Remote
          </span>
        </div>
        <Link
          to="/contact"
          className="text-primary/60 hover:text-primary transition-colors duration-150 hidden sm:block"
          style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.55rem" }}
        >
          [ GET IN TOUCH ]
        </Link>
      </div>
    </div>
  );
}

export function Layout() {
  return (
    <div className="min-h-screen flex flex-col" style={{ backgroundColor: "#0A0E12" }}>
      <ScrollToTop />
      <MouseGlow />
      <Navbar />
      <AvailabilityBanner />
      <main className="flex-1 pt-[4.5rem]">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}
