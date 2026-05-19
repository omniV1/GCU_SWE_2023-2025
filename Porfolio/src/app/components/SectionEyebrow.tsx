interface SectionEyebrowProps {
  children: React.ReactNode
  className?: string
}

/** Small section label, readable, not terminal cosplay. */
export function SectionEyebrow({ children, className = "" }: SectionEyebrowProps) {
  return (
    <span
      className={`text-primary font-medium tracking-wide ${className}`}
      style={{
        fontFamily: "'Space Grotesk', sans-serif",
        fontSize: "0.8rem",
      }}
    >
      {children}
    </span>
  )
}
