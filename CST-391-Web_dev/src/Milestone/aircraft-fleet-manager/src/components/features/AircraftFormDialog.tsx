// src/components/features/AircraftFormDialog.tsx
import { useState, useEffect } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Aircraft, AircraftStatus } from '@/types';

interface AircraftFormData {
  model: string;
  serialNumber: string;
  dateOfManufacture: string;
  flightTime: number;
  engineHours: number;
  status: AircraftStatus;
}

interface AircraftFormDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onSubmit: (data: AircraftFormData) => void;
  initialData?: Aircraft;
  mode: 'add' | 'edit';
}

/**
 * AircraftFormDialog component renders a dialog for adding or editing aircraft details.
 *
 * @param {Object} props - The component props.
 * @param {boolean} props.open - Indicates whether the dialog is open.
 * @param {function} props.onOpenChange - Callback function to handle dialog open state change.
 * @param {function} props.onSubmit - Callback function to handle form submission.
 * @param {AircraftFormData} [props.initialData] - Initial data to populate the form fields.
 * @param {'add' | 'edit'} props.mode - Mode of the form, either 'add' for adding a new aircraft or 'edit' for editing an existing aircraft.
 *
 * @returns {JSX.Element} The rendered AircraftFormDialog component.
 */
export function AircraftFormDialog({
  open,
  onOpenChange,
  onSubmit,
  initialData,
  mode
}: AircraftFormDialogProps) {
  const [formData, setFormData] = useState<AircraftFormData>({
    model: '',
    serialNumber: '',
    dateOfManufacture: new Date().toISOString().split('T')[0],
    flightTime: 0,
    engineHours: 0,
    status: AircraftStatus.NOT_READY
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        model: initialData.model || '',
        serialNumber: initialData.serialNumber || '',
        dateOfManufacture: initialData.dateOfManufacture 
          ? new Date(initialData.dateOfManufacture).toISOString().split('T')[0]
          : new Date().toISOString().split('T')[0],
        flightTime: initialData.flightTime || 0,
        engineHours: initialData.engineHours || 0,
        status: initialData.status || AircraftStatus.NOT_READY
      });
    }
  }, [initialData]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>
            {mode === 'add' ? 'Add Aircraft' : 'Edit Aircraft'}
          </DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <Label>Model</Label>
            <Input
              value={formData.model}
              onChange={(e) => setFormData({ ...formData, model: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Serial Number</Label>
            <Input
              value={formData.serialNumber}
              onChange={(e) => setFormData({ ...formData, serialNumber: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Date of Manufacture</Label>
            <Input
              type="date"
              value={formData.dateOfManufacture}
              onChange={(e) => setFormData({ ...formData, dateOfManufacture: e.target.value })}
              required
            />
          </div>

          <div className="space-y-2">
            <Label>Flight Time (hours)</Label>
            <Input
              type="number"
              value={formData.flightTime}
              onChange={(e) => setFormData({ ...formData, flightTime: Number(e.target.value) })}
              required
              min="0"
              step="0.1"
            />
          </div>

          <div className="space-y-2">
            <Label>Engine Hours</Label>
            <Input
              type="number"
              value={formData.engineHours}
              onChange={(e) => setFormData({ ...formData, engineHours: Number(e.target.value) })}
              required
              min="0"
              step="0.1"
            />
          </div>

          <div className="space-y-2">
            <Label>Status</Label>
            <select
              className="w-full h-10 rounded-md border border-input bg-background px-3 py-2"
              value={formData.status}
              onChange={(e) => setFormData({ ...formData, status: e.target.value as AircraftStatus })}
            >
              {Object.values(AircraftStatus).map((status) => (
                <option key={status} value={status}>
                  {status.toLowerCase()}
                </option>
              ))}
            </select>
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