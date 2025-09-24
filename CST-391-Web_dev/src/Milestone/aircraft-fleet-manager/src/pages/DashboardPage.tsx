import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PlaneTakeoff, Wrench, LineChart, PlaneLanding, AlertTriangle, Clock, Plane } from 'lucide-react';
import { Card, CardContent } from "@/components/ui/card";
import { aircraftService } from '@/services/aircraft.service';
import { Aircraft } from '@/types';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

/**
 * DashboardPage component displays the main dashboard of the Aircraft Maintenance Management System.
 * It shows statistics about the aircraft fleet, including total aircraft, maintenance required, and total flight hours.
 * It also provides navigation options to view aircraft details, maintenance records, and performance analytics.
 *
 * @component
 * @returns {JSX.Element} The rendered component.
 *
 * @example
 * <DashboardPage />
 *
 * @remarks
 * This component uses several hooks:
 * - `useNavigate` for navigation.
 * - `useState` for managing state.
 * - `useEffect` for loading dashboard data on component mount.
 *
 * The component fetches data from `aircraftService` to populate the dashboard statistics and aircraft list.
 *
 * @function
 * @name DashboardPage
 *
 * @typedef {Object} Stats
 * @property {number} totalAircraft - The total number of aircraft.
 * @property {number} maintenanceRequired - The number of aircraft requiring maintenance.
 * @property {number} totalFlightHours - The total flight hours of all aircraft.
 *
 * @typedef {Object} Aircraft
 * @property {number} aircraftID - The unique identifier of the aircraft.
 * @property {string} model - The model of the aircraft.
 * @property {string} maintenanceStatus - The maintenance status of the aircraft.
 *
 * @typedef {Object} PerformanceRecord
 * @property {number} FlightTime - The flight time of the aircraft.
 *
 * @typedef {Object} Error
 * @property {string} message - The error message.
 *
 * @function
 * @name loadDashboardData
 * @description Fetches the aircraft and performance data, calculates statistics, and updates the state.
 * @returns {Promise<void>} A promise that resolves when the data is loaded.
 *
 * @function
 * @name handleMaintenanceClick
 * @description Navigates to the maintenance page of the selected aircraft.
 * @param {number} aircraftID - The ID of the selected aircraft.
 *
 * @function
 * @name handlePerformanceClick
 * @description Navigates to the performance page of the selected aircraft.
 * @param {number} aircraftID - The ID of the selected aircraft.
 *
 * @function
 * @name handleAircraftListClick
 * @description Navigates to the aircraft list page.
 */
export default function DashboardPage() {
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    totalAircraft: 0,
    maintenanceRequired: 0,
    totalFlightHours: 0
  });
  const [aircraft, setAircraft] = useState<Aircraft[]>([]);
  const [maintenanceMenuOpen, setMaintenanceMenuOpen] = useState(false);
  const [performanceMenuOpen, setPerformanceMenuOpen] = useState(false);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const [aircraftData, performanceData] = await Promise.all([
        aircraftService.getAllAircraft(),
        aircraftService.getAllPerformanceRecords()
      ]);
      setAircraft(aircraftData);
      
      const totalAircraft = aircraftData.length;
      const maintenanceRequired = aircraftData.filter(a => 
        a.maintenanceStatus === 'DEFERRED' || a.maintenanceStatus === 'SCHEDULED'
      ).length;
      const totalFlightHours = performanceData.reduce((sum, p) => sum + (p.FlightTime || 0), 0);

      setStats({
        totalAircraft,
        maintenanceRequired,
        totalFlightHours
      });
    } catch (error) {
      console.error('Error loading dashboard data:', error);
    }
  };

  // Navigation handlers
  const handleMaintenanceClick = (aircraftID: number) => {
    navigate(`/aircraft/${aircraftID}/maintenance`);
    setMaintenanceMenuOpen(false);
  };

  const handlePerformanceClick = (aircraftID: number) => {
    navigate(`/aircraft/${aircraftID}/performance`);
    setPerformanceMenuOpen(false);
  };

  const handleAircraftListClick = () => {
    navigate('/aircraft');
  };

  return (
    <div className="min-h-screen bg-[#1a1a1a] p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-[#00BCD4] flex items-center gap-2">
            <PlaneTakeoff className="h-8 w-8" />
            Aircraft Maintenance Management System
          </h1>
          <p className="text-gray-400 mt-2">
            Monitor your fleet's performance, track maintenance schedules, and manage aircraft records all in one place.
          </p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Card className="bg-[#1e1e1e] border-gray-800">
            <CardContent className="p-6">
              <div className="flex flex-col items-center">
                <Plane className="h-12 w-12 text-blue-500 mb-3" />
                <span className="text-4xl font-bold text-blue-500">{stats.totalAircraft}</span>
                <span className="text-gray-400 mt-2">Total Aircraft</span>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-[#1e1e1e] border-gray-800">
            <CardContent className="p-6">
              <div className="flex flex-col items-center">
                <AlertTriangle className="h-12 w-12 text-red-500 mb-3" />
                <span className="text-4xl font-bold text-red-500">{stats.maintenanceRequired}</span>
                <span className="text-gray-400 mt-2">Maintenance Required</span>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-[#1e1e1e] border-gray-800">
            <CardContent className="p-6">
              <div className="flex flex-col items-center">
                <Clock className="h-12 w-12 text-green-500 mb-3" />
                <span className="text-4xl font-bold text-green-500">{stats.totalFlightHours}</span>
                <span className="text-gray-400 mt-2">Total Flight Hours</span>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Action Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card 
            className="bg-[#1e1e1e] border-gray-800 hover:bg-[#252525] transition-colors cursor-pointer"
            onClick={handleAircraftListClick}
          >
            <CardContent className="p-6">
              <div className="flex flex-col items-center">
                <Plane className="h-12 w-12 text-blue-500 mb-4" />
                <h3 className="text-xl font-semibold text-white mb-2">Aircraft Fleet</h3>
                <p className="text-gray-400 text-center">
                  Manage your aircraft inventory and view aircraft details
                </p>
              </div>
            </CardContent>
          </Card>

          <div className="relative">
            <DropdownMenu>
              <DropdownMenuTrigger onClick={() => setMaintenanceMenuOpen(!maintenanceMenuOpen)}>
                <Card className="bg-[#1e1e1e] border-gray-800 hover:bg-[#252525] transition-colors cursor-pointer w-full">
                  <CardContent className="p-6">
                    <div className="flex flex-col items-center">
                      <Wrench className="h-12 w-12 text-red-500 mb-4" />
                      <h3 className="text-xl font-semibold text-white mb-2">Maintenance Records</h3>
                      <p className="text-gray-400 text-center">
                        View and manage maintenance schedules and history
                      </p>
                    </div>
                  </CardContent>
                </Card>
              </DropdownMenuTrigger>
              <DropdownMenuContent isOpen={maintenanceMenuOpen}>
                {aircraft.map(a => (
                  <DropdownMenuItem
                    key={a.aircraftID}
                    onClick={() => handleMaintenanceClick(a.aircraftID)}
                  >
                    <div className="flex items-center gap-2 p-2 hover:bg-gray-700 w-full">
                      <Plane className="h-4 w-4" />
                      <span>{a.model}</span>
                    </div>
                  </DropdownMenuItem>
                ))}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>

          <div className="relative">
            <DropdownMenu>
              <DropdownMenuTrigger onClick={() => setPerformanceMenuOpen(!performanceMenuOpen)}>
                <Card className="bg-[#1e1e1e] border-gray-800 hover:bg-[#252525] transition-colors cursor-pointer w-full">
                  <CardContent className="p-6">
                    <div className="flex flex-col items-center">
                      <LineChart className="h-12 w-12 text-green-500 mb-4" />
                      <h3 className="text-xl font-semibold text-white mb-2">Performance Analytics</h3>
                      <p className="text-gray-400 text-center">
                        Track and analyze aircraft performance metrics
                      </p>
                    </div>
                  </CardContent>
                </Card>
              </DropdownMenuTrigger>
              <DropdownMenuContent isOpen={performanceMenuOpen}>
                {aircraft.map(a => (
                  <DropdownMenuItem
                    key={a.aircraftID}
                    onClick={() => handlePerformanceClick(a.aircraftID)}
                  >
                    <div className="flex items-center gap-2 p-2 hover:bg-gray-700 w-full">
                      <Plane className="h-4 w-4" />
                      <span>{a.model}</span>
                    </div>
                  </DropdownMenuItem>
                ))}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </div>
    </div>
  );
}