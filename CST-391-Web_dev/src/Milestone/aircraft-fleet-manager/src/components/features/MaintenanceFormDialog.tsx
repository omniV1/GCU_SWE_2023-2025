import { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select } from "@/components/ui/select";
import { MaintenanceType, MaintenanceStatus, MaintenanceCategory } from '@/types/maintenance';

 export interface MaintenanceFormData {
  MaintenanceDate: string;
  Details: string;
  Technician: string;
  maintenanceType: MaintenanceType;
  nextDueDate: string;
  maintenanceStatus: MaintenanceStatus;
  maintenanceCategory: MaintenanceCategory;
  AircraftID: number;  // Add this line
}

interface MaintenanceFormDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onSubmit: (data: MaintenanceFormData) => void;
  initialData?: Partial<MaintenanceFormData>;
  mode: 'add' | 'edit';
}

/**
 * Component for displaying a maintenance form dialog.
 * 
 * @param {Object} props - The component props.
 * @param {boolean} props.open - Indicates whether the dialog is open.
 * @param {function} props.onOpenChange - Callback function to handle dialog open state change.
 * @param {function} props.onSubmit - Callback function to handle form submission.
 * @param {MaintenanceFormData} [props.initialData] - Initial data for the form.
 * @param {'add' | 'edit'} props.mode - Mode of the form, either 'add' or 'edit'.
 * 
 * @returns {JSX.Element} The rendered component.
 */
export function MaintenanceFormDialog({
  open,
  onOpenChange,
  onSubmit,
  initialData,
  mode
}: MaintenanceFormDialogProps) {
  const [formData, setFormData] = useState<MaintenanceFormData>({
    MaintenanceDate: initialData?.MaintenanceDate || '',
    Details: initialData?.Details || '',
    Technician: initialData?.Technician || '',
    maintenanceType: initialData?.maintenanceType || MaintenanceType.ROUTINE,
    nextDueDate: initialData?.nextDueDate || '',
    maintenanceStatus: initialData?.maintenanceStatus || MaintenanceStatus.SCHEDULED,
    maintenanceCategory: initialData?.maintenanceCategory || MaintenanceCategory.ENGINE,
    AircraftID: initialData?.AircraftID || 0  // Add this line
  });

  const [errors, setErrors] = useState<Partial<Record<keyof MaintenanceFormData, string>>>({});

  const validateForm = () => {
    const newErrors: Partial<Record<keyof MaintenanceFormData, string>> = {};

    if (!formData.MaintenanceDate) newErrors.MaintenanceDate = 'Date is required';
    if (!formData.Details) newErrors.Details = 'Details are required';
    if (!formData.Technician) newErrors.Technician = 'Technician name is required';
    if (!formData.nextDueDate) newErrors.nextDueDate = 'Next due date is required';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validateForm()) {
      onSubmit(formData);
    }
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
          <div className="grid gap-4">
            <div>
              <Label>Maintenance Date</Label>
              <Input
                type="date"
                value={formData.MaintenanceDate}
                onChange={(e) => setFormData({ ...formData, MaintenanceDate: e.target.value })}
                error={errors.MaintenanceDate}
              />
            </div>

            <div>
              <Label>Type</Label>
              <Select
                value={formData.maintenanceType}
                onChange={(e) => setFormData({ ...formData, maintenanceType: e.target.value as MaintenanceType })}
              >
                {Object.values(MaintenanceType).map((type) => (
                  <option key={type} value={type}>{type}</option>
                ))}
              </Select>
            </div>

            <div>
              <Label>Category</Label>
              <Select
                value={formData.maintenanceCategory}
                onChange={(e) => setFormData({ ...formData, maintenanceCategory: e.target.value as MaintenanceCategory })}
              >
                {Object.values(MaintenanceCategory).map((category) => (
                  <option key={category} value={category}>{category}</option>
                ))}
              </Select>
            </div>

            <div>
              <Label>Details</Label>
              <Input
                value={formData.Details}
                onChange={(e) => setFormData({ ...formData, Details: e.target.value })}
                error={errors.Details}
              />
            </div>

            <div>
              <Label>Technician</Label>
              <Input
                value={formData.Technician}
                onChange={(e) => setFormData({ ...formData, Technician: e.target.value })}
                error={errors.Technician}
              />
            </div>

            <div>
              <Label>Next Due Date</Label>
              <Input
                type="date"
                value={formData.nextDueDate}
                onChange={(e) => setFormData({ ...formData, nextDueDate: e.target.value })}
                error={errors.nextDueDate}
              />
            </div>

            <div>
              <Label>Status</Label>
              <Select
                value={formData.maintenanceStatus}
                onChange={(e) => setFormData({ ...formData, maintenanceStatus: e.target.value as MaintenanceStatus })}
              >
                {Object.values(MaintenanceStatus).map((status) => (
                  <option key={status} value={status}>{status}</option>
                ))}
              </Select>
            </div>
          </div>

          <DialogFooter>
            <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>
              Cancel
            </Button>
            <Button type="submit">
              {mode === 'add' ? 'Add' : 'Save'}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}