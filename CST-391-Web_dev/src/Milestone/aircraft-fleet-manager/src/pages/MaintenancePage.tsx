import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { PencilLine, Trash2 } from 'lucide-react';
import { MaintenanceRecord, MaintenanceCategory } from '@/types';
import { aircraftService } from '@/services/aircraft.service';
import { toast } from '@/components/ui/use-toast';
import { MaintenanceRecordDialog } from '@/components/features/MaintenanceRecordDialog';
import { AlertDialog, AlertDialogContent, AlertDialogHeader, AlertDialogTitle, 
         AlertDialogDescription, AlertDialogFooter, AlertDialogCancel, AlertDialogAction } from "@/components/ui/alert-dialog";

/**
 * MaintenancePage component is responsible for displaying and managing the maintenance records of a specific aircraft.
 * It allows users to view, add, edit, and delete maintenance records.
 *
 * @component
 * @returns {JSX.Element} The rendered MaintenancePage component.
 *
 * @example
 * <MaintenancePage />
 *
 * @remarks
 * This component uses the `useParams` hook to get the aircraft ID from the URL parameters.
 * It fetches the maintenance records for the specified aircraft and displays them in a table.
 * Users can filter records by category, add new records, edit existing records, and delete records.
 *
 * @function
 * @name MaintenancePage
 *
 * @typedef {Object} MaintenanceRecord
 * @property {number} MaintenanceID - The unique identifier for the maintenance record.
 * @property {string} MaintenanceDate - The date of the maintenance.
 * @property {string} maintenanceType - The type of maintenance performed.
 * @property {string} maintenanceCategory - The category of maintenance.
 * @property {string} maintenanceStatus - The status of the maintenance (e.g., IN_PROGRESS, COMPLETED, SCHEDULED).
 * @property {string} Details - Additional details about the maintenance.
 * @property {string} Technician - The name of the technician who performed the maintenance.
 * @property {string} nextDueDate - The next due date for the maintenance.
 *
 * @typedef {Object} MaintenanceCategory
 * @property {string} category - The category of maintenance.
 *
 * @typedef {Object} ToastOptions
 * @property {string} title - The title of the toast message.
 * @property {string} description - The description of the toast message.
 * @property {string} [variant] - The variant of the toast message (e.g., destructive).
 *
 * @typedef {Object} ButtonProps
 * @property {string} variant - The variant of the button (e.g., default, outline, ghost).
 * @property {string} size - The size of the button (e.g., sm).
 * @property {Function} onClick - The function to call when the button is clicked.
 *
 * @typedef {Object} MaintenanceRecordDialogProps
 * @property {boolean} open - Whether the dialog is open.
 * @property {Function} onOpenChange - The function to call when the dialog's open state changes.
 * @property {Function} onSubmit - The function to call when the form is submitted.
 * @property {string} mode - The mode of the dialog (e.g., add, edit).
 * @property {MaintenanceRecord} [initialData] - The initial data for the form in edit mode.
 *
 * @typedef {Object} AlertDialogProps
 * @property {boolean} open - Whether the alert dialog is open.
 * @property {Function} onOpenChange - The function to call when the alert dialog's open state changes.
 *
 * @typedef {Object} AlertDialogContentProps
 * @property {React.ReactNode} children - The content of the alert dialog.
 *
 * @typedef {Object} AlertDialogHeaderProps
 * @property {React.ReactNode} children - The header content of the alert dialog.
 *
 * @typedef {Object} AlertDialogTitleProps
 * @property {React.ReactNode} children - The title content of the alert dialog.
 *
 * @typedef {Object} AlertDialogDescriptionProps
 * @property {React.ReactNode} children - The description content of the alert dialog.
 *
 * @typedef {Object} AlertDialogFooterProps
 * @property {React.ReactNode} children - The footer content of the alert dialog.
 *
 * @typedef {Object} AlertDialogCancelProps
 * @property {React.ReactNode} children - The cancel button content of the alert dialog.
 *
 * @typedef {Object} AlertDialogActionProps
 * @property {Function} onClick - The function to call when the action button is clicked.
 * @property {string} className - The class name for the action button.
 *
 * @typedef {Object} InputProps
 * @property {string} placeholder - The placeholder text for the input.
 * @property {string} className - The class name for the input.
 */
export default function MaintenancePage() {
  const { id } = useParams();
  const [records, setRecords] = useState<MaintenanceRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddDialog, setShowAddDialog] = useState(false);
  const [editingRecord, setEditingRecord] = useState<MaintenanceRecord | null>(null);
  const [recordToDelete, setRecordToDelete] = useState<MaintenanceRecord | null>(null);
  const [selectedCategory, setSelectedCategory] = useState<'ALL' | MaintenanceCategory>('ALL');

  const loadMaintenanceRecords = async (aircraftId: number) => {
    try {
      setLoading(true);
      const data = await aircraftService.getMaintenanceHistory(aircraftId);
      setRecords(data);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load maintenance records",
        variant: "destructive"
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (id) {
      loadMaintenanceRecords(parseInt(id));
    }
  }, [id]);

  const handleAddRecord = async (formData: any) => {
    if (!id) return;
    try {
      await aircraftService.createMaintenanceRecord(parseInt(id), {
        ...formData,
        AircraftID: parseInt(id)
      });
      await loadMaintenanceRecords(parseInt(id));
      toast({
        title: "Success",
        description: "Maintenance record added successfully"
      });
    } catch (error) {
      console.error('Error adding maintenance record:', error);
      toast({
        title: "Error",
        description: "Failed to add maintenance record",
        variant: "destructive"
      });
    }
  };

  const handleEditRecord = async (formData: any) => {
    if (!editingRecord?.MaintenanceID || !id) return;
    try {
      await aircraftService.updateMaintenanceRecord(parseInt(id), {
        ...formData,
        MaintenanceID: editingRecord.MaintenanceID,
        AircraftID: parseInt(id)
      });
      await loadMaintenanceRecords(parseInt(id));
      setEditingRecord(null);
      toast({
        title: "Success",
        description: "Maintenance record updated successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to update maintenance record",
        variant: "destructive"
      });
    }
  };

  const handleDeleteRecord = async (record: MaintenanceRecord) => {
    if (!id) return;
    try {
      await aircraftService.deleteMaintenanceRecord(parseInt(id), record.MaintenanceID);
      await loadMaintenanceRecords(parseInt(id));
      toast({
        title: "Success",
        description: "Maintenance record deleted successfully"
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to delete maintenance record",
        variant: "destructive"
      });
    }
  };

  const filteredRecords = selectedCategory === 'ALL' 
    ? records 
    : records.filter(record => record.maintenanceCategory === selectedCategory);

  if (loading) {
    return <div className="flex items-center justify-center h-64">Loading...</div>;
  }

  return (
    <div className="p-6 bg-background">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Maintenance History - Aircraft {id}</h1>
        <Button onClick={() => setShowAddDialog(true)}>
          Add Record
        </Button>
      </div>

      <div className="mb-6 space-y-4">
        <Input 
          placeholder="Filter..." 
          className="bg-[#1e1e1e] border-input"
        />
        
        <div className="flex flex-wrap gap-2">
          <Button
            variant={selectedCategory === 'ALL' ? 'default' : 'outline'}
            onClick={() => setSelectedCategory('ALL')}
          >
            ALL
          </Button>
          {Object.values(MaintenanceCategory).map((category) => (
            <Button
              key={category}
              variant={selectedCategory === category ? 'default' : 'outline'}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </Button>
          ))}
        </div>
      </div>
      <div className="rounded-md border border-input">
      <table className="w-full">
  <thead>
    <tr className="border-b bg-muted/50">
      <th className="p-4 text-left font-medium">Date</th>
      <th className="p-4 text-left font-medium">Type</th>
      <th className="p-4 text-left font-medium">Category</th>
      <th className="p-4 text-left font-medium">Status</th>
      <th className="p-4 text-left font-medium">Details</th>
      <th className="p-4 text-left font-medium">Technician</th>
      <th className="p-4 text-left font-medium">Next Due Date</th>
      <th className="p-4 text-left font-medium">Actions</th>
    </tr>
  </thead>
  <tbody>
    {filteredRecords.map((record) => (
      <tr key={record.MaintenanceID} className="border-b border-input">
        <td className="p-4">{new Date(record.MaintenanceDate).toLocaleDateString()}</td>
        <td className="p-4">{record.maintenanceType}</td>
        <td className="p-4">{record.maintenanceCategory}</td>
        <td className="p-4">
          <span className={`px-2 py-1 rounded-full text-sm ${
            record.maintenanceStatus === 'IN_PROGRESS' ? 'text-blue-400' :
            record.maintenanceStatus === 'COMPLETED' ? 'text-green-400' :
            record.maintenanceStatus === 'SCHEDULED' ? 'text-yellow-400' :
            'text-red-400'
          }`}>{record.maintenanceStatus}</span>
        </td>
        <td className="p-4">{record.Details}</td>
        <td className="p-4">{record.Technician}</td>
        <td className="p-4">{new Date(record.nextDueDate).toLocaleDateString()}</td>
        <td className="p-4">
          <div className="flex space-x-2">
            <Button variant="ghost" size="sm" onClick={() => setEditingRecord(record)}>
              <PencilLine className="h-4 w-4" />
            </Button>
            <Button variant="ghost" size="sm" className="text-red-400" onClick={() => setRecordToDelete(record)}>
              <Trash2 className="h-4 w-4" />
            </Button>
          </div>
        </td>
      </tr>
    ))}
  </tbody>
</table>
      </div>

      <MaintenanceRecordDialog
        open={showAddDialog}
        onOpenChange={setShowAddDialog}
        onSubmit={handleAddRecord}
        mode="add"
      />

      {editingRecord && (
        <MaintenanceRecordDialog
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
            <AlertDialogTitle>Delete Maintenance Record</AlertDialogTitle>
            <AlertDialogDescription>
              Are you sure you want to delete this maintenance record? 
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