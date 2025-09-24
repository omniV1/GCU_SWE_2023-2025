/**
 * Dialog component for editing existing aircraft details
 * Provides a form interface to modify aircraft properties with validation
 * Handles date formatting and data transformation for the backend
 */
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AircraftWithMaintenance, AircraftStatus } from '../../../models/aircraft.model';

@Component({
  selector: 'app-edit-aircraft-dialog',
  standalone: false, 
  templateUrl: './edit-aircraft-dialog.component.html',
  styleUrls: ['./edit-aircraft-dialog.component.scss']
})
export class EditAircraftDialogComponent {
  // Reactive form for aircraft data
  aircraftForm!: FormGroup;
  
  // Array of possible aircraft statuses from enum for dropdown
  aircraftStatus = Object.values(AircraftStatus);

  /**
   * @param fb - FormBuilder service for creating reactive form
   * @param dialogRef - Reference to dialog instance
   * @param data - Existing aircraft data to be edited
   */
  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<EditAircraftDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: AircraftWithMaintenance
  ) {
    console.log('Constructor received data:', data);
    
    // Validate incoming aircraft data
    if (!data || !data.aircraftID) {
      console.error('Invalid data received:', data);
      this.dialogRef.close();
      return;
    }
  
    try {
      // Format the date for the date input field
      const formattedDate = data.dateOfManufacture ? 
        new Date(data.dateOfManufacture).toISOString().split('T')[0] : 
        '';
  
      // Initialize form with existing aircraft data and validators
      this.aircraftForm = this.fb.group({
        model: [data.model || '', Validators.required],
        serialNumber: [data.serialNumber || '', Validators.required],
        dateOfManufacture: [formattedDate, Validators.required],
        flightTime: [data.flightTime || 0, [Validators.required, Validators.min(0)]],
        engineHours: [data.engineHours || 0, [Validators.required, Validators.min(0)]],
        status: [data.status || '', Validators.required]
      });
    } catch (error) {
      console.error('Error initializing form:', error);
      this.dialogRef.close();
    }
  }

  /**
   * Saves the form data if valid and closes dialog
   * Formats dates and prepares data for backend
   */
  save() {
    if (this.aircraftForm.valid) {
      const formValue = this.aircraftForm.value;
      // Format the date for backend storage
      const formattedDateOfManufacture = new Date(formValue.dateOfManufacture)
        .toISOString().split('T')[0];
      
      // Prepare updated aircraft object
      const updatedAircraft = {
        model: formValue.model,
        serialNumber: formValue.serialNumber,
        dateOfManufacture: formattedDateOfManufacture,
        flightTime: formValue.flightTime,
        engineHours: formValue.engineHours,
        status: formValue.status,
        aircraftID: this.data.aircraftID
      };
  
      console.log('Saving updated aircraft:', updatedAircraft);
      this.dialogRef.close(updatedAircraft);
    }
  }
  
  /**
   * Closes the dialog without saving changes
   */
  cancel() {
    this.dialogRef.close();
  }
}