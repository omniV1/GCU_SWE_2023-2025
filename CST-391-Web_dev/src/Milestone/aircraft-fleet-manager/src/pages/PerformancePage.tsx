import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { LineChart, PencilLine, Trash2 } from 'lucide-react';
import { PerformanceMetric } from '@/types/performance';
import { aircraftService } from '@/services/aircraft.service';
import { toast } from '@/components/ui/use-toast';
import { PerformanceMetricDialog } from '@/components/features/PerformanceMetricDialog';
import { AlertDialog, AlertDialogContent, AlertDialogHeader, AlertDialogTitle, 
         AlertDialogDescription, AlertDialogFooter, AlertDialogCancel, AlertDialogAction } from "@/components/ui/alert-dialog";

/**
 * PerformancePage component is responsible for displaying and managing performance metrics
 * for a specific aircraft. It allows users to view, add, edit, and delete performance records.
 * 
 * @component
 * 
 * @returns {JSX.Element} The rendered component.
 * 
 * @example
 * <PerformancePage />
 * 
 * @remarks
 * This component uses several hooks and services:
 * - `useNavigate` from `react-router-dom` for navigation.
 * - `useParams` from `react-router-dom` to get the aircraft ID from the URL.
 * - `useState` and `useEffect` from `react` for state management and side effects.
 * - `aircraftService` for API calls to manage performance records.
 * - `toast` for displaying notifications.
 * 
 * @function
 * @name PerformancePage
 * 
 * @typedef {Object} PerformanceMetric
 * @property {number} MetricID - The unique identifier for the performance metric.
 * @property {number} FlightTime - The flight time in hours.
 * @property {number} OilConsumption - The oil consumption in liters.
 * @property {number} FuelConsumption - The fuel consumption in gallons per hour.
 * 
 * @typedef {Object} FormData
 * @property {number} FlightTime - The flight time in hours.
 * @property {number} OilConsumption - The oil consumption in liters.
 * @property {number} FuelConsumption - The fuel consumption in gallons per hour.
 * 
 * @function
 * @name loadPerformanceMetrics
 * @description Loads performance metrics for a specific aircraft.
 * @param {number} aircraftId - The ID of the aircraft.
 * 
 * @function
 * @name handleViewAnalytics
 * @description Navigates to the performance analytics page for the current aircraft.
 * 
 * @function
 * @name handleAddRecord
 * @description Adds a new performance record for the current aircraft.
 * @param {FormData} formData - The data for the new performance record.
 * 
 * @function
 * @name handleEditRecord
 * @description Edits an existing performance record for the current aircraft.
 * @param {FormData} formData - The updated data for the performance record.
 * 
 * @function
 * @name handleDeleteRecord
 * @description Deletes a performance record for the current aircraft.
 * @param {PerformanceMetric} record - The performance record to delete.
 * 
 * @hook
 * @name useEffect
 * @description Loads performance metrics when the component mounts or the aircraft ID changes.
 * 
 * @hook
 * @name useState
 * @description Manages the state for performance metrics, loading status, dialogs, and editing/deleting records.
 */
export default function PerformancePage() {
  const navigate = useNavigate();
  const { id } = useParams<{ id: string }>();
  const [performanceMetrics, setPerformanceMetrics] = useState<PerformanceMetric[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddDialog, setShowAddDialog] = useState(false);
  const [editingRecord, setEditingRecord] = useState<PerformanceMetric | null>(null);
  const [recordToDelete, setRecordToDelete] = useState<PerformanceMetric | null>(null);

  useEffect(() => {
    if (id) {
      loadPerformanceMetrics(parseInt(id));
    }
  }, [id]);

  const loadPerformanceMetrics = async (aircraftId: number) => {
    try {
      setLoading(true);
      const data = await aircraftService.getPerformanceRecords(aircraftId);
      setPerformanceMetrics(data);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load performance metrics",
        variant: "destructive"
      });
    } finally {
      setLoading(false);
    }
  };

  const handleViewAnalytics = () => {
    if (id) {
      navigate(`/aircraft/${id}/performance/analytics`);
    }
  };

  const handleAddRecord = async (formData: Omit<PerformanceMetric, 'MetricID'>) => {
    if (!id) return;
    try {
      await aircraftService.createPerformanceRecord(parseInt(id), formData);
      await loadPerformanceMetrics(parseInt(id));
      toast({
        title: "Success",
        description: "Performance record added successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to add performance record",
        variant: "destructive"
      });
    }
  };

  const handleEditRecord = async (formData: Omit<PerformanceMetric, 'MetricID'>) => {
    if (!editingRecord?.MetricID || !id) return;
    try {
      await aircraftService.updatePerformanceRecord(parseInt(id), {
        ...formData,
        MetricID: editingRecord.MetricID,
      });
      await loadPerformanceMetrics(parseInt(id));
      setEditingRecord(null);
      toast({
        title: "Success",
        description: "Performance record updated successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to update performance record",
        variant: "destructive"
      });
    }
  };

  const handleDeleteRecord = async (record: PerformanceMetric) => {
    if (!id) return;
    try {
      await aircraftService.deletePerformanceRecord(parseInt(id), record.MetricID);
      await loadPerformanceMetrics(parseInt(id));
      toast({
        title: "Success",
        description: "Performance record deleted successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to delete performance record",
        variant: "destructive"
      });
    }
  };

  if (loading) {
    return <div className="flex items-center justify-center h-64 text-white">Loading...</div>;
  }

  return (
    <div className="p-6 bg-background text-white">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Performance Metrics - Aircraft {id}</h1>
        <div className="flex space-x-4">
          <Button 
            onClick={handleViewAnalytics}
            variant="secondary"
            className="flex items-center gap-2"
          >
            <LineChart className="h-4 w-4" />
            View Analytics
          </Button>
          <Button onClick={() => setShowAddDialog(true)}>
            Add Record
          </Button>
        </div>
      </div>

      <div className="mb-6 space-y-4">
        <Input 
          placeholder="Filter..." 
          className="bg-[#1e1e1e] border-input text-white"
        />
      </div>

      <div className="rounded-md border border-input">
      <table className="w-full">
  <thead>
    <tr className="border-b bg-muted/50">
      <th className="p-4 text-left font-medium text-white">Metric ID</th>
      <th className="p-4 text-left font-medium text-white">Flight Time (hrs)</th>
      <th className="p-4 text-left font-medium text-white">Oil Consumption (L)</th>
      <th className="p-4 text-left font-medium text-white">Fuel Consumption (gal/hr)</th>
      <th className="p-4 text-left font-medium text-white">Actions</th>
    </tr>
  </thead>
  <tbody>
    {performanceMetrics.map((metric) => (
      <tr key={metric.MetricID} className="border-b border-input">
        <td className="p-4 text-white">{metric.MetricID}</td>
        <td className="p-4 text-white">{metric.FlightTime} hrs</td>
        <td className="p-4 text-white">{metric.OilConsumption} L</td>
        <td className="p-4 text-white">{metric.FuelConsumption} gal/hr</td>
        <td className="p-4">
                  <div className="flex space-x-2">
                    <Button 
                      variant="ghost" 
                      size="sm"
                      onClick={() => setEditingRecord(metric)}
                    >
                      <PencilLine className="h-4 w-4 text-white" />
                    </Button>
                    <Button 
                      variant="ghost" 
                      size="sm" 
                      className="text-red-400"
                      onClick={() => setRecordToDelete(metric)}
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

      <PerformanceMetricDialog
        open={showAddDialog}
        onOpenChange={setShowAddDialog}
        onSubmit={handleAddRecord}
        mode="add"
      />

      {editingRecord && (
        <PerformanceMetricDialog
          open={true}
          onOpenChange={() => setEditingRecord(null)}
          onSubmit={handleEditRecord}
          initialData={editingRecord}
          mode="edit"
        />
      )}

      <AlertDialog 
        open={!!recordToDelete} 
        onOpenChange={(open) => !open && setRecordToDelete(null)}
      >
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Delete Performance Record</AlertDialogTitle>
            <AlertDialogDescription>
              Are you sure you want to delete this performance record? 
              This action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction
              onClick={() => {
                if (recordToDelete) {
                  handleDeleteRecord(recordToDelete);
                  setRecordToDelete(null);
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
  );
}