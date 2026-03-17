import { type ReactNode, useRef, useState } from "react";

interface HudCardProps {
  children: ReactNode;
  className?: string;
  label?: string;
}

export function HudCard({ children, className = "", label }: HudCardProps) {
  const cardRef = useRef<HTMLDivElement>(null);
  const [style, setStyle] = useState<React.CSSProperties>({});

  function handleMove(e: React.MouseEvent) {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;
    const y = (e.clientY - rect.top) / rect.height;
    const rotateX = (0.5 - y) * 8;
    const rotateY = (x - 0.5) * 8;
    setStyle({
      transform: `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`,
      transition: "transform 0.1s ease-out",
    });
  }

  function handleLeave() {
    setStyle({
      transform: "perspective(800px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)",
      transition: "transform 0.4s ease-out",
    });
  }

  return (
    <div
      ref={cardRef}
      className={`relative group/hud ${className}`}
      style={style}
      onMouseMove={handleMove}
      onMouseLeave={handleLeave}
    >
      {/* Card body */}
      <div
        className="relative border border-border bg-card/60 h-full transition-all duration-150 group-hover/hud:border-primary/30 group-hover/hud:shadow-[0_0_30px_rgba(0,255,212,0.08)]"
        style={{ backdropFilter: "blur(4px)" }}
      >
        {/* HUD corner brackets */}
        <div className="absolute -top-px -left-px w-3 h-3 border-t border-l border-primary/40 group-hover/hud:border-primary/70 transition-colors duration-150" />
        <div className="absolute -top-px -right-px w-3 h-3 border-t border-r border-primary/40 group-hover/hud:border-primary/70 transition-colors duration-150" />
        <div className="absolute -bottom-px -left-px w-3 h-3 border-b border-l border-primary/40 group-hover/hud:border-primary/70 transition-colors duration-150" />
        <div className="absolute -bottom-px -right-px w-3 h-3 border-b border-r border-primary/40 group-hover/hud:border-primary/70 transition-colors duration-150" />

        {/* Optional label */}
        {label && (
          <span
            className="absolute -top-2.5 right-4 px-1.5 bg-background text-primary/40 group-hover/hud:text-primary/70 transition-colors duration-150"
            style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: "0.5rem", letterSpacing: "0.1em" }}
          >
            {label}
          </span>
        )}

        {children}
      </div>
    </div>
  );
}
