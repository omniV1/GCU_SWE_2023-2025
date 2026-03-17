import { useState } from "react";
import { ChevronDown } from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { FadeIn } from "./FadeIn";

const timeline = [
  { year: "2026", event: "B.S. Software Development — Grand Canyon University (Spring)" },
  { year: "2026", event: "LUNARA — senior capstone, deployed to production at lunaracare.org" },
  { year: "2026", event: "Built Multi-Agent Code Quality System" },
  { year: "2025", event: "CineScope — movie review platform, primary developer on 4-person Agile team" },
  { year: "2025", event: "Built AGMS — enterprise airport operations platform" },
  { year: "2025", event: "Aircraft Fleet Manager — React + ASP.NET Core maintenance tracking system" },
  { year: "2023", event: "Began GCU Software Engineering program" },
  { year: "2022", event: "Separated from USAF — Tactical Aircraft Maintenance (5th Gen), F-22 Raptor" },
  { year: "2017", event: "Enlisted — United States Air Force \u00b7 5 Years of Service" },
];

const interests = [
  "Long-distance backpacking",
  "National parks",
  "Retro computing",
  "Aviation history",
  "Open source tools",
  "Competitive programming",
];

export function AboutPage() {
  const [qualificationsOpen, setQualificationsOpen] = useState(false);

  return (
    <div>
      {/* Hero */}
      <section className="relative py-20 px-6 md:px-20 border-b border-border overflow-hidden">
        {/* Grid overlay */}
        <div
          className="absolute inset-0 opacity-[0.04]"
          style={{
            backgroundImage: `repeating-linear-gradient(0deg, transparent, transparent 40px, rgba(0,255,212,0.2) 40px, rgba(0,255,212,0.2) 41px),
              repeating-linear-gradient(90deg, transparent, transparent 40px, rgba(0,255,212,0.2) 40px, rgba(0,255,212,0.2) 41px)`,
          }}
        />
        {/* Noise */}
        <div
          className="absolute inset-0 opacity-[0.06]"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E")`,
          }}
        />
        {/* Color accent */}
        <div
          className="absolute inset-0"
          style={{ background: "radial-gradient(ellipse at 20% 50%, rgba(0,255,212,0.04) 0%, transparent 50%)" }}
        />

        <div className="relative max-w-[1200px] mx-auto">
          <FadeIn>
            <span
              className="text-primary"
              style={{
                fontFamily: "'IBM Plex Mono', monospace",
                fontSize: "0.75rem",
                textShadow: "0 0 8px rgba(0,255,212,0.4)",
              }}
            >
              // ABOUT
            </span>
            <h1
              className="mt-3"
              style={{
                fontFamily: "'Bebas Neue', sans-serif",
                fontSize: "clamp(2.5rem, 6vw, 4.5rem)",
                letterSpacing: "0.04em",
                color: "#D4DEE8",
              }}
            >
              ABOUT THE ENGINEER
            </h1>
          </FadeIn>
        </div>
      </section>

      {/* Two-column content */}
      <section className="py-16 px-6 md:px-20">
        <div className="max-w-[1200px] mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20">
          {/* Left — Bio */}
          <FadeIn>
            <div>
              <h2
                className="text-primary tracking-widest mb-6 pb-2 border-b border-border"
                style={{
                  fontSize: "0.6rem",
                  fontFamily: "'Space Grotesk', sans-serif",
                  letterSpacing: "0.15em",
                  textShadow: "0 0 6px rgba(0,255,212,0.3)",
                }}
              >
                BACKGROUND
              </h2>

              <div className="space-y-4 text-foreground/70" style={{ fontSize: "0.82rem", lineHeight: 1.85 }}>
                <p>
                  Software engineer and USAF veteran. Served in F-22 Tactical Aircraft Maintenance
                  (2A3X7) before transitioning to civilian software engineering. B.S. in
                  Software Development, Grand Canyon University, Class of 2026.
                </p>
                <p>
                  I bring operational discipline from the flight line to the codebase — I build systems
                  that are reliable under pressure, documented thoroughly, and designed to be handed off.
                </p>
              </div>

              <div className="mt-10">
                <h2
                  className="text-primary tracking-widest mb-4 pb-2 border-b border-border"
                  style={{
                    fontSize: "0.6rem",
                    fontFamily: "'Space Grotesk', sans-serif",
                    letterSpacing: "0.15em",
                    textShadow: "0 0 6px rgba(0,255,212,0.3)",
                  }}
                >
                  INTERESTS
                </h2>
                <p className="text-foreground/50" style={{ fontSize: "0.78rem", lineHeight: 1.8 }}>
                  {interests.join("  //  ")}
                </p>
              </div>
            </div>
          </FadeIn>

          {/* Right — Timeline */}
          <FadeIn delay={0.15}>
            <div>
              <h2
                className="text-primary tracking-widest mb-6 pb-2 border-b border-border"
                style={{
                  fontSize: "0.6rem",
                  fontFamily: "'Space Grotesk', sans-serif",
                  letterSpacing: "0.15em",
                  textShadow: "0 0 6px rgba(0,255,212,0.3)",
                }}
              >
                TIMELINE
              </h2>

              <div className="space-y-0">
                {timeline.map((entry, i) => (
                  <div
                    key={i}
                    className="flex gap-5 py-3 border-b border-border/20 group hover:bg-primary/[0.02] transition-colors duration-150 px-2 -mx-2"
                  >
                    <span
                      className="text-primary shrink-0 pt-0.5"
                      style={{
                        fontFamily: "'IBM Plex Mono', monospace",
                        fontSize: "0.7rem",
                        minWidth: "3rem",
                        textShadow: "0 0 6px rgba(0,255,212,0.3)",
                      }}
                    >
                      [{entry.year}]
                    </span>
                    <span
                      className="text-foreground/60 whitespace-pre-line group-hover:text-foreground/80 transition-colors duration-150"
                      style={{ fontSize: "0.78rem", lineHeight: 1.6 }}
                    >
                      {entry.event}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </FadeIn>
        </div>
      </section>

      {/* Additional Qualifications */}
      <section className="px-6 md:px-20 pb-16">
        <div className="max-w-[1200px] mx-auto">
          <FadeIn>
            <button
              onClick={() => setQualificationsOpen(!qualificationsOpen)}
              className="w-full flex items-center justify-between border border-border p-4 hover:border-primary/30 hover:shadow-[0_0_15px_rgba(0,255,212,0.05)] transition-all duration-150"
            >
              <span
                className="text-muted-foreground tracking-widest"
                style={{ fontSize: "0.65rem", fontFamily: "'Space Grotesk', sans-serif", letterSpacing: "0.12em" }}
              >
                ADDITIONAL QUALIFICATIONS
              </span>
              <ChevronDown
                size={14}
                className={`text-muted-foreground transition-transform duration-150 ${qualificationsOpen ? "rotate-180" : ""}`}
              />
            </button>

            <AnimatePresence>
              {qualificationsOpen && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.15, ease: "easeOut" }}
                  className="overflow-hidden border-x border-b border-border"
                >
                  <div className="p-5 space-y-4">
                    <div>
                      <div className="flex items-center gap-3 mb-2">
                        <span
                          className="w-1.5 h-1.5 rounded-full bg-primary shrink-0"
                          style={{ boxShadow: "0 0 4px #00FFD4, 0 0 10px rgba(0,255,212,0.3)" }}
                        />
                        <span className="text-foreground/80" style={{ fontSize: "0.82rem", fontWeight: 500 }}>
                          Eagle Scout — Boy Scouts of America
                        </span>
                      </div>
                      <p className="text-foreground/40 ml-[1.125rem] pl-3" style={{ fontSize: "0.75rem", lineHeight: 1.7 }}>
                        Highest rank in scouting. Requires demonstrated leadership, a community
                        service project planned and executed independently, and sustained commitment
                        over multiple years.
                      </p>
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </FadeIn>
        </div>
      </section>
    </div>
  );
}
