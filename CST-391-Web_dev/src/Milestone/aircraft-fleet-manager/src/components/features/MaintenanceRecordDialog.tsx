import { useState, useEffect } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { MaintenanceType, MaintenanceStatus, MaintenanceCategory, MaintenanceRecord } from '@/types';

interface MaintenanceRecordFormData {
  MaintenanceDate: string;
  Details: string;
  Technician: string;
  maintenanceType: MaintenanceType;
  nextDueDate: string;
  maintenanceStatus: MaintenanceStatus;
  maintenanceCategory: MaintenanceCategory;
}

interface MaintenanceRecordDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onSubmit: (data: MaintenanceRecordFormData) => void;
  initialData?: MaintenanceRecord;
  mode: 'add' | 'edit';
}

/**
 * Component for displaying a dialog to add or edit a maintenance record.
 *
 * @param {Object} props - The properties object.
 * @param {boolean} props.open - Indicates whether the dialog is open.
 * @param {function} props.onOpenChange - Callback function to handle the change in dialog open state.
 * @param {function} props.onSubmit - Callback function to handle form submission.
 * @param {MaintenanceRecordFormData} [props.initialData] - Initial data for the form, used when editing a record.
 * @param {'add' | 'edit'} props.mode - Mode of the dialog, either 'add' for adding a new record or 'edit' for editing an existing record.
 *
 * @returns {JSX.Element} The rendered MaintenanceRecordDialog component.
 */
export function MaintenanceRecordDialog({
  open,
  onOpenChange,
  onSubmit,
  initialData,
  mode
}: MaintenanceRecordDialogProps) {
  const [formData, setFormData] = useState<MaintenanceRecordFormData>({
    MaintenanceDate: new Date().toISOString().split('T')[0],
    Details: '',
    Technician: '',
    maintenanceType: MaintenanceType.INSPECTION,
    nextDueDate: new Date().toISOString().split('T')[0],
    maintenanceStatus: MaintenanceStatus.SCHEDULED,
    maintenanceCategory: MaintenanceCategory.ENGINE
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        MaintenanceDate: new Date(initialData.MaintenanceDate).toISOString().split('T')[0],
        Details: initialData.Details,
        Technician: initialData.Technician,
        maintenanceType: initialData.maintenanceType,
        nextDueDate: new Date(initialData.nextDueDate).toISOString().split('T')[0],
        maintenanceStatus: initialData.maintenanceStatus,
        maintenanceCategory: initialData.maintenanceCategory
      });
    }
  }, [initialData]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
    onOpenChange(false);
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>
            {mode === 'add' ? 'Add Maintenance Record' : 'Edit Maintenance Record'}
          </DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <Label>Date</Label>
            <Input
              type="date"
              value={formData.MaintenanceDate}
              onChange={(e) => setFormData({ ...formData, MaintenanceDate: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Type</Label>
            <select
              className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
              value={formData.maintenanceType}
              onChange={(e) => setFormData({ ...formData, maintenanceType: e.target.value as MaintenanceType })}
            >
              {Object.values(MaintenanceType).map((type) => (
                <option key={type} value={type}>{type}</option>
              ))}
            </select>
          </div>

          <div className="space-y-2">
            <Label>Category</Label>
            <select
              className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
              value={formData.maintenanceCategory}
              onChange={(e) => setFormData({ ...formData, maintenanceCategory: e.target.value as MaintenanceCategory })}
            >
              {Object.values(MaintenanceCategory).map((category) => (
                <option key={category} value={category}>{category}</option>
              ))}
            </select>
          </div>

          <div className="space-y-2">
            <Label>Details</Label>
            <Input
              value={formData.Details}
              onChange={(e) => setFormData({ ...formData, Details: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Technician</Label>
            <Input
              value={formData.Technician}
              onChange={(e) => setFormData({ ...formData, Technician: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Status</Label>
            <select
              className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
              value={formData.maintenanceStatus}
              onChange={(e) => setFormData({ ...formData, maintenanceStatus: e.target.value as MaintenanceStatus })}
            >
              {Object.values(MaintenanceStatus).map((status) => (
                <option key={status} value={status}>{status}</option>
              ))}
            </select>
          </div>

          <div className="space-y-2">
            <Label>Next Due Date</Label>
            <Input
              type="date"
              value={formData.nextDueDate}
              onChange={(e) => setFormData({ ...formData, nextDueDate: e.target.value })}
              required
            />
          </div>

          <DialogFooter>
            <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>
              Cancel
            </Button>
            <Button type="submit">
              {mode === 'add' ? 'Add Record' : 'Save Changes'}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}