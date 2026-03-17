export function Footer() {
  return (
    <footer className="border-t border-border py-8 px-6 md:px-20" style={{ backgroundColor: "#0A0E12" }}>
      <div className="max-w-[1200px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <span
          className="text-muted-foreground/40"
          style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.65rem" }}
        >
          &copy; 2026 Owen Lindsey // Built with precision.
        </span>
        <div className="flex items-center gap-4">
          <a
            href="https://github.com/omniV1"
            target="_blank"
            rel="noopener noreferrer"
            className="text-muted-foreground/60 hover:text-primary transition-colors duration-150"
            style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.65rem", letterSpacing: "0.1em" }}
          >
            GITHUB
          </a>
          <span className="text-border">//</span>
          <a
            href="https://www.linkedin.com/in/owen-lindsey-5b323a23b/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-muted-foreground/60 hover:text-primary transition-colors duration-150"
            style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.65rem", letterSpacing: "0.1em" }}
          >
            LINKEDIN
          </a>
          <span className="text-border">//</span>
          <a
            href="mailto:owen.lindsey98@outlook.com"
            className="text-muted-foreground/60 hover:text-primary transition-colors duration-150"
            style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: "0.65rem", letterSpacing: "0.1em" }}
          >
            EMAIL
          </a>
        </div>
      </div>
    </footer>
  );
}
