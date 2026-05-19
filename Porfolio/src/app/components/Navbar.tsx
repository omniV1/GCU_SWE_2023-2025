import { useState } from "react";
import { Link, useLocation } from "react-router";
import { motion, AnimatePresence } from "motion/react";
import { siteCopy } from "@/app/content/siteCopy";

const navLinks = [
  { path: "/projects", label: siteCopy.nav.projects },
  { path: "/about", label: siteCopy.nav.about },
  { path: "/resume", label: siteCopy.nav.resume },
  { path: "/contact", label: siteCopy.nav.contact },
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
          <Link
            to="/"
            className="text-primary font-medium tracking-tight"
            style={{
              fontFamily: "'Space Grotesk', sans-serif",
              fontSize: "0.95rem",
            }}
          >
            {siteCopy.brand.logo}
          </Link>

          <div
            className="hidden md:flex items-center gap-6"
            style={{ fontFamily: "'Space Grotesk', sans-serif" }}
          >
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`py-1 text-sm transition-colors duration-150 ${
                  location.pathname === link.path ||
                  (link.path !== "/" && location.pathname.startsWith(link.path))
                    ? "text-primary"
                    : "text-muted-foreground hover:text-foreground"
                }`}
              >
                {link.label}
              </Link>
            ))}
          </div>

          <button
            type="button"
            className="md:hidden text-primary text-sm"
            onClick={() => setMobileOpen(!mobileOpen)}
            style={{ fontFamily: "'Space Grotesk', sans-serif" }}
          >
            {mobileOpen ? siteCopy.nav.menuOpen : siteCopy.nav.menuClosed}
          </button>
        </div>
      </div>

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
                  className={`px-3 py-2 text-sm transition-colors duration-150 ${
                    location.pathname === link.path
                      ? "text-primary"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
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
