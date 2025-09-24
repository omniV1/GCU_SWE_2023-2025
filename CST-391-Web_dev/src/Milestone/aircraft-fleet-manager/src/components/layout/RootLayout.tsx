import { Link, Outlet } from 'react-router-dom';
import { LayoutGrid, Plane } from 'lucide-react';

/**
 * RootLayout component serves as the main layout for the application.
 * It includes a header with the title "Aircraft Manager" and a navigation bar
 * with links to the Dashboard and Aircraft Fleet pages.
 * 
 * @returns {JSX.Element} The RootLayout component.
 * 
 * @component
 * @example
 * return (
 *   <RootLayout />
 * )
 */
export default function RootLayout() {
  return (
    <div className="min-h-screen bg-[#1E1E1E]">
      <div className="p-6 max-w-[1200px] mx-auto">
        <h1 className="text-4xl font-bold mb-4">Aircraft Manager</h1>
        <nav className="flex space-x-4 mb-8">
          <Link 
            to="/" 
            className="flex items-center text-[#646cff] hover:text-[#535bf2]"
          >
            <LayoutGrid className="w-4 h-4 mr-2" />
            Dashboard
          </Link>
          <Link 
            to="/aircraft" 
            className="flex items-center text-[#646cff] hover:text-[#535bf2]"
          >
            <Plane className="w-4 h-4 mr-2" />
            Aircraft Fleet
          </Link>
        </nav>
        <main>
          <Outlet />
        </main>
      </div>
    </div>
  );
}