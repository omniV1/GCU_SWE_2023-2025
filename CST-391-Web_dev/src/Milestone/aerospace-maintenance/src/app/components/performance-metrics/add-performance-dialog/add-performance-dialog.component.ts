// add-performance-dialog.component.ts
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewPerformanceMetric } from '../../../models/performance.model';


@Component({
  selector: 'app-add-performance-dialog',
  standalone: false,
  templateUrl: './add-performance-dialog.component.html',
  styleUrls: ['./add-performance-dialog.component.scss']
})
export class AddPerformanceDialogComponent {
  performanceForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<AddPerformanceDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { aircraftId: number }
  ) {
    this.performanceForm = this.fb.group({
      FlightTime: ['', [Validators.required, Validators.min(0)]],
      OilConsumption: ['', [Validators.required, Validators.min(0)]],
      FuelConsumption: ['', [Validators.required, Validators.min(0)]] // Match backend field name
    });
  }

  onSave(): void {
    if (this.performanceForm.valid) {
      const newRecord: NewPerformanceMetric = {
        ...this.performanceForm.value,
        AircraftID: this.data.aircraftId
      };
      console.log('Saving record:', newRecord); // Add logging
      this.dialogRef.close(newRecord);
    }
  }

  onCancel(): void {
    this.dialogRef.close();
  }
}