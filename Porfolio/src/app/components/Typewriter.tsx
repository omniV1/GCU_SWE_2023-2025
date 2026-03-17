import { useEffect, useRef, useState } from "react";

interface TypewriterProps {
  texts: string[];
  className?: string;
  style?: React.CSSProperties;
  typingSpeed?: number;
  deletingSpeed?: number;
  pauseTime?: number;
}

export function Typewriter({
  texts,
  className,
  style,
  typingSpeed = 50,
  deletingSpeed = 30,
  pauseTime = 2500,
}: TypewriterProps) {
  const [displayed, setDisplayed] = useState("");
  const [textIndex, setTextIndex] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);
  const timeoutRef = useRef<number>(0);

  useEffect(() => {
    const current = texts[textIndex];

    if (!isDeleting) {
      if (displayed.length < current.length) {
        timeoutRef.current = window.setTimeout(() => {
          setDisplayed(current.slice(0, displayed.length + 1));
        }, typingSpeed);
      } else {
        timeoutRef.current = window.setTimeout(() => {
          setIsDeleting(true);
        }, pauseTime);
      }
    } else {
      if (displayed.length > 0) {
        timeoutRef.current = window.setTimeout(() => {
          setDisplayed(current.slice(0, displayed.length - 1));
        }, deletingSpeed);
      } else {
        setIsDeleting(false);
        setTextIndex((prev) => (prev + 1) % texts.length);
      }
    }

    return () => clearTimeout(timeoutRef.current);
  }, [displayed, isDeleting, textIndex, texts, typingSpeed, deletingSpeed, pauseTime]);

  return (
    <span className={className} style={style}>
      {displayed}
      <span
        className="inline-block w-[2px] h-[1em] bg-primary ml-0.5 align-middle"
        style={{ animation: "terminal-blink 1s step-end infinite" }}
      />
    </span>
  );
}
