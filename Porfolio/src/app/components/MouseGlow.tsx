import { useEffect, useRef } from "react";

export function MouseGlow() {
  const glowRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleMove(e: MouseEvent) {
      if (!glowRef.current) return;
      glowRef.current.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
      glowRef.current.style.opacity = "1";
    }

    function handleLeave() {
      if (!glowRef.current) return;
      glowRef.current.style.opacity = "0";
    }

    window.addEventListener("mousemove", handleMove);
    document.addEventListener("mouseleave", handleLeave);
    return () => {
      window.removeEventListener("mousemove", handleMove);
      document.removeEventListener("mouseleave", handleLeave);
    };
  }, []);

  return (
    <div
      ref={glowRef}
      className="fixed top-0 left-0 pointer-events-none z-[1]"
      style={{
        width: 600,
        height: 600,
        marginLeft: -300,
        marginTop: -300,
        background: "radial-gradient(circle, rgba(0,255,212,0.04) 0%, rgba(0,255,212,0.01) 30%, transparent 60%)",
        opacity: 0,
        transition: "opacity 0.3s ease",
        willChange: "transform",
      }}
    />
  );
}
