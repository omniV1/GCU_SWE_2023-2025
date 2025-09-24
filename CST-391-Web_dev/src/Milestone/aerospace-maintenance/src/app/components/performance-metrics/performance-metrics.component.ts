/**
 * Performance Metrics Component
 * Manages display and operations for aircraft performance records
 * Includes CRUD operations and data filtering capabilities
 */
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { ActivatedRoute } from '@angular/router';

import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { AircraftService } from '../../services/aircraft.service';
import { PerformanceMetric, NewPerformanceMetric } from '../../models/performance.model';
import { AddPerformanceDialogComponent } from './add-performance-dialog/add-performance-dialog.component';
import { EditPerformanceDialogComponent } from './edit-performance-dialog/edit-performance-dialog.component';
import { ConfirmationDialogComponent } from '../aircraft-list/confimation-dialog/confirmation-dialog.component';

@Component({
  selector: 'app-performance-metrics',
  standalone: false, 
  templateUrl: 'performance-metrics.component.html',
  styleUrls: ['performance-metrics.component.scss'],                                                        
})
export class PerformanceMetricsComponent implements OnInit {
  // Table column definitions
  displayedColumns: string[] = [
    'MetricID',
    'FlightTime',
    'OilConsumption',
    'FuelConsumption',
    'actions'
  ];

  // Table data source with type safety
  dataSource: MatTableDataSource<PerformanceMetric> = new MatTableDataSource<PerformanceMetric>();
  aircraftId: number = 0;
  
  // Material table feature references
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(
    private route: ActivatedRoute,
    private aircraftService: AircraftService,
    private dialog: MatDialog,
    private snackBar: MatSnackBar
  ) {}

  /**
   * Initialize component and load aircraft performance data
   */
  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');
    if (idParam) {
      this.aircraftId = +idParam;
      this.loadPerformanceRecords();
    }
  }

  /**
   * Set up sorting and pagination after view initialization
   */
  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }

  /**
   * Load performance records for the selected aircraft
   */
  loadPerformanceRecords(): void {
    this.aircraftService.getPerformanceRecordsByAircraftId(this.aircraftId).subscribe({
      next: (records: PerformanceMetric[]) => {
        console.log('Loaded performance records:', records);
        this.dataSource.data = records;
      },
      error: (error: any) => {
        console.error('Error loading performance records:', error);
        this.snackBar.open('Error loading performance records', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }

  /**
   * Opens dialog for adding new performance record
   */
  openAddDialog(): void {
    const dialogRef = this.dialog.open(AddPerformanceDialogComponent, {
      width: '500px',
      data: { aircraftId: this.aircraftId }
    });
  
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        console.log('Dialog result:', result); // Add logging
        
        this.aircraftService.addPerformanceRecord(this.aircraftId, result).subscribe({
          next: (newRecord) => {
            console.log('New record added:', newRecord);
            this.loadPerformanceRecords();
            this.snackBar.open('Performance record added successfully', 'Close', {
              duration: 3000,
              panelClass: ['success-snackbar']
            });
          },
          error: (error) => {
            console.error('Error adding record:', error);
            this.snackBar.open('Error adding performance record', 'Close', {
              duration: 3000,
              panelClass: ['error-snackbar']
            });
          }
        });
      }
    });
  }

  /**
   * Opens dialog for editing existing performance record
   * @param record - Performance record to edit
   */
  openEditDialog(record: PerformanceMetric): void {
    const dialogRef = this.dialog.open(EditPerformanceDialogComponent, {
      width: '500px',
      data: { ...record }
    });

    dialogRef.afterClosed().subscribe((result?: PerformanceMetric) => {
      if (result) {
        this.aircraftService.updatePerformanceRecord(this.aircraftId, result).subscribe({
          next: () => {
            this.loadPerformanceRecords();
            this.snackBar.open('Performance record updated successfully', 'Close', {
              duration: 3000,
              panelClass: ['success-snackbar']
            });
          },
          error: (error: any) => {
            console.error('Error updating performance record:', error);
            this.snackBar.open('Error updating performance record', 'Close', {
              duration: 3000,
              panelClass: ['error-snackbar']
            });
          }
        });
      }
    });
  }

  /**
   * Opens confirmation dialog and deletes performance record if confirmed
   * @param record - Performance record to delete
   */
  deleteRecord(record: PerformanceMetric): void {
    const dialogRef = this.dialog.open(ConfirmationDialogComponent, {
      width: '400px',
      data: {
        title: 'Delete Performance Record',
        message: 'Are you sure you want to delete this performance record?',
        confirmText: 'Delete',
        cancelText: 'Cancel'
      }
    });

    dialogRef.afterClosed().subscribe((result: boolean) => {
      if (result) {
        this.aircraftService.deletePerformanceRecord(this.aircraftId, record.MetricID).subscribe({
          next: () => {
            this.loadPerformanceRecords();
            this.snackBar.open('Performance record deleted successfully', 'Close', {
              duration: 3000,
              panelClass: ['success-snackbar']
            });
          },
          error: (error: any) => {
            console.error('Error deleting performance record:', error);
            this.snackBar.open('Error deleting performance record', 'Close', {
              duration: 3000,
              panelClass: ['error-snackbar']
            });
          }
        });
      }
    });
  }

  /**
   * Applies filter to the table data
   * @param event - Input event from filter field
   */
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}