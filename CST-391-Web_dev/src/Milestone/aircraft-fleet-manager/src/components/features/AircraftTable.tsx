import { useState, useEffect } from 'react';
import { Table } from '../ui/table';
import { Button } from '../ui/button';

import { Activity, Wrench, PencilLine, Trash2 } from 'lucide-react';
import { useToast } from '../ui/use-toast';
import apiClient from '../../api/client';

interface Aircraft {
  aircraftID: number;
  model: string | null;
  serialNumber: string | null;
  DateOfManufacture: string;  // Changed to match API response
  flightTime: number | null;
  engineHours: number | null;
  status: string | null;  // Changed to allow null
}

/**
 * AircraftTable component fetches and displays a list of aircraft in a table format.
 * 
 * @component
 * 
 * @returns {JSX.Element} The rendered component.
 * 
 * @example
 * <AircraftTable />
 * 
 * @remarks
 * - The component fetches aircraft data from an API endpoint and displays it in a table.
 * - It includes a loading state while the data is being fetched.
 * - The table includes columns for model, serial number, flight hours, engine hours, status, and actions.
 * - The status column is color-coded based on the aircraft's status.
 * - The actions column includes buttons for various actions (e.g., view activity, maintenance, edit, delete).
 * 
 * @function
 * @name AircraftTable
 * 
 * @typedef {Object} Aircraft
 * @property {number} aircraftID - The unique identifier for the aircraft.
 * @property {string} model - The model of the aircraft.
 * @property {string} serialNumber - The serial number of the aircraft.
 * @property {number} flightTime - The total flight hours of the aircraft.
 * @property {number} engineHours - The total engine hours of the aircraft.
 * @property {string | null} status - The current status of the aircraft (e.g., 'ready', 'not ready', 'in maintenance').
 * 
 * @hook
 * @name useState
 * @description Manages the state of the aircraft data, loading state, and filter.
 * 
 * @hook
 * @name useEffect
 * @description Fetches the aircraft data when the component mounts.
 * 
 * @function
 * @name fetchAircraft
 * @description Fetches aircraft data from the API and updates the state.
 * 
 * @function
 * @name getStatusColor
 * @description Returns the appropriate CSS classes for the status badge based on the aircraft's status.
 * 
 * @constant
 * @name filteredAircraft
 * @description Filters the aircraft data based on the filter state.
 */
export default function AircraftTable() {
  const [aircraft, setAircraft] = useState<Aircraft[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter] = useState('');
  const { toast } = useToast();

  useEffect(() => {
    console.log('Component mounted, fetching aircraft');
    fetchAircraft();
  }, []);

  const fetchAircraft = async () => {
    try {
      console.log('Fetching aircraft data...');
      const response = await apiClient.get<Aircraft[]>('/aircraft');
      console.log('Aircraft data received:', response.data);
      setAircraft(response.data);
    } catch (error) {
      console.error('Error fetching aircraft:', error);
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : 'Failed to fetch aircraft data',
        variant: "destructive"
      });
    } finally {
      setLoading(false);
    }
  };

  const getStatusColor = (status: string | null) => {
    if (!status) return 'bg-gray-500/20 text-gray-500';
    
    switch (status.toLowerCase()) {
      case 'ready': return 'bg-green-500/20 text-green-500';
      case 'not ready': return 'bg-red-500/20 text-red-500';
      case 'in maintenance': return 'bg-yellow-500/20 text-yellow-500';
      default: return 'bg-gray-500/20 text-gray-500';
    }
  };

  const filteredAircraft = aircraft.filter(item =>
    (item.model?.toLowerCase() || '').includes(filter.toLowerCase()) ||
    (item.serialNumber?.toLowerCase() || '').includes(filter.toLowerCase())
  );

  if (loading) {
    return <div className="p-4 text-white">Loading...</div>;
  }

  return (
    <div className="rounded-md border border-gray-800 overflow-hidden">
      <Table>
        <thead className="bg-[#1e1e1e]">
          <tr>
            <th className="text-left p-4 text-gray-400">Model</th>
            <th className="text-left p-4 text-gray-400">Serial Number</th>
            <th className="text-left p-4 text-gray-400">Flight Hours</th>
            <th className="text-left p-4 text-gray-400">Engine Hours</th>
            <th className="text-left p-4 text-gray-400">Status</th>
            <th className="text-right p-4 text-gray-400">Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredAircraft.map((item) => (
            <tr key={item.aircraftID} className="border-t border-gray-800 hover:bg-[#1e1e1e]">
              <td className="p-4 text-white">{item.model || 'N/A'}</td>
              <td className="p-4 text-white">{item.serialNumber || 'N/A'}</td>
              <td className="p-4 text-white">{item.flightTime || 0}</td>
              <td className="p-4 text-white">{item.engineHours || 0}</td>
              <td className="p-4">
                <span className={`px-2 py-1 rounded-full text-xs ${getStatusColor(item.status)}`}>
                  {item.status || 'Unknown'}
                </span>
              </td>
              <td className="p-4">
                <div className="flex justify-end gap-2">
                  <Button variant="ghost" size="sm">
                    <Activity className="w-4 h-4" />
                  </Button>
                  <Button variant="ghost" size="sm">
                    <Wrench className="w-4 h-4" />
                  </Button>
                  <Button variant="ghost" size="sm">
                    <PencilLine className="w-4 h-4" />
                  </Button>
                  <Button variant="ghost" size="sm" className="text-red-500">
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}