// src/components/ui/card.tsx
import React from 'react';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({ children, className, ...props }) => {
  return (
    <div className={`card ${className}`} {...props}>
      {children}
    </div>
  );
};

/**
 * CardContent component is a functional React component that renders its children
 * inside a div with a class of "card-content" and any additional classes passed
 * through the className prop. It also spreads any other props onto the div.
 *
 * @param {CardProps} props - The props for the CardContent component.
 * @param {React.ReactNode} props.children - The content to be rendered inside the card.
 * @param {string} [props.className] - Additional class names to apply to the card content.
 * @returns {JSX.Element} The rendered CardContent component.
 */
export const CardContent: React.FC<CardProps> = ({ children, className, ...props }) => {
  return (
    <div className={`card-content ${className}`} {...props}>
      {children}
    </div>
  );
};