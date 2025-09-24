import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { LineChart, Wrench, PencilLine, Trash2 } from 'lucide-react';
import { Aircraft } from '@/types';
import { aircraftService } from '@/services/aircraft.service';
import { toast } from '@/components/ui/use-toast';
import { AircraftFormDialog } from '@/components/features/AircraftFormDialog';
import { AlertDialog, AlertDialogContent, AlertDialogHeader, AlertDialogTitle, 
  AlertDialogDescription, AlertDialogFooter, AlertDialogCancel, AlertDialogAction 
} from "@/components/ui/alert-dialog";


/**
 * AircraftListPage component is responsible for displaying and managing a list of aircraft.
 * It provides functionalities to filter, add, edit, and delete aircraft.
 * 
 * @component
 * 
 * @returns {JSX.Element} The rendered component.
 * 
 * @example
 * <AircraftListPage />
 * 
 * @remarks
 * This component uses several hooks and services:
 * - `useNavigate` for navigation.
 * - `useState` for managing component state.
 * - `useEffect` for loading aircraft data on component mount.
 * - `aircraftService` for interacting with the backend API.
 * - `toast` for displaying notifications.
 * 
 * @function loadAircraft
 * Fetches the list of aircraft from the backend and updates the state.
 * 
 * @function handleFilterClick
 * Sets the filter state to the selected aircraft model.
 * 
 * @function clearFilter
 * Clears the current filter.
 * 
 * @function getStatusClass
 * Returns the CSS class for the aircraft status.
 * 
 * @function getMaintenanceStatusClass
 * Returns the CSS class for the maintenance status.
 * 
 * @function formatDate
 * Formats a date string or object to a locale date string.
 * 
 * @function handleAddAircraft
 * Handles the addition of a new aircraft.
 * 
 * @function handleEditAircraft
 * Handles the editing of an existing aircraft.
 * 
 * @function handleDeleteAircraft
 * Handles the deletion of an aircraft.
 * 
 * @state {Aircraft[]} aircraft - The list of aircraft.
 * @state {boolean} loading - Indicates if the data is being loaded.
 * @state {string} filter - The current filter string.
 * @state {boolean} showAddDialog - Controls the visibility of the add aircraft dialog.
 * @state {Aircraft | null} editingAircraft - The aircraft being edited.
 * @state {Aircraft | null} aircraftToDelete - The aircraft being deleted.
 */
export default function AircraftListPage() {
  const navigate = useNavigate();
  const [aircraft, setAircraft] = useState<Aircraft[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('');
  const [showAddDialog, setShowAddDialog] = useState(false);
  const [editingAircraft, setEditingAircraft] = useState<Aircraft | null>(null);
  const [aircraftToDelete, setAircraftToDelete] = useState<Aircraft | null>(null);

  useEffect(() => {
    loadAircraft();
  }, []);

  const loadAircraft = async () => {
    try {
      setLoading(true);
      const data = await aircraftService.getAllAircraft();
      setAircraft(data);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load aircraft data",
        variant: "destructive"
      });
    } finally {
      setLoading(false);
    }
  };

  const filteredAircraft = aircraft.filter(item => 
    (item.model?.toLowerCase() || '').includes(filter.toLowerCase()) ||
    (item.serialNumber?.toLowerCase() || '').includes(filter.toLowerCase())
  );

  // Get unique aircraft models for filter buttons, handling null values
  const uniqueModels = Array.from(new Set(aircraft
    .map(item => item.model)
    .filter((model): model is string => model != null) // Type guard to remove null/undefined
  ));

  const handleFilterClick = (model: string) => {
    setFilter(model);
  };

  const clearFilter = () => {
    setFilter('');
  };

  const getStatusClass = (status: string | null | undefined) => {
    switch (status?.toLowerCase()) {
      case 'ready':
        return 'bg-green-500/20 text-green-500';
      case 'not ready':
        return 'bg-red-500/20 text-red-500';
      case 'in maintenance':
        return 'bg-yellow-500/20 text-yellow-500';
      default:
        return 'bg-gray-500/20 text-gray-500';
    }
  };

  const getMaintenanceStatusClass = (status: string | null | undefined) => {
    switch (status) {
      case 'COMPLETED':
        return 'text-green-400';
      case 'IN_PROGRESS':
        return 'text-blue-400';
      case 'SCHEDULED':
        return 'text-yellow-400';
      case 'DEFERRED':
        return 'text-red-400';
      default:
        return 'text-gray-400';
    }
  };

  const formatDate = (date: Date | string | null | undefined) => {
    if (!date) return 'N/A';
    return new Date(date).toLocaleDateString();
  };

  const handleAddAircraft = async (formData: any) => {
    try {
      await aircraftService.createAircraft(formData);
      loadAircraft();
      toast({
        title: "Success",
        description: "Aircraft added successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to add aircraft",
        variant: "destructive"
      });
    }
  };
  
  const handleEditAircraft = async (formData: any) => {
    if (!editingAircraft?.aircraftID) return;
    
    try {
      await aircraftService.updateAircraft(editingAircraft.aircraftID, formData);
      loadAircraft();
      setEditingAircraft(null);
      toast({
        title: "Success",
        description: "Aircraft updated successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to update aircraft",
        variant: "destructive"
      });
    }
  };
  
  if (loading) {
    return <div className="flex items-center justify-center h-64">Loading...</div>;
  }

  const handleDeleteAircraft = async (aircraft: Aircraft) => {
    try {
      await aircraftService.deleteAircraft(aircraft.aircraftID);
      await loadAircraft();
      toast({
        title: "Success",
        description: "Aircraft deleted successfully"
      });
    } catch (error) {
      console.error('Error deleting aircraft:', error);
      toast({
        title: "Error",
        description: "Failed to delete aircraft",
        variant: "destructive"
      });
    }
  };

  return (
    <div className="p-6 bg-background">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Aircraft Fleet Management</h1>
        <Button onClick={() => setShowAddDialog(true)}>
        Add Aircraft
        </Button>
      </div>

      <div className="mb-6 space-y-4">
        <Input 
          placeholder="Filter..." 
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="bg-[#1e1e1e] border-input"
        />
        
        <div className="flex flex-wrap gap-2">
          <Button
            variant={filter === '' ? 'default' : 'outline'}
            onClick={clearFilter}
          >
            ALL
          </Button>
          {uniqueModels.map((model) => (
            <Button
              key={model}
              variant={filter === model ? 'default' : 'outline'}
              onClick={() => handleFilterClick(model)}
            >
              {model}
            </Button>
          ))}
        </div>
      </div>

      <div className="rounded-md border border-input">
        <table className="w-full">
          <thead>
            <tr className="border-b bg-muted/50">
              <th className="p-4 text-left font-medium">Model</th>
              <th className="p-4 text-left font-medium">Serial Number</th>
              <th className="p-4 text-left font-medium">Last Maintenance</th>
              <th className="p-4 text-left font-medium">Maintenance Status</th>
              <th className="p-4 text-left font-medium">Status</th>
              <th className="p-4 text-left font-medium">Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredAircraft.map((item) => (
              <tr key={item.aircraftID} className="border-b border-input">
                <td className="p-4">{item.model || 'N/A'}</td>
                <td className="p-4">{item.serialNumber || 'N/A'}</td>
                <td className="p-4">{formatDate(item.lastMaintenanceDate)}</td>
                <td className="p-4">
                  <span className={`px-2 py-1 rounded-full text-sm ${getMaintenanceStatusClass(item.maintenanceStatus)}`}>
                    {item.maintenanceStatus || 'N/A'}
                  </span>
                </td>
                <td className="p-4">
                  <span className={`px-2 py-1 rounded-full text-sm ${getStatusClass(item.status)}`}>
                    {item.status?.toLowerCase() || 'unknown'}
                  </span>
                </td>
                <td className="p-4">
                  <div className="flex space-x-2">
                    <Button 
                      variant="ghost" 
                      size="sm"
                      onClick={() => navigate(`/aircraft/${item.aircraftID}/performance`)}
                    >
                      <LineChart className="h-4 w-4" />
                    </Button>
                    <Button 
                      variant="ghost" 
                      size="sm"
                      onClick={() => navigate(`/aircraft/${item.aircraftID}/maintenance`)}
                    >
                      <Wrench className="h-4 w-4" />
                    </Button>
                    <Button 
  variant="ghost" 
  size="sm"
  onClick={() => setEditingAircraft(item)}
>
  <PencilLine className="h-4 w-4" />
</Button>
<Button 
                    variant="ghost" 
                    size="sm" 
                    className="text-red-400"
                    onClick={() => setAircraftToDelete(item)}
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>

    {/* Dialogs go here, AFTER the table */}
    <AircraftFormDialog
      open={showAddDialog}
      onOpenChange={setShowAddDialog}
      onSubmit={handleAddAircraft}
      mode="add"
    />

    {editingAircraft && (
      <AircraftFormDialog
        open={true}
        onOpenChange={() => setEditingAircraft(null)}
        onSubmit={handleEditAircraft}
        initialData={editingAircraft}
        mode="edit"
      />
    )}

    <AlertDialog 
      open={!!aircraftToDelete} 
      onOpenChange={(open) => !open && setAircraftToDelete(null)}
    >
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Delete Aircraft</AlertDialogTitle>
          <AlertDialogDescription>
            Are you sure you want to delete {aircraftToDelete?.model} ({aircraftToDelete?.serialNumber})?
            This action cannot be undone.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction
            onClick={() => {
              if (aircraftToDelete) {
                handleDeleteAircraft(aircraftToDelete);
                setAircraftToDelete(null);
              }
            }}
            className="bg-red-600 hover:bg-red-700"
          >
            Delete
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  </div>
  ); }