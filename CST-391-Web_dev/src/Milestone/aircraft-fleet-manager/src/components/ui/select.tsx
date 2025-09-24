interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
    label?: string;
    error?: string;
  }
  
  /**
   * A custom select component that renders a label, a select dropdown, and an error message.
   *
   * @param {Object} props - The properties object.
   * @param {string} [props.label] - The label text for the select dropdown.
   * @param {string} [props.error] - The error message to display.
   * @param {string} [props.className] - Additional class names to apply to the select element.
   * @param {React.ReactNode} props.children - The options to be rendered within the select dropdown.
   * @param {Object} [props.rest] - Additional properties to be spread onto the select element.
   *
   * @returns {JSX.Element} The rendered select component.
   */
  export function Select({ label, error, className, children, ...props }: SelectProps) {
    return (
      <div className="space-y-2">
        {label && (
          <label className="text-sm font-medium text-white">
            {label}
          </label>
        )}
        <select
          className={`
            w-full rounded-md border bg-background px-3 py-2 text-sm 
            ring-offset-background focus-visible:outline-none 
            focus-visible:ring-2 focus-visible:ring-ring 
            focus-visible:ring-offset-2 disabled:cursor-not-allowed 
            disabled:opacity-50 border-input
            ${className}
          `}
          {...props}
        >
          {children}
        </select>
        {error && (
          <p className="text-sm font-medium text-red-500">
            {error}
          </p>
        )}
      </div>
    );
  }