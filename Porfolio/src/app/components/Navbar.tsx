import { useState } from "react";
import { Link, useLocation } from "react-router";
import { motion, AnimatePresence } from "motion/react";

const navLinks = [
  { path: "/projects", label: "PROJECTS" },
  { path: "/about", label: "ABOUT" },
  { path: "/resume", label: "RESUME" },
  { path: "/contact", label: "CONTACT" },
];

export function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const location = useLocation();

  return (
    <nav
      className="fixed top-0 left-0 right-0 z-50 border-b border-border"
      style={{ backgroundColor: "rgba(10, 14, 18, 0.92)", backdropFilter: "blur(12px)" }}
    >
      <div className="max-w-[1200px] mx-auto px-6 md:px-20">
        <div className="flex items-center justify-between h-12">
          {/* Logo */}
          <Link
            to="/"
            className="text-primary tracking-widest"
            style={{
              fontFamily: "'IBM Plex Mono', monospace",
              fontSize: "0.85rem",
              textShadow: "0 0 10px rgba(0,255,212,0.5)",
            }}
          >
            OL://
          </Link>

          {/* Desktop Nav */}
          <div
            className="hidden md:flex items-center"
            style={{ fontFamily: "'Space Grotesk', sans-serif" }}
          >
            {navLinks.map((link, i) => (
              <span key={link.path} className="flex items-center">
                {i > 0 && (
                  <span className="text-[#1A2633] mx-3 select-none" style={{ fontSize: "0.75rem" }}>
                    //
                  </span>
                )}
                <Link
                  to={link.path}
                  className={`py-1 tracking-wider transition-colors duration-150 ${
                    location.pathname === link.path || (link.path !== "/" && location.pathname.startsWith(link.path))
                      ? "text-primary"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                  style={{
                    fontSize: "0.7rem",
                    letterSpacing: "0.12em",
                    ...(location.pathname === link.path || (link.path !== "/" && location.pathname.startsWith(link.path))
                      ? { textShadow: "0 0 8px rgba(0,255,212,0.4)" }
                      : {}),
                  }}
                >
                  {link.label}
                </Link>
              </span>
            ))}
          </div>

          {/* Mobile Toggle */}
          <button
            className="md:hidden text-primary tracking-widest"
            onClick={() => setMobileOpen(!mobileOpen)}
            style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.7rem" }}
          >
            [{mobileOpen ? "CLOSE" : "MENU"}]
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
            className="md:hidden border-t border-border overflow-hidden"
            style={{ backgroundColor: "rgba(10, 14, 18, 0.97)" }}
          >
            <div
              className="px-6 py-4 flex flex-col gap-1"
              style={{ fontFamily: "'Space Grotesk', sans-serif" }}
            >
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  onClick={() => setMobileOpen(false)}
                  className={`px-3 py-2 tracking-wider transition-colors duration-150 ${
                    location.pathname === link.path
                      ? "text-primary"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                  style={{ fontSize: "0.75rem", letterSpacing: "0.1em" }}
                >
                  {link.label}
                </Link>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
