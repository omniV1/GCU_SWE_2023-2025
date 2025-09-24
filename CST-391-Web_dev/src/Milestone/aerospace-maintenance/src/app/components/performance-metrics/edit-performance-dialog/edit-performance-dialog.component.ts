/**
 * Dialog component for editing performance metrics
 * Provides form interface for updating flight performance data
 */
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { PerformanceMetric } from '../../../models/performance.model';



@Component({
  selector: 'app-edit-performance-dialog',
  standalone: false, 
  templateUrl: './edit-performance-dialog.component.html',
  styleUrls: ['./edit-performance-dialog.component.scss'],


})
export class EditPerformanceDialogComponent {
  // Reactive form for performance metrics
  performanceForm: FormGroup;

  /**
   * @param fb - FormBuilder service for creating reactive form
   * @param dialogRef - Reference to dialog instance
   * @param data - Existing performance metric data to edit
   */
  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<EditPerformanceDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: PerformanceMetric
  ) {
    // Initialize form with existing data and validators
    this.performanceForm = this.fb.group({
      FlightTime: [data.FlightTime, [Validators.required, Validators.min(0)]],
      OilConsumption: [data.OilConsumption, [Validators.required, Validators.min(0)]],
      FuelConsumption: [data.FuelConsumption, [Validators.required, Validators.min(0)]]  // Matches DB
    });
  }

  /**
   * Save form data if valid and close dialog
   * Combines existing data with form updates
   */
  save() {
    if (this.performanceForm.valid) {
      const updatedMetric = {
        ...this.data,           // Preserve existing data
        ...this.performanceForm.value  // Override with form updates
      };
      this.dialogRef.close(updatedMetric);
    }
  }

  /**
   * Close dialog without saving changes
   */
  cancel() {
    this.dialogRef.close();
  }
}