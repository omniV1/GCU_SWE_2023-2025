import { siteCopy, recruiterLinks } from "@/app/content/siteCopy";
import { FadeIn } from "./FadeIn";
import { SectionEyebrow } from "./SectionEyebrow";

const resume = siteCopy.resume;

export function ResumePage() {
  const handleDownload = () => {
    const link = document.createElement("a");
    link.href = "/Owen_Lindsey_Resume.pdf";
    link.download = "Owen_Lindsey_Resume.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="min-h-[70vh] py-24 px-6 md:px-20">
      <div className="max-w-[720px] mx-auto">
        <FadeIn>
          <div className="text-center mb-10">
            <SectionEyebrow className="block">{resume.eyebrow}</SectionEyebrow>

            <h1
              className="mt-4 mb-4"
              style={{
                fontFamily: "'Bebas Neue', sans-serif",
                fontSize: "clamp(2rem, 5vw, 3.5rem)",
                letterSpacing: "0.04em",
                color: "#D4DEE8",
              }}
            >
              {resume.title}
            </h1>

            <p
              className="text-muted-foreground mb-2"
              style={{ fontSize: "0.9rem", lineHeight: 1.75, fontFamily: "'Space Grotesk', sans-serif" }}
            >
              {resume.body}
            </p>
            <p
              className="text-foreground/60"
              style={{ fontSize: "0.78rem", fontFamily: "'IBM Plex Mono', monospace" }}
            >
              {resume.targetLine}
            </p>
          </div>

          <div
            className="border border-border p-5 mb-8 text-left"
            style={{ backgroundColor: "rgba(0,255,212,0.02)" }}
          >
            <p
              className="text-primary/70 tracking-widest mb-3"
              style={{ fontSize: "0.55rem", fontFamily: "'Space Grotesk', sans-serif", letterSpacing: "0.15em" }}
            >
              {resume.highlightsTitle}
            </p>
            <ul className="space-y-2">
              {resume.highlights.map((item) => (
                <li
                  key={item}
                  className="flex gap-2 text-foreground/65"
                  style={{ fontSize: "0.78rem", lineHeight: 1.6, fontFamily: "'Space Grotesk', sans-serif" }}
                >
                  <span className="text-primary shrink-0">→</span>
                  {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="flex flex-col sm:flex-row gap-3 justify-center mb-8">
            <button
              type="button"
              onClick={handleDownload}
              className="inline-flex items-center justify-center px-8 py-3 bg-primary text-primary-foreground hover:shadow-[0_0_20px_rgba(0,255,212,0.3)] transition-all duration-150 cursor-pointer"
              style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.75rem", letterSpacing: "0.05em" }}
            >
              {resume.download}
            </button>
            <a
              href="/Owen_Lindsey_Resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center px-8 py-3 border border-border text-muted-foreground hover:border-primary/50 hover:text-primary transition-all duration-150"
              style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.85rem" }}
            >
              {resume.viewInBrowser}
            </a>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-x-4 gap-y-2">
            {recruiterLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                download={"download" in link ? link.download : undefined}
                target={link.href.startsWith("http") ? "_blank" : undefined}
                rel={link.href.startsWith("http") ? "noopener noreferrer" : undefined}
                className="text-primary/60 hover:text-primary transition-colors duration-150"
                style={{ fontSize: "0.68rem", fontFamily: "'IBM Plex Mono', monospace" }}
              >
                {link.label}
              </a>
            ))}
          </div>
        </FadeIn>
      </div>
    </div>
  );
}
