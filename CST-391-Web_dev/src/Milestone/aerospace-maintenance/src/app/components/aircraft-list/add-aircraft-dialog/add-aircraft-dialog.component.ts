// add-aircraft-dialog.component.ts

/**
 * Dialog component for adding new aircraft or editing existing aircraft details
 * Implements a reactive form with validation for aircraft properties
 * 
 * @usage
 * const dialogRef = dialog.open(AddAircraftDialogComponent, {
 *   data: existingAircraft // Optional: Pass existing aircraft for editing
 * });
 */
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Aircraft, AircraftStatus } from '../../../models/aircraft.model';


@Component({
  selector: 'app-add-aircraft-dialog',
  standalone: false,  // 

  templateUrl: './add-aircraft-dialog.component.html',
  styleUrls: ['./add-aircraft-dialog.component.scss']
})
export class AddAircraftDialogComponent {
  // Reactive form instance for aircraft details
  aircraftForm: FormGroup;
  
  // Array of possible aircraft statuses from enum for dropdown
  aircraftStatus = Object.values(AircraftStatus);

  /**
   * @param fb - FormBuilder service for creating reactive form
   * @param dialogRef - Reference to dialog instance
   * @param data - Optional existing aircraft data for editing
   */
  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<AddAircraftDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    // Initialize form with validators for required fields
    this.aircraftForm = this.fb.group({
      model: ['', Validators.required],
      serialNumber: ['', Validators.required],
      dateOfManufacture: ['', Validators.required],
      flightTime: ['', Validators.required],
      engineHours: ['', Validators.required],
      status: ['', Validators.required]
    });
  }

  /**
   * Saves the form data if valid and closes dialog
   * Returns form value to parent component through dialogRef
   */
  save() {
    if (this.aircraftForm.valid) {
      this.dialogRef.close(this.aircraftForm.value);
    }
  }

  /**
   * Closes the dialog without saving changes
   */
  cancel() {
    this.dialogRef.close();
  }
}