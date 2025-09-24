// src/components/ui/dropdown-menu.tsx
import React from 'react';

interface DropdownMenuProps {
  children: React.ReactNode;
}

export const DropdownMenu: React.FC<DropdownMenuProps> = ({ children }) => {
  return (
    <div className="dropdown-menu">
      {children}
    </div>
  );
};

interface DropdownMenuTriggerProps {
  children: React.ReactNode;
  onClick: () => void;
}

/**
 * DropdownMenuTrigger component.
 *
 * This component serves as a trigger for a dropdown menu. It wraps its children
 * in a `div` element with an `onClick` handler and a specific CSS class.
 *
 * @param {DropdownMenuTriggerProps} props - The properties for the component.
 * @param {React.ReactNode} props.children - The child elements to be rendered inside the trigger.
 * @param {React.MouseEventHandler<HTMLDivElement>} props.onClick - The function to be called when the trigger is clicked.
 *
 * @returns {JSX.Element} The rendered `div` element that acts as the dropdown trigger.
 */
export const DropdownMenuTrigger: React.FC<DropdownMenuTriggerProps> = ({ children, onClick }) => {
  return (
    <div onClick={onClick} className="dropdown-trigger">
      {children}
    </div>
  );
};

interface DropdownMenuContentProps {
  isOpen: boolean;
  children: React.ReactNode;
}

export const DropdownMenuContent: React.FC<DropdownMenuContentProps> = ({ isOpen, children }) => {
  return isOpen ? (
    <div className="dropdown-content">
      {children}
    </div>
  ) : null;
};

interface DropdownMenuItemProps {
  onClick: () => void;
  children: React.ReactNode;
}

export const DropdownMenuItem: React.FC<DropdownMenuItemProps> = ({ onClick, children }) => {
  return (
    <div className="dropdown-item" onClick={onClick}>
      {children}
    </div>
  );
};