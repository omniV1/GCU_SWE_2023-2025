import { Link } from "react-router";

export function NotFound() {
  return (
    <div className="min-h-[60vh] flex items-center justify-center px-6">
      <div className="text-center">
        <h1
          className="text-primary mb-4"
          style={{
            fontFamily: "'Bebas Neue', sans-serif",
            fontSize: "5rem",
            letterSpacing: "0.1em",
            textShadow: "0 0 30px rgba(0,255,212,0.3), 0 0 60px rgba(0,255,212,0.1)",
          }}
        >
          404
        </h1>
        <p
          className="text-muted-foreground mb-2"
          style={{ fontSize: "0.78rem", fontFamily: "'IBM Plex Mono', monospace" }}
        >
          ERROR :: TARGET NOT FOUND
        </p>
        <p
          className="text-muted-foreground/50 mb-6"
          style={{ fontSize: "0.68rem", fontFamily: "'IBM Plex Mono', monospace" }}
        >
          Returning to base...
        </p>
        <Link
          to="/"
          className="inline-flex items-center px-6 py-3 border border-primary text-primary hover:bg-primary/10 hover:shadow-[0_0_20px_rgba(0,255,212,0.15)] transition-all duration-150"
          style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.75rem" }}
        >
          [ RETURN HOME ]
        </Link>
      </div>
    </div>
  );
}
