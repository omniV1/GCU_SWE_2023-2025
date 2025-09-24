import { useState, useEffect } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogFooter, DialogClose } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { PerformanceMetric } from '@/types/performance';

interface PerformanceMetricDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onSubmit: (data: Omit<PerformanceMetric, 'MetricID'>) => void;
  initialData?: PerformanceMetric;
  mode: 'add' | 'edit';
}

/**
 * PerformanceMetricDialog component renders a dialog for adding or editing performance metrics.
 * 
 * @param {Object} props - The component props.
 * @param {boolean} props.open - Determines if the dialog is open.
 * @param {function} props.onOpenChange - Callback function to handle the dialog open state change.
 * @param {function} props.onSubmit - Callback function to handle form submission.
 * @param {Object} props.initialData - Initial data for the form.
 * @param {number} props.initialData.AircraftID - The ID of the aircraft.
 * @param {number} props.initialData.FlightTime - The flight time of the aircraft.
 * @param {number} props.initialData.OilConsumption - The oil consumption of the aircraft.
 * @param {number} props.initialData.FuelConsumption - The fuel consumption of the aircraft.
 * @param {string} props.mode - The mode of the dialog, either 'add' or 'edit'.
 * 
 * @returns {JSX.Element} The rendered PerformanceMetricDialog component.
 */
export const PerformanceMetricDialog: React.FC<PerformanceMetricDialogProps> = ({ open, onOpenChange, onSubmit, initialData, mode }) => {
  const [formData, setFormData] = useState<Omit<PerformanceMetric, 'MetricID'>>({
    AircraftID: initialData?.AircraftID || 0,
    FlightTime: initialData?.FlightTime || 0,
    OilConsumption: initialData?.OilConsumption || 0,
    FuelConsumption: initialData?.FuelConsumption || 0,
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        AircraftID: initialData.AircraftID,
        FlightTime: initialData.FlightTime,
        OilConsumption: initialData.OilConsumption,
        FuelConsumption: initialData.FuelConsumption,
      });
    }
  }, [initialData]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: parseFloat(value) }));
  };

  const handleSubmit = () => {
    onSubmit(formData);
    onOpenChange(false);
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>{mode === 'add' ? 'Add Performance Metric' : 'Edit Performance Metric'}</DialogTitle>
          <DialogDescription>
            {mode === 'add' ? 'Add a new performance metric.' : 'Edit the performance metric.'}
          </DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div>
            <label htmlFor="FlightTime" className="block text-sm font-medium text-gray-700">
              Flight Time
            </label>
            <Input
              id="FlightTime"
              name="FlightTime"
              value={formData.FlightTime}
              onChange={handleChange}
              type="number"
              className="mt-1"
            />
          </div>
          <div>
            <label htmlFor="OilConsumption" className="block text-sm font-medium text-gray-700">
              Oil Consumption
            </label>
            <Input
              id="OilConsumption"
              name="OilConsumption"
              value={formData.OilConsumption}
              onChange={handleChange}
              type="number"
              className="mt-1"
            />
          </div>
          <div>
            <label htmlFor="FuelConsumption" className="block text-sm font-medium text-gray-700">
              Fuel Consumption
            </label>
            <Input
              id="FuelConsumption"
              name="FuelConsumption"
              value={formData.FuelConsumption}
              onChange={handleChange}
              type="number"
              className="mt-1"
            />
          </div>
        </div>
        <DialogFooter>
          <Button onClick={handleSubmit}>{mode === 'add' ? 'Add' : 'Save'}</Button>
          <DialogClose asChild>
            <Button variant="ghost">Cancel</Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};