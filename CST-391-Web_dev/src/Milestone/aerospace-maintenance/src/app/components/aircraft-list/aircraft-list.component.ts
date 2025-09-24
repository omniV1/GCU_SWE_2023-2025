// aircraft-list.component.ts

/**
 * Component for displaying and managing the aircraft fleet
 * Provides functionality for viewing, adding, editing, and deleting aircraft
 * Includes maintenance status tracking and performance monitoring
 */
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { Router } from '@angular/router';
import { AircraftStatus, AircraftWithMaintenance } from '../../models/aircraft.model';
import { MaintenanceStatus } from '../../models/maintenance.model';
import { AircraftService } from '../../services/aircraft.service';
import { MatDialog } from '@angular/material/dialog';
import { AddAircraftDialogComponent } from './add-aircraft-dialog/add-aircraft-dialog.component';
import { EditAircraftDialogComponent } from './edit-aircraft-dialog/edit-aircraft-dialog.component';
import { ConfirmationDialogComponent } from '../aircraft-list/confimation-dialog/confirmation-dialog.component';

@Component({
  selector: 'app-aircraft-list',
  standalone: false, 
  templateUrl: './aircraft-list.component.html',
  styleUrls: ['./aircraft-list.component.scss']
})
export class AircraftListComponent implements OnInit {
  // Enum references for template usage
  MaintenanceStatus = MaintenanceStatus;
  AircraftStatus = AircraftStatus;
  aircraft: AircraftWithMaintenance | undefined;
  
  // Column definitions for material table
  displayedColumns: string[] = [
    'model',
    'serialNumber',
    'lastMaintenanceDate',
    'maintenanceStatus',
    'FlightTime',
    'status',
    'actions'
  ];
  
  // Material table sort and pagination references
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  /**
   * Initializes table sorting and pagination after view initialization
   */
  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }

  // Table data source
  dataSource: MatTableDataSource<AircraftWithMaintenance>;
  
  constructor(
    private router: Router,
    private aircraftService: AircraftService,
    private dialog: MatDialog
  ) {
    this.dataSource = new MatTableDataSource<AircraftWithMaintenance>([]);
  }

  /**
   * Loads initial aircraft data on component initialization
   */
  ngOnInit(): void {
    this.aircraftService.getAllAircraft().subscribe((data) => {
      this.dataSource.data = data;
    });
  }
  
  /**
   * Maps maintenance status to corresponding Material icon
   * @param status - Current maintenance status
   * @returns Material icon name for the status
   */
  getMaintenanceIcon(status: MaintenanceStatus): string {
    switch (status) {
      case MaintenanceStatus.COMPLETED:
        return 'check_circle';
      case MaintenanceStatus.IN_PROGRESS:
        return 'schedule';
      case MaintenanceStatus.DEFERRED:
        return 'error';
      case MaintenanceStatus.SCHEDULED:
        return 'alarm';
      default:
        return 'help';
    }
  }
  
  /**
   * Maps maintenance status to corresponding Material color
   * @param status - Current maintenance status
   * @returns Material color name for the status
   */
  getMaintenanceColor(status: MaintenanceStatus): string {
    switch(status) {
      case MaintenanceStatus.COMPLETED:
        return 'accent';
      case MaintenanceStatus.IN_PROGRESS:
        return 'primary';
      case MaintenanceStatus.DEFERRED:
        return 'warn';
      case MaintenanceStatus.SCHEDULED:
        return 'basic';
      default:
        return '';
    }
  }

  /**
   * Generates tooltip text for maintenance information
   * @param aircraft - Aircraft object with maintenance data
   * @returns Formatted tooltip string with maintenance details
   */
  getMaintenanceTooltip(aircraft: AircraftWithMaintenance): string {
    if (!aircraft.lastMaintenanceDate || !aircraft.nextMaintenanceDate) {
        return 'No maintenance data available';
    }

    const daysAgo = Math.floor(
        (new Date().getTime() - new Date(aircraft.lastMaintenanceDate).getTime()) / (1000 * 3600 * 24)
    );
    const nextDue = Math.floor(
        (new Date(aircraft.nextMaintenanceDate).getTime() - new Date().getTime()) / (1000 * 3600 * 24)
    );
    
    return `Last Maintenance: ${daysAgo} days ago\n` +
           `Next Maintenance Due: ${nextDue} days\n` +
           `Total Flight Time: ${aircraft.flightTime} hours`;
  }

  /**
   * Generates tooltip text for maintenance status
   * @param aircraft - Aircraft object with maintenance data
   * @returns Formatted tooltip string with status details
   */
  getMaintenanceStatusTooltip(aircraft: AircraftWithMaintenance): string {
    if (!aircraft.nextMaintenanceDate) {
        return 'No maintenance scheduled';
    }

    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const nextDate = new Date(aircraft.nextMaintenanceDate);
    nextDate.setHours(0, 0, 0, 0);
    
    const daysUntilNext = Math.ceil(
        (nextDate.getTime() - today.getTime()) / (1000 * 3600 * 24)
    );

    if (daysUntilNext < 0) {
        return `Maintenance overdue by ${Math.abs(daysUntilNext)} days`;
    } else if (daysUntilNext <= 3) {
        return `Maintenance due soon: ${daysUntilNext} days remaining`;
    } else {
        return `Next maintenance due in ${daysUntilNext} days`;
    }
  }

  /**
   * Determines CSS class for maintenance date display
   * @param date - Maintenance date to evaluate
   * @returns CSS class name based on maintenance schedule status
   */
  getMaintenanceDateClass(date: Date | undefined): string {
    if (!date) {
        return 'maintenance-no-data';
    }
    const daysAgo = (new Date().getTime() - new Date(date).getTime()) / (1000 * 3600 * 24);
    if (daysAgo > 30) return 'maintenance-overdue';
    if (daysAgo > 20) return 'maintenance-due-soon';
    return 'maintenance-ok';
  }
  
  /**
   * Handles table filtering
   * @param event - Input event from filter field
   */
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  /**
   * Navigates to aircraft performance view
   * @param aircraftId - ID of selected aircraft
   */
  viewPerformance(aircraftId: number) {
    this.router.navigate(['/aircraft', aircraftId, 'performance']);
  }

  /**
   * Navigates to aircraft maintenance view
   * @param aircraftId - ID of selected aircraft
   */
  viewMaintenance(aircraftId: number) {
    this.router.navigate(['/aircraft', aircraftId, 'maintenance']);
  }

  /**
   * Gets color for aircraft status display
   * @param status - Current aircraft status
   * @returns Material color name
   */
  getStatusColor(status: AircraftStatus): string {
    return status === AircraftStatus.READY ? 'accent' : 'warn';
  }

  /**
   * Gets CSS class for aircraft status display
   * @param status - Current aircraft status
   * @returns CSS class name
   */
  getStatusClass(status: AircraftStatus): string {
    return status === AircraftStatus.READY 
      ? 'status-ready' 
      : 'status-not-ready';
  }

  /**
   * Opens dialog for adding new aircraft
   * Handles dialog result and updates table data
   */
  openAddAircraftDialog() {
    this.dialog.open(AddAircraftDialogComponent, {
      width: '600px',
      data: {}
    }).afterClosed().subscribe((result) => {
      if (result) {
        this.aircraftService.createAircraft(result).subscribe((newAircraft) => {
          this.dataSource.data = [...this.dataSource.data, newAircraft];
        });
      }
    });
  }

  /**
   * Opens dialog for editing existing aircraft
   * Handles dialog result and updates table data
   * @param aircraft - Aircraft to be edited
   */
  openEditAircraftDialog(aircraft: AircraftWithMaintenance) {
    console.log('Opening edit dialog for aircraft:', aircraft);
  
    if (!aircraft || typeof aircraft === 'number') {
      console.error('Invalid aircraft data:', aircraft);
      return;
    }
  
    const dialogRef = this.dialog.open(EditAircraftDialogComponent, {
      width: '500px',
      height: '600px',
      data: aircraft,
      disableClose: true
    });
  
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.aircraftService.updateAircraft(result).subscribe({
          next: () => {
            const index = this.dataSource.data.findIndex(a => a.aircraftID === aircraft.aircraftID);
            if (index !== -1) {
              this.dataSource.data[index] = { ...result, aircraftID: aircraft.aircraftID };
              this.dataSource.data = [...this.dataSource.data];
            }
          },
          error: (error) => console.error('Error updating aircraft:', error)
        });
      }
    });
  }

  /**
   * Opens confirmation dialog for aircraft deletion
   * Handles confirmation and updates table data
   * @param aircraft - Aircraft to be deleted
   */
  deleteAircraft(aircraft: AircraftWithMaintenance) {
    this.dialog.open(ConfirmationDialogComponent, {
      width: '400px',
      data: {
        title: 'Delete Aircraft',
        message: `Are you sure you want to delete the aircraft with serial number ${aircraft.serialNumber}?`
      }
    }).afterClosed().subscribe((result) => {
      if (result) {
        this.aircraftService.deleteAircraft(aircraft.aircraftID).subscribe(() => {
          this.dataSource.data = this.dataSource.data.filter(a => a.aircraftID !== aircraft.aircraftID);
        });
      }
    });
  }
}