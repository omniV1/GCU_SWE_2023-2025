import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

/**
 * Generates a set of class names for button components based on variant and size options.
 *
 * @param baseClassNames - The base class names for the button component.
 * @param options - An object containing variant and size options.
 * @param options.variants - An object specifying the different variants and their corresponding class names.
 * @param options.variants.variant - The variant of the button, which can be one of the following:
 *   - `default`: Primary button with background and foreground colors.
 *   - `destructive`: Destructive button with background and foreground colors.
 *   - `outline`: Button with border and transparent background.
 *   - `secondary`: Secondary button with background and foreground colors.
 *   - `ghost`: Button with hover background and foreground colors.
 *   - `link`: Button styled as a link with underline.
 * @param options.variants.size - The size of the button, which can be one of the following:
 *   - `default`: Default size with height, padding, and text size.
 *   - `sm`: Small size with height, padding, and text size.
 *   - `lg`: Large size with height, padding, and text size.
 *   - `icon`: Icon size with equal height and width.
 * @param options.defaultVariants - An object specifying the default variant and size.
 * @param options.defaultVariants.variant - The default variant of the button.
 * @param options.defaultVariants.size - The default size of the button.
 * @returns A string containing the generated class names for the button component.
 */
const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-transparent shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }