import { useState } from "react";
import { FadeIn } from "./FadeIn";

export function ContactPage() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => setSubmitted(false), 3000);
    setForm({ name: "", email: "", message: "" });
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center py-24 px-6 md:px-20 relative">
      {/* Background grid */}
      <div
        className="absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage: `repeating-linear-gradient(0deg, transparent, transparent 60px, rgba(0,255,212,0.3) 60px, rgba(0,255,212,0.3) 61px),
            repeating-linear-gradient(90deg, transparent, transparent 60px, rgba(0,255,212,0.3) 60px, rgba(0,255,212,0.3) 61px)`,
        }}
      />

      <div className="max-w-[650px] w-full relative">
        <FadeIn>
          <div className="text-center">
            <span
              className="text-primary"
              style={{
                fontFamily: "'IBM Plex Mono', monospace",
                fontSize: "0.75rem",
                textShadow: "0 0 8px rgba(0,255,212,0.4)",
              }}
            >
              // CONTACT
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
              LET'S BUILD SOMETHING.
            </h1>

            <div className="mb-6">
              <p className="text-foreground" style={{ fontSize: "0.9rem" }}>
                Owen Lindsey
              </p>
              <p
                className="text-muted-foreground mt-1"
                style={{ fontSize: "0.78rem", fontFamily: "'Space Grotesk', sans-serif" }}
              >
                Software Engineer // Phoenix, AZ
              </p>
            </div>
          </div>

          {/* What I'm looking for */}
          <div className="border border-border p-4 mb-8" style={{ backgroundColor: "rgba(0,255,212,0.02)" }}>
            <p
              className="text-primary/70 tracking-widest mb-3"
              style={{ fontSize: "0.55rem", fontFamily: "'Space Grotesk', sans-serif", letterSpacing: "0.15em" }}
            >
              CURRENTLY SEEKING
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {[
                "Full-time software engineering roles",
                "Contract / freelance projects",
                "Remote or Phoenix, AZ on-site",
                "Full-stack, backend, or systems work",
              ].map((item) => (
                <div key={item} className="flex items-center gap-2">
                  <span
                    className="w-1 h-1 rounded-full bg-primary shrink-0"
                    style={{ boxShadow: "0 0 4px #00FFD4" }}
                  />
                  <span className="text-foreground/60" style={{ fontSize: "0.72rem", fontFamily: "'IBM Plex Mono', monospace" }}>
                    {item}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Links */}
          <div className="flex items-center justify-center gap-3 mb-6 flex-wrap">
            {[
              { label: "Email", href: "mailto:owen.lindsey98@outlook.com" },
              { label: "GitHub", href: "https://github.com/omniV1" },
              { label: "LinkedIn", href: "https://www.linkedin.com/in/owen-lindsey-5b323a23b/" },
              { label: "Resume PDF", href: "/Owen_Lindsey_Resume.pdf" },
            ].map((link, i) => (
              <span key={link.label} className="flex items-center">
                {i > 0 && <span className="text-border mx-2">//</span>}
                <a
                  href={link.href}
                  target={link.href.startsWith("http") ? "_blank" : undefined}
                  rel={link.href.startsWith("http") ? "noopener noreferrer" : undefined}
                  className="text-primary/70 hover:text-primary transition-colors duration-150"
                  style={{ fontSize: "0.72rem", fontFamily: "'IBM Plex Mono', monospace" }}
                >
                  [ {link.label} ]
                </a>
              </span>
            ))}
          </div>

          <p
            className="text-muted-foreground mb-10 italic text-center"
            style={{ fontSize: "0.75rem" }}
          >
            "Available for full-time roles, contract work, and interesting problems."
          </p>
        </FadeIn>

        {/* Form */}
        <FadeIn delay={0.2}>
          <form onSubmit={handleSubmit} className="text-left space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label
                  className="block text-muted-foreground tracking-widest mb-1.5"
                  style={{
                    fontSize: "0.55rem",
                    fontFamily: "'Space Grotesk', sans-serif",
                    letterSpacing: "0.12em",
                    textShadow: "0 0 4px rgba(0,255,212,0.2)",
                  }}
                >
                  NAME
                </label>
                <input
                  type="text"
                  value={form.name}
                  onChange={(e) => setForm({ ...form, name: e.target.value })}
                  required
                  className="w-full px-4 py-3 bg-[#0C1016] border border-border text-foreground focus:border-primary/40 focus:shadow-[0_0_10px_rgba(0,255,212,0.1)] focus:outline-none transition-all duration-150"
                  style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.8rem", caretColor: "#00FFD4" }}
                />
              </div>
              <div>
                <label
                  className="block text-muted-foreground tracking-widest mb-1.5"
                  style={{
                    fontSize: "0.55rem",
                    fontFamily: "'Space Grotesk', sans-serif",
                    letterSpacing: "0.12em",
                    textShadow: "0 0 4px rgba(0,255,212,0.2)",
                  }}
                >
                  EMAIL
                </label>
                <input
                  type="email"
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                  required
                  className="w-full px-4 py-3 bg-[#0C1016] border border-border text-foreground focus:border-primary/40 focus:shadow-[0_0_10px_rgba(0,255,212,0.1)] focus:outline-none transition-all duration-150"
                  style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.8rem", caretColor: "#00FFD4" }}
                />
              </div>
            </div>
            <div>
              <label
                className="block text-muted-foreground tracking-widest mb-1.5"
                style={{
                  fontSize: "0.55rem",
                  fontFamily: "'Space Grotesk', sans-serif",
                  letterSpacing: "0.12em",
                  textShadow: "0 0 4px rgba(0,255,212,0.2)",
                }}
              >
                MESSAGE
              </label>
              <textarea
                value={form.message}
                onChange={(e) => setForm({ ...form, message: e.target.value })}
                required
                rows={4}
                className="w-full px-4 py-3 bg-[#0C1016] border border-border text-foreground focus:border-primary/40 focus:shadow-[0_0_10px_rgba(0,255,212,0.1)] focus:outline-none transition-all duration-150 resize-none"
                style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.8rem", caretColor: "#00FFD4" }}
                placeholder="Tell me about the role or project..."
              />
            </div>
            <button
              type="submit"
              className="w-full px-6 py-3 bg-primary text-primary-foreground hover:shadow-[0_0_20px_rgba(0,255,212,0.3)] transition-all duration-150"
              style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.75rem", letterSpacing: "0.05em" }}
            >
              {submitted ? "TRANSMISSION SENT." : "> SEND_MESSAGE"}
            </button>
          </form>
        </FadeIn>
      </div>
    </div>
  );
}
