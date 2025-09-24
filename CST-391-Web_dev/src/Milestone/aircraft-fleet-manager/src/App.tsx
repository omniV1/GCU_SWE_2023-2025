import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RootLayout from './components/layout/RootLayout';
import DashboardPage from './pages/DashboardPage';
import AircraftListPage from './pages/AircraftListPage';
import MaintenancePage from './pages/MaintenancePage';
import PerformancePage from './pages/PerformancePage';
import { Toaster } from './components/ui/toaster'; 
import PerformanceAnalyticsPage from './pages/PerformanceAnalyticsPage';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      {
        index: true,
        element: <DashboardPage />,
      },
      {
        path: 'aircraft',
        element: <AircraftListPage />,
      },
      {
        path: 'aircraft/:id/maintenance',
        element: <MaintenancePage />,
      },
      {
        path: 'aircraft/:id/performance',
        element: <PerformancePage />,
      },
      {
        path: 'aircraft/:id/performance/analytics',
        element: <PerformanceAnalyticsPage />,
      },
    ],
  },
]);

export default function App() {
  return (
    <>
      <RouterProvider router={router} />
      <Toaster />  { }
    </>
  );
}