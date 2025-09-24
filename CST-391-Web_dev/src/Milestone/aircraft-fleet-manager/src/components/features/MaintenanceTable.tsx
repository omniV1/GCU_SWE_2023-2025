import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { PencilLine, Trash2 } from "lucide-react";
import { MaintenanceRecord } from "@/types/maintenance";

export interface MaintenanceTableProps {
  records: MaintenanceRecord[];
  onEdit: (record: MaintenanceRecord) => void;
  onDelete: (record: MaintenanceRecord) => void;
}

/**
 * Renders a table displaying maintenance records with options to edit or delete each record.
 *
 * @param {MaintenanceTableProps} props - The properties for the MaintenanceTable component.
 * @param {Array} props.records - An array of maintenance records to display in the table.
 * @param {Function} props.onEdit - Callback function to handle editing a maintenance record.
 * @param {Function} props.onDelete - Callback function to handle deleting a maintenance record.
 *
 * @returns {JSX.Element} The rendered MaintenanceTable component.
 */
export function MaintenanceTable({ records, onEdit, onDelete }: MaintenanceTableProps) {
  return (
    <div className="overflow-x-auto">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Date</TableHead>
            <TableHead>Type</TableHead>
            <TableHead>Category</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Details</TableHead>
            <TableHead>Technician</TableHead>
            <TableHead className="text-right">Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {records.map((record) => (
            <TableRow key={record.MaintenanceID}>
              <TableCell>{new Date(record.MaintenanceDate).toLocaleDateString()}</TableCell>
              <TableCell>{record.maintenanceType}</TableCell>
              <TableCell>{record.maintenanceCategory}</TableCell>
              <TableCell>
                <span className={`px-2 py-1 rounded-full text-xs ${
                  record.maintenanceStatus === 'COMPLETED' ? 'bg-green-500/10 text-green-500' :
                  record.maintenanceStatus === 'IN_PROGRESS' ? 'bg-blue-500/10 text-blue-500' :
                  record.maintenanceStatus === 'SCHEDULED' ? 'bg-yellow-500/10 text-yellow-500' :
                  'bg-red-500/10 text-red-500'
                }`}>
                  {record.maintenanceStatus}
                </span>
              </TableCell>
              <TableCell>{record.Details}</TableCell>
              <TableCell>{record.Technician}</TableCell>
              <TableCell className="text-right">
                <div className="flex justify-end gap-2">
                  <Button
                    variant="ghost"
                    size="icon"
                    onClick={() => onEdit(record)}
                  >
                    <PencilLine className="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="text-red-500"
                    onClick={() => onDelete(record)}
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}