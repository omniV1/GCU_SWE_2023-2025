import { Link } from "react-router";
import { siteCopy } from "@/app/content/siteCopy";
import { FadeIn } from "./FadeIn";
import { ImageWithFallback } from "./figma/ImageWithFallback";
import { HudCard } from "./HudCard";
import { SectionEyebrow } from "./SectionEyebrow";
import { Typewriter } from "./Typewriter";
import { AnimatedCounter } from "./AnimatedCounter";

const HERO_BG = "https://images.unsplash.com/photo-1764347840355-b30ef7283a16?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxkYXJrJTIwbW91bnRhaW4lMjBhZXJpYWwlMjBsYW5kc2NhcGUlMjBtb29keXxlbnwxfHx8fDE3NzM3MDEyNDF8MA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral";

const ABOUT_BG = "https://images.unsplash.com/photo-1745202089032-e2ab9acb5b3c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxkZXNlcnQlMjB0ZXJyYWluJTIwYWVyaWFsJTIwZGFyayUyMHNvdXRod2VzdHxlbnwxfHx8fDE3NzM3MDEyNDF8MA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral";

const { home: copy, featuredProjects } = siteCopy;

const techStack = [
  {
    name: "LANGUAGES",
    items: ["Java", "C# / .NET", "Python", "TypeScript", "JavaScript", "C / Bash", "SQL"],
  },
  {
    name: "FRONTEND",
    items: ["React + TypeScript", "Angular", "Tailwind CSS", "Radix UI", "Recharts", "Bootstrap"],
  },
  {
    name: "BACKEND",
    items: ["Spring Boot 3", "Node.js / Express", "ASP.NET Core MVC", ".NET Web API", "Spring Security", "REST API Design", "MongoDB / MySQL"],
  },
  {
    name: "SYSTEMS & TOOLS",
    items: ["Docker", "SonarQube", "Git / GitHub", "OpenAPI / Swagger", "Pre-commit Hooks", "Maven", "OS Fundamentals"],
  },
];

const keyMetrics = copy.metrics;

export function HomePage() {
  return (
    <div>
      {/* ===== HERO ===== */}
      <section className="relative min-h-screen flex items-center overflow-hidden">
        {/* Background */}
        <div className="absolute inset-0">
          <ImageWithFallback
            src={HERO_BG}
            alt=""
            className="w-full h-full object-cover"
            style={{ filter: "brightness(0.12) saturate(0.15) hue-rotate(180deg)" }}
          />
          {/* Grid overlay */}
          <div
            className="absolute inset-0"
            style={{
              backgroundImage: `repeating-linear-gradient(0deg, transparent, transparent 60px, rgba(0,255,212,0.03) 60px, rgba(0,255,212,0.03) 61px),
                repeating-linear-gradient(90deg, transparent, transparent 60px, rgba(0,255,212,0.03) 60px, rgba(0,255,212,0.03) 61px)`,
            }}
          />
          {/* Cyan gradient vignette */}
          <div
            className="absolute inset-0 z-[2]"
            style={{
              background: "radial-gradient(ellipse at 30% 50%, rgba(0,255,212,0.04) 0%, transparent 60%), radial-gradient(ellipse at 80% 20%, rgba(255,45,107,0.03) 0%, transparent 50%)",
            }}
          />
        </div>

        <div className="relative z-10 max-w-[1200px] mx-auto px-6 md:px-20 w-full py-32">
          <FadeIn delay={0.2}>
            <h1
              className="glitch-hover"
              style={{
                fontFamily: "'Bebas Neue', sans-serif",
                fontSize: "clamp(4rem, 12vw, 9rem)",
                lineHeight: 0.9,
                letterSpacing: "0.02em",
                color: "#D4DEE8",
              }}
            >
              OWEN
              <br />
              LINDSEY
            </h1>
            <style>{`
              .glitch-hover:hover {
                animation: glitch 0.3s ease-in-out;
              }
            `}</style>
          </FadeIn>

          <FadeIn delay={0.35}>
            <div
              className="mt-4 text-primary h-6"
              style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.85rem" }}
            >
              <Typewriter
                texts={[...copy.typewriter]}
                typingSpeed={60}
                deletingSpeed={35}
                pauseTime={2000}
              />
            </div>
            <p
              className="mt-3 text-muted-foreground max-w-xl"
              style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.95rem", lineHeight: 1.75 }}
            >
              {copy.heroTagline}
            </p>
            <p
              className="mt-2 text-muted-foreground/80 max-w-xl"
              style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.82rem", lineHeight: 1.7 }}
            >
              {copy.heroSub}
            </p>
          </FadeIn>

          {/* Status Readout */}
          <FadeIn delay={0.5}>
            <div className="mt-12 relative">
              {/* HUD corner brackets */}
              <div className="absolute -top-1 -left-1 w-4 h-4 border-t border-l border-primary/60" />
              <div className="absolute -top-1 -right-1 w-4 h-4 border-t border-r border-primary/60" />
              <div className="absolute -bottom-1 -left-1 w-4 h-4 border-b border-l border-primary/60" />
              <div className="absolute -bottom-1 -right-1 w-4 h-4 border-b border-r border-primary/60" />

              <div className="border border-border bg-card/40 overflow-x-auto" style={{ backdropFilter: "blur(8px)" }}>
                <div className="grid grid-cols-2 md:grid-cols-4 min-w-[500px]">
                  {copy.readout.map((item, i) => (
                    <div
                      key={item.label}
                      className={`p-4 md:p-5 ${i > 0 ? "border-l border-border" : ""}`}
                    >
                      <p
                        className="text-primary tracking-widest mb-2"
                        style={{
                          fontFamily: "'IBM Plex Mono', monospace",
                          fontSize: "0.55rem",
                          textShadow: "0 0 6px rgba(0,255,212,0.3)",
                        }}
                      >
                        {item.label}
                      </p>
                      <p
                        className="text-foreground/80 whitespace-pre-line"
                        style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.72rem", lineHeight: 1.6 }}
                      >
                        {item.value}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </FadeIn>

          {/* CTAs */}
          <FadeIn delay={0.65}>
            <div className="mt-8 flex flex-col sm:flex-row gap-3">
              <Link
                to="/projects"
                className="inline-flex items-center justify-center px-6 py-3 border border-primary text-primary hover:bg-primary/10 hover:shadow-[0_0_20px_rgba(0,255,212,0.15)] transition-all duration-150"
                style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.8rem", fontWeight: 500 }}
              >
                {copy.ctaProjects}
              </Link>
              <Link
                to="/contact"
                className="inline-flex items-center justify-center px-6 py-3 bg-primary text-primary-foreground hover:shadow-[0_0_20px_rgba(0,255,212,0.3)] transition-all duration-150"
                style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.8rem", fontWeight: 500 }}
              >
                {copy.ctaContact}
              </Link>
              <a
                href="/Owen_Lindsey_Resume.pdf" download
                className="inline-flex items-center justify-center px-6 py-3 border border-border text-muted-foreground hover:border-primary/50 hover:text-primary transition-all duration-150"
                style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.8rem" }}
              >
                {copy.ctaResume}
              </a>
            </div>
          </FadeIn>
        </div>
      </section>

      {/* ===== KEY METRICS ===== */}
      <section className="border-t border-border" style={{ backgroundColor: "#0C1016" }}>
        <div className="max-w-[1200px] mx-auto px-6 md:px-20">
          <FadeIn>
            <div className="grid grid-cols-2 md:grid-cols-4 divide-x divide-border">
              {keyMetrics.map((metric) => (
                <div key={metric.label} className="py-8 px-4 text-center">
                  <AnimatedCounter
                    value={metric.value}
                    className="text-primary block"
                    style={{
                      fontFamily: "'Bebas Neue', sans-serif",
                      fontSize: "2.2rem",
                      letterSpacing: "0.02em",
                      textShadow: "0 0 15px rgba(0,255,212,0.3)",
                    }}
                  />
                  <p
                    className="text-foreground/70 tracking-widest mt-1"
                    style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.55rem", letterSpacing: "0.1em" }}
                  >
                    {metric.label}
                  </p>
                  <p
                    className="text-muted-foreground mt-0.5"
                    style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.55rem" }}
                  >
                    {metric.sub}
                  </p>
                </div>
              ))}
            </div>
          </FadeIn>
        </div>
      </section>

      {/* ===== FEATURED PROJECTS ===== */}
      <section className="py-20 px-6 md:px-20 border-t border-border">
        <div className="max-w-[1200px] mx-auto">
          <FadeIn>
            <div className="flex items-center gap-4 mb-8">
              <SectionEyebrow>{copy.workSection}</SectionEyebrow>
              <div className="flex-1 h-px" style={{ background: "linear-gradient(90deg, #1A2633, transparent)" }} />
            </div>
          </FadeIn>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {featuredProjects.map((project, i) => (
              <FadeIn key={project.id} delay={i * 0.1}>
                <Link to={`/projects`} className="group block h-full">
                  <HudCard className="h-full flex flex-col p-5" label={`PRJ.0${i + 1}`}>
                    {/* Tags */}
                    <div className="flex flex-wrap gap-1.5 mb-4">
                      {project.tags.map((tag) => (
                        <span
                          key={tag}
                          className="px-2 py-0.5 bg-primary/5 text-primary/70 border border-primary/10"
                          style={{ fontSize: "0.6rem", fontFamily: "'IBM Plex Mono', monospace" }}
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                    {/* Title */}
                    <h3
                      className="text-foreground mb-3 group-hover:text-primary transition-colors duration-150"
                      style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: "1.4rem", letterSpacing: "0.04em" }}
                    >
                      {project.title}
                    </h3>
                    {/* Description */}
                    <p
                      className="text-muted-foreground flex-1 mb-5"
                      style={{ fontSize: "0.75rem", lineHeight: 1.7 }}
                    >
                      {project.description}
                    </p>
                    {/* Live link badge */}
                    {"liveUrl" in project && project.liveUrl && (
                      <a
                        href={project.liveUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        onClick={(e) => e.stopPropagation()}
                        className="inline-flex items-center gap-1.5 mb-3 text-accent hover:underline"
                        style={{
                          fontSize: "0.68rem",
                          fontFamily: "'IBM Plex Mono', monospace",
                          textShadow: "0 0 8px rgba(255,45,107,0.4)",
                        }}
                      >
                        Live · {new URL(project.liveUrl).host.replace(/^www\./, "")}
                      </a>
                    )}
                    {/* Link */}
                    <span
                      className="text-primary/70 group-hover:text-primary transition-colors duration-150"
                      style={{ fontSize: "0.7rem", fontFamily: "'IBM Plex Mono', monospace" }}
                    >
                      Project details &rarr;
                    </span>
                  </HudCard>
                </Link>
              </FadeIn>
            ))}
          </div>

          <FadeIn delay={0.3}>
            <div className="mt-6 text-right">
              <Link
                to="/projects"
                className="text-primary/70 hover:text-primary transition-colors duration-150"
                style={{ fontSize: "0.7rem", fontFamily: "'IBM Plex Mono', monospace" }}
              >
                {copy.workViewAll} &rarr;
              </Link>
            </div>
          </FadeIn>
        </div>
      </section>

      {/* ===== TECHNICAL PROFILE ===== */}
      <section className="py-20 px-6 md:px-20 border-t border-border" style={{ backgroundColor: "#0C1016" }}>
        <div className="max-w-[1200px] mx-auto">
          <FadeIn>
            <div className="flex items-center gap-4 mb-10">
              <SectionEyebrow>{copy.techSection}</SectionEyebrow>
              <div className="flex-1 h-px" style={{ background: "linear-gradient(90deg, #1A2633, transparent)" }} />
            </div>
          </FadeIn>

          <FadeIn delay={0.1}>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
              {techStack.map((category) => (
                <div key={category.name}>
                  <p
                    className="text-primary tracking-widest mb-4 pb-2 border-b border-border"
                    style={{
                      fontSize: "0.6rem",
                      fontFamily: "'Space Grotesk', sans-serif",
                      textShadow: "0 0 6px rgba(0,255,212,0.3)",
                    }}
                  >
                    {category.name}
                  </p>
                  <div className="space-y-0">
                    {category.items.map((item, i) => (
                      <p
                        key={item}
                        className={`text-foreground/60 py-1.5 hover:text-primary/80 hover:pl-2 transition-all duration-150 ${i < category.items.length - 1 ? "border-b border-border/20" : ""}`}
                        style={{ fontSize: "0.72rem", fontFamily: "'IBM Plex Mono', monospace" }}
                      >
                        {item}
                      </p>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </FadeIn>
        </div>
      </section>

      {/* ===== ABOUT STRIP ===== */}
      <section className="border-t border-border">
        <div className="max-w-[1200px] mx-auto grid grid-cols-1 md:grid-cols-2">
          {/* Left — Photo */}
          <div className="relative h-64 md:h-auto overflow-hidden">
            <ImageWithFallback
              src={ABOUT_BG}
              alt=""
              className="w-full h-full object-cover"
              style={{ filter: "brightness(0.15) saturate(0.15) hue-rotate(180deg)" }}
            />
            <div
              className="absolute inset-0 opacity-[0.06]"
              style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E")`,
              }}
            />
            <div
              className="absolute inset-0"
              style={{ background: "linear-gradient(135deg, rgba(0,255,212,0.05) 0%, transparent 60%)" }}
            />
          </div>

          {/* Right — Bio */}
          <div className="p-8 md:p-12 lg:p-16 flex flex-col justify-center">
            <FadeIn>
              <h2
                className="mb-6"
                style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: "2rem", letterSpacing: "0.04em", color: "#D4DEE8" }}
              >
                {copy.aboutTitle}
              </h2>
              <div className="space-y-3 text-foreground/70" style={{ fontSize: "0.8rem", lineHeight: 1.8 }}>
                <div className="flex items-start gap-3">
                  <span className="w-1 h-1 rounded-full bg-primary shrink-0 mt-2.5" style={{ boxShadow: "0 0 4px #00FFD4" }} />
                  <p>
                    <span className="text-foreground/90">{copy.aboutPoints[0].lead}</span> {copy.aboutPoints[0].body}
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <span className="w-1 h-1 rounded-full bg-primary shrink-0 mt-2.5" style={{ boxShadow: "0 0 4px #00FFD4" }} />
                  <p>
                    <span className="text-foreground/90">{copy.aboutPoints[1].lead}</span> {copy.aboutPoints[1].body}
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <span className="w-1 h-1 rounded-full bg-primary shrink-0 mt-2.5" style={{ boxShadow: "0 0 4px #00FFD4" }} />
                  <p>
                    <span className="text-foreground/90">{copy.aboutPoints[2].lead}</span> {copy.aboutPoints[2].body}
                  </p>
                </div>
              </div>
              <div className="mt-6 flex gap-3">
                <Link
                  to="/about"
                  className="inline-block text-primary/70 hover:text-primary transition-colors duration-150"
                  style={{ fontSize: "0.7rem", fontFamily: "'IBM Plex Mono', monospace" }}
                >
                  {copy.aboutMore} &rarr;
                </Link>
                <Link
                  to="/contact"
                  className="inline-block text-accent/70 hover:text-accent transition-colors duration-150"
                  style={{ fontSize: "0.7rem", fontFamily: "'IBM Plex Mono', monospace" }}
                >
                  {copy.aboutContact} &rarr;
                </Link>
              </div>
            </FadeIn>
          </div>
        </div>
      </section>

      {/* ===== BOTTOM CTA ===== */}
      <section className="border-t border-border py-16 px-6 md:px-20 text-center" style={{ backgroundColor: "#0C1016" }}>
        <div className="max-w-[600px] mx-auto">
          <FadeIn>
            <SectionEyebrow className="block mb-4 text-primary/70">Open to work</SectionEyebrow>
            <h2
              style={{
                fontFamily: "'Bebas Neue', sans-serif",
                fontSize: "clamp(1.8rem, 4vw, 2.8rem)",
                letterSpacing: "0.04em",
                color: "#D4DEE8",
              }}
            >
              {copy.ctaTitle}
            </h2>
            <p
              className="text-muted-foreground mt-3 mb-8"
              style={{ fontSize: "0.9rem", lineHeight: 1.7, fontFamily: "'Space Grotesk', sans-serif" }}
            >
              {copy.ctaBody}
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Link
                to="/contact"
                className="inline-flex items-center justify-center px-8 py-3 bg-primary text-primary-foreground hover:shadow-[0_0_20px_rgba(0,255,212,0.3)] transition-all duration-150"
                style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.85rem", fontWeight: 500 }}
              >
                {copy.ctaBottomContact}
              </Link>
              <a
                href="/Owen_Lindsey_Resume.pdf" download
                className="inline-flex items-center justify-center px-8 py-3 border border-border text-muted-foreground hover:border-primary/50 hover:text-primary transition-all duration-150"
                style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.85rem" }}
              >
                {copy.ctaBottomResume}
              </a>
            </div>
          </FadeIn>
        </div>
      </section>
    </div>
  );
}
