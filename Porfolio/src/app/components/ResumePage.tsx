import { FadeIn } from "./FadeIn";

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
    <div className="min-h-[70vh] flex items-center justify-center py-24 px-6 md:px-20">
      <div className="max-w-[600px] w-full text-center">
        <FadeIn>
          <span
            className="text-primary"
            style={{
              fontFamily: "'IBM Plex Mono', monospace",
              fontSize: "0.75rem",
              textShadow: "0 0 8px rgba(0,255,212,0.4)",
            }}
          >
            // RESUME
          </span>

          <h1
            className="mt-4 mb-6"
            style={{
              fontFamily: "'Bebas Neue', sans-serif",
              fontSize: "clamp(2rem, 5vw, 3.5rem)",
              letterSpacing: "0.04em",
              color: "#D4DEE8",
            }}
          >
            DOWNLOAD RESUME
          </h1>

          <p className="text-muted-foreground mb-8" style={{ fontSize: "0.78rem", lineHeight: 1.7 }}>
            PDF resume available for download. For the most current information,
            see the projects and about pages.
          </p>

          <div className="flex flex-col sm:flex-row gap-3 justify-center">
            <button
              onClick={handleDownload}
              className="inline-flex items-center justify-center px-8 py-3 bg-primary text-primary-foreground hover:shadow-[0_0_20px_rgba(0,255,212,0.3)] transition-all duration-150 cursor-pointer"
              style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.75rem", letterSpacing: "0.05em" }}
            >
              [ DOWNLOAD PDF ]
            </button>
            <a
              href="/Owen_Lindsey_Resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center px-8 py-3 border border-border text-muted-foreground hover:border-primary/50 hover:text-primary transition-all duration-150"
              style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.75rem", letterSpacing: "0.05em" }}
            >
              [ VIEW IN BROWSER ]
            </a>
          </div>
        </FadeIn>
      </div>
    </div>
  );
}
