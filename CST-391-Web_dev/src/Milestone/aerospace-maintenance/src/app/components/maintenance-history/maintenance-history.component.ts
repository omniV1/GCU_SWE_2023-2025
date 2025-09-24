// maintenance-history.component.ts
import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { AircraftService } from '../../services/aircraft.service';

import { 
  MaintenanceRecord, 
  MaintenanceType, 
  MaintenanceStatus, 
  MaintenanceCategory 
} from '../../models/maintenance.model';
import { MaintenanceRecordDialogComponent } from './maintenance-record-dialog/maintenance-record-dialog.component';
import { ConfirmationDialogComponent } from '../aircraft-list/confimation-dialog/confirmation-dialog.component';

/**
 * Component for displaying and managing the maintenance history of an aircraft.
 */
@Component({
  selector: 'app-maintenance-history',
  standalone: false,
  templateUrl: './maintenance-history.component.html',
  styleUrls: ['./maintenance-history.component.scss']
})
export class MaintenanceHistoryComponent implements OnInit {
  /**
   * Columns to be displayed in the maintenance history table.
   */
  displayedColumns: string[] = [
    'MaintenanceDate',
    'maintenanceType',
    'maintenanceCategory',
    'Details',
    'Technician',
    'maintenanceStatus',
    'nextDueDate',
    'actions'
  ];

  /**
   * Data source for the maintenance history table.
   */
  dataSource: MatTableDataSource<MaintenanceRecord> = new MatTableDataSource<MaintenanceRecord>();

  /**
   * ID of the aircraft whose maintenance history is being displayed.
   */
  aircraftId: number = 0;

  /**
   * Reference to the table sort directive.
   */
  @ViewChild(MatSort) sort!: MatSort;

  /**
   * Reference to the table paginator directive.
   */
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  /**
   * List of maintenance types.
   */
  maintenanceTypes = Object.values(MaintenanceType);

  /**
   * List of maintenance statuses.
   */
  maintenanceStatuses = Object.values(MaintenanceStatus);

  /**
   * List of maintenance categories.
   */
  maintenanceCategories = Object.values(MaintenanceCategory);

  /**
   * Selected maintenance category for filtering.
   */
  selectedCategory: MaintenanceCategory | 'ALL' = 'ALL';

  constructor(
    private route: ActivatedRoute,
    private aircraftService: AircraftService,
    private dialog: MatDialog,
    private snackBar: MatSnackBar
  ) {}

  /**
   * Initializes the component by loading the maintenance records.
   */
  ngOnInit(): void {
    this.aircraftId = Number(this.route.snapshot.paramMap.get('id'));
    this.loadMaintenanceRecords();
  }

  /**
   * Sets up the table sort and paginator after the view has been initialized.
   */
  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }

  /**
   * Adds a new maintenance record.
   * @param record The maintenance record to add.
   */
  addMaintenanceRecord(record: MaintenanceRecord): void {
    this.aircraftService.addMaintenanceRecord(this.aircraftId, record).subscribe({
      next: () => {
        this.loadMaintenanceRecords();
        this.snackBar.open('Maintenance record added successfully', 'Close', {
          duration: 3000,
          panelClass: ['success-snackbar']
        });
      },
      error: (error) => {
        console.error('Error adding maintenance record:', error);
        this.snackBar.open('Error adding maintenance record', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }

  /**
   * Updates an existing maintenance record.
   * @param record The maintenance record to update.
   */
  updateMaintenanceRecord(record: MaintenanceRecord): void {
    console.log('Attempting to update record:', record); // Debug log
    this.aircraftService.updateMaintenanceRecord(this.aircraftId, record).subscribe({
      next: (response) => {
        console.log('Update successful, response:', response); // Debug log
        this.loadMaintenanceRecords();
        this.snackBar.open('Maintenance record updated successfully', 'Close', {
          duration: 3000,
          panelClass: ['success-snackbar']
        });
      },
      error: (error) => {
        console.error('Error updating maintenance record:', error);
        console.error('Full error details:', JSON.stringify(error, null, 2)); // Detailed error log
        this.snackBar.open('Error updating maintenance record', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }

  /**
   * Deletes a maintenance record.
   * @param record The maintenance record to delete.
   */
  deleteMaintenanceRecord(record: MaintenanceRecord): void {
    this.aircraftService.deleteMaintenanceRecord(this.aircraftId, record.MaintenanceID).subscribe({
      next: () => {
        this.loadMaintenanceRecords();
        this.snackBar.open('Maintenance record deleted successfully', 'Close', {
          duration: 3000,
          panelClass: ['success-snackbar']
        });
      },
      error: (error) => {
        console.error('Error deleting maintenance record:', error);
        this.snackBar.open('Error deleting maintenance record', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }

  /**
   * Opens a dialog for adding or editing a maintenance record.
   * @param record The maintenance record to edit (optional).
   */
  openMaintenanceDialog(record?: MaintenanceRecord): void {
    const dialogRef = this.dialog.open(MaintenanceRecordDialogComponent, {
      width: '500px',
      data: { 
        aircraftId: this.aircraftId,
        record: record
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        if (result.MaintenanceID) {
          this.updateMaintenanceRecord(result);
        } else {
          this.addMaintenanceRecord(result);
        }
      }
    });
  }

  /**
   * Opens a confirmation dialog for deleting a maintenance record.
   * @param record The maintenance record to delete.
   */
  openDeleteConfirmDialog(record: MaintenanceRecord): void {
    const dialogRef = this.dialog.open(ConfirmationDialogComponent, {
      width: '400px',
      data: {
        title: 'Delete Maintenance Record',
        message: 'Are you sure you want to delete this maintenance record?',
        confirmText: 'Delete',
        cancelText: 'Cancel'
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.deleteMaintenanceRecord(record);
      }
    });
  }

  /**
   * Gets the CSS class for the maintenance type chip.
   * @param type The maintenance type.
   * @returns The CSS class for the maintenance type chip.
   */
  getMaintenanceTypeColor(type: MaintenanceType): string {
    switch (type) {
      case MaintenanceType.ROUTINE:
        return 'routine-chip';
      case MaintenanceType.INSPECTION:
        return 'inspection-chip';
      case MaintenanceType.REPAIR:
        return 'repair-chip';
      case MaintenanceType.OVERHAUL:
        return 'overhaul-chip';
      default:
        return '';
    }
  }

  /**
   * Gets the CSS class for the maintenance category chip.
   * @param category The maintenance category.
   * @returns The CSS class for the maintenance category chip.
   */
  getCategoryChipColor(category: MaintenanceCategory): string {
    switch (category) {
      case MaintenanceCategory.ENGINE:
        return 'engine-chip';    // red/orange for engine
      case MaintenanceCategory.AIRFRAME:
        return 'airframe-chip';  // blue/teal for airframe
      case MaintenanceCategory.AVIONICS:
        return 'avionics-chip';  // purple for avionics
      default:
        return '';
    }
  }

  /**
   * Gets the CSS class for the maintenance status chip.
   * @param status The maintenance status.
   * @returns The CSS class for the maintenance status chip.
   */
  getMaintenanceColor(status: MaintenanceStatus): string {
    switch (status) {
      case MaintenanceStatus.COMPLETED:
        return 'completed-status';    // Will use magenta/pink
      case MaintenanceStatus.IN_PROGRESS:
        return 'in-progress-status';  // Will use red
      case MaintenanceStatus.SCHEDULED:
        return 'scheduled-status';    // Will use grey/silver
      case MaintenanceStatus.DEFERRED:
        return 'deferred-status';     // Will use warning color
      default:
        return '';
    }
  }

  /**
   * Checks if a maintenance record is overdue.
   * @param date The date to check.
   * @returns True if the maintenance record is overdue, false otherwise.
   */
  isOverdue(date: Date): boolean {
    return new Date(date) < new Date();
  }

  /**
   * Gets the tooltip text for the maintenance status.
   * @param record The maintenance record.
   * @returns The tooltip text for the maintenance status.
   */
  getMaintenanceStatusTooltip(record: MaintenanceRecord): string {
    return `Status: ${record.maintenanceStatus}`;
  }

  /**
   * Gets the icon for the maintenance status.
   * @param status The maintenance status.
   * @returns The icon for the maintenance status.
   */
  getMaintenanceIcon(status: MaintenanceStatus): string {
    switch (status) {
      case MaintenanceStatus.COMPLETED:
        return 'check_circle';
      case MaintenanceStatus.SCHEDULED:
        return 'schedule';
      case MaintenanceStatus.IN_PROGRESS:
        return 'alarm';
      case MaintenanceStatus.DEFERRED:
        return 'error';
      default:
        return 'help';
    }
  }

  /**
   * Handles the change of the maintenance category filter.
   * @param category The selected maintenance category.
   */
  onCategoryChange(category: MaintenanceCategory | 'ALL'): void {
    console.log('Category changed to:', category);
    this.selectedCategory = category;
    this.applyFilters();
  }

  /**
   * Applies the current filters to the data source.
   */
  private applyFilters(): void {
    const currentFilter = {
      searchTerm: this.dataSource.filter ? 
        JSON.parse(this.dataSource.filter).searchTerm || '' : 
        '',
      category: this.selectedCategory
    };
    
    console.log('Applying filters:', currentFilter);
    this.dataSource.filter = JSON.stringify(currentFilter);
  }

  /**
   * Applies a search filter to the data source.
   * @param event The input event containing the search term.
   */
  applyFilter(event: Event): void {
    const filterValue = (event.target as HTMLInputElement).value;
    const currentFilter = {
      searchTerm: filterValue.trim().toLowerCase(),
      category: this.selectedCategory
    };
    
    console.log('Applying search filter:', currentFilter);
    this.dataSource.filter = JSON.stringify(currentFilter);
  }

  /**
   * Loads the maintenance records for the aircraft.
   */
  private loadMaintenanceRecords(): void {
    this.aircraftService.getMaintenanceHistory(this.aircraftId).subscribe({
      next: (records) => {
        this.dataSource.data = records;
        this.dataSource.filterPredicate = (data: MaintenanceRecord, filterString: string) => {
          try {
            const filterValue = JSON.parse(filterString);
            
            // Check category filter
            if (filterValue.category !== 'ALL' && 
              data.maintenanceCategory.toUpperCase() !== filterValue.category.toUpperCase()) {
            return false;
          }
  
            // If no search term, return true after category check
            if (!filterValue.searchTerm) {
              return true;
            }
  
            // Check search term against relevant fields
            const searchFields = [
              data.maintenanceType,
              data.maintenanceCategory,
              data.Details,
              data.Technician,
              data.maintenanceStatus
            ].map(field => field?.toLowerCase() || '');
  
            return searchFields.some(field => 
              field.includes(filterValue.searchTerm.toLowerCase())
            );
          } catch (error) {
            console.error('Error parsing filter:', error);
            return true; // Show all records if filter is invalid
          }
        };
  
        // Initialize filter
        this.applyFilters();
      },
      error: (error) => {
        console.error('Error loading maintenance records:', error);
        this.snackBar.open('Error loading maintenance records', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }

  /**
   * Gets the icon for the maintenance type.
   * @param type The maintenance type.
   * @returns The icon for the maintenance type.
   */
  getMaintenanceTypeIcon(type: MaintenanceType): string {
    switch (type) {
      case MaintenanceType.ROUTINE:
        return 'schedule';
      case MaintenanceType.REPAIR:
        return 'build';
      case MaintenanceType.INSPECTION:
        return 'search';
      case MaintenanceType.OVERHAUL:
        return 'engineering';
      default:
        return 'engineering';
    }
  }

  /**
   * Gets the icon for the maintenance category.
   * @param category The maintenance category.
   * @returns The icon for the maintenance category.
   */
  getCategoryIcon(category: MaintenanceCategory): string {
    switch (category) {
      case MaintenanceCategory.ENGINE:
        return 'engine';
      case MaintenanceCategory.AIRFRAME:
        return 'flight';
      case MaintenanceCategory.AVIONICS:
        return 'wifi';
      default:
        return 'category';
    }
  }

  /**
   * Gets the color for the maintenance status.
   * @param status The maintenance status.
   * @returns The color for the maintenance status.
   */
  getStatusColor(status: MaintenanceStatus): string {
    switch (status) {
      case MaintenanceStatus.COMPLETED:
        return 'primary';
      case MaintenanceStatus.IN_PROGRESS:
        return 'accent';
      case MaintenanceStatus.SCHEDULED:
        return 'basic';
      case MaintenanceStatus.DEFERRED:
        return 'warn';
      default:
        return 'basic';
    }
  }

  /**
   * Gets the icon for the maintenance status.
   * @param status The maintenance status.
   * @returns The icon for the maintenance status.
   */
  getStatusIcon(status: MaintenanceStatus): string {
    switch (status) {
      case MaintenanceStatus.COMPLETED:
        return 'check_circle';
      case MaintenanceStatus.IN_PROGRESS:
        return 'pending';
      case MaintenanceStatus.SCHEDULED:
        return 'schedule';
      case MaintenanceStatus.DEFERRED:
        return 'warning';
      default:
        return 'help';
    }
  }
}