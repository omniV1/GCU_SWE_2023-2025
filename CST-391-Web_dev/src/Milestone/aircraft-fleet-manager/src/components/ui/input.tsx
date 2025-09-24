import * as React from "react"

import { cn } from "@/lib/utils"

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: string;  // Add this line to support error messages
}

/**
 * A forward-ref input component that supports error handling and custom styling.
 *
 * @param {string} className - Additional class names for the input element.
 * @param {string} type - The type of the input element (e.g., "text", "password").
 * @param {string} [error] - An optional error message to display below the input.
 * @param {React.Ref<HTMLInputElement>} ref - A ref to the input element.
 * @param {InputProps} props - Additional props to pass to the input element.
 *
 * @returns {JSX.Element} The rendered input component with optional error message.
 */
const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, error, ...props }, ref) => {
    return (
      <div className="space-y-2">
        <input
          type={type}
          className={cn(
            "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
            error && "border-red-500",  // Add red border when there's an error
            className
          )}
          ref={ref}
          {...props}
        />
        {error && (
          <p className="text-sm font-medium text-red-500">
            {error}
          </p>
        )}
      </div>
    )
  }
)
Input.displayName = "Input"

export { Input }