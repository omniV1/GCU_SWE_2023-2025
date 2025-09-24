import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Card } from "@/components/ui/card";
import { PerformanceChart } from '@/components/features/PerformanceChart';

/**
 * PerformanceAnalyticsPage component displays performance analytics for a specific aircraft.
 * It shows total flight hours, average fuel efficiency, and various performance charts.
 *
 * @component
 * @example
 * return (
 *   <PerformanceAnalyticsPage />
 * )
 *
 * @returns {JSX.Element} The rendered component.
 *
 * @remarks
 * This component uses the `useParams` hook to get the aircraft ID from the URL.
 * It maintains state for performance data and statistics using the `useState` hook.
 *
 * @function
 * @name PerformanceAnalyticsPage
 */
export default function PerformanceAnalyticsPage() {
  const { id } = useParams();
  const [data, setData] = useState([
    { id: 30, flightHours: 6, fuelConsumption: 4500 },
    { id: 31, flightHours: 2.1, fuelConsumption: 1430 },
    { id: 32, flightHours: 3, fuelConsumption: 2500 },
    { id: 33, flightHours: 4, fuelConsumption: 2833 },
    { id: 34, flightHours: 2, fuelConsumption: 1799 },
  ]);

  const [stats, setStats] = useState({
    totalFlightHours: '18.1',
    avgFuelEfficiency: '2,300.83'
  });

  return (
    <div className="min-h-screen bg-[#121212] p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-white">Performance Analytics - Aircraft {id}</h1>
          <div className="grid grid-cols-2 gap-4 mt-4">
            <div className="bg-[#1e1e1e] p-4 rounded-lg">
              <span className="text-gray-400">Total Flight Hours</span>
              <div className="text-2xl font-bold text-blue-500">{stats.totalFlightHours}</div>
            </div>
            <div className="bg-[#1e1e1e] p-4 rounded-lg">
              <span className="text-gray-400">Avg Fuel Efficiency</span>
              <div className="text-2xl font-bold text-green-500">{stats.avgFuelEfficiency} gal/hr</div>
            </div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <PerformanceChart
            title="Performance History"
            description="Track flight hours and fuel consumption trends over time. Higher values indicate longer flights or increased fuel usage."
            data={data}
            lines={[
              { key: 'flightHours', name: 'Flight Hours', color: '#3b82f6' },
              { key: 'fuelConsumption', name: 'Fuel Consumption', color: '#22c55e' }
            ]}
          />

          <PerformanceChart
            title="Recent Activity Analysis"
            description="Compare flight duration and fuel efficiency for the last 5 records. Fuel efficiency is scaled (×10) for better comparison with flight hours."
            data={data}
            lines={[
              { key: 'flightHours', name: 'Flight Duration', color: '#3b82f6' },
              { key: 'fuelConsumption', name: 'Fuel Efficiency', color: '#22c55e' }
            ]}
          />

          {/* Real-Time Fuel Consumption */}
          <Card className="bg-[#1e1e1e] p-4 col-span-1">
            <h3 className="text-white text-lg font-semibold mb-4">Real-Time Fuel Consumption</h3>
            <p className="text-sm text-gray-400 mb-4">Current fuel consumption rate in gallons per hour. The gauge shows the latest recorded value relative to the maximum observed rate.</p>
            <div className="flex items-center justify-center h-[300px]">
              <div className="text-center">
                <div className="text-5xl font-bold text-green-500">573</div>
                <div className="text-gray-400 mt-2">gal/hr</div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}