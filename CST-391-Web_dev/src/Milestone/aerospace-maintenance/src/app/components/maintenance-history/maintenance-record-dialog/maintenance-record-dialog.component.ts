// maintenance-record-dialog.component.ts
import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { 
  MaintenanceRecord, 
  MaintenanceType, 
  MaintenanceStatus, 
  MaintenanceCategory 
} from '../../../models/maintenance.model';

/**
 * Component for displaying and managing a maintenance record dialog.
 * This dialog allows users to add or edit maintenance records for an aircraft.
 * 
 * @component
 * @selector app-maintenance-record-dialog
 * @templateUrl ./maintenance-record-dialog.component.html
 * @styleUrls ['./maintenance-record-dialog.component.scss']
 * 
 * @property {FormGroup} maintenanceForm - The form group for the maintenance record form.
 * @property {boolean} isEdit - Flag indicating if the dialog is in edit mode.
 * @property {string[]} maintenanceTypes - Array of maintenance types.
 * @property {string[]} maintenanceStatuses - Array of maintenance statuses.
 * @property {string[]} maintenanceCategories - Array of maintenance categories.
 * 
 * @constructor
 * @param {FormBuilder} fb - Form builder for creating the form group.
 * @param {MatDialogRef<MaintenanceRecordDialogComponent>} dialogRef - Reference to the dialog.
 * @param {any} data - Data passed to the dialog, including aircraft ID and optional maintenance record.
 * 
 * @method ngOnInit - Initializes the component and patches form values if in edit mode.
 * @method getMaintenanceTypeColor - Returns the color for a given maintenance type.
 * @param {MaintenanceType} type - The maintenance type.
 * @returns {string} - The color for the maintenance type.
 * 
 * @method getMaintenanceTypeIcon - Returns the icon for a given maintenance type.
 * @param {MaintenanceType} type - The maintenance type.
 * @returns {string} - The icon for the maintenance type.
 * 
 * @method getCategoryIcon - Returns the icon for a given maintenance category.
 * @param {MaintenanceCategory} category - The maintenance category.
 * @returns {string} - The icon for the maintenance category.
 * 
 * @method getStatusColor - Returns the color for a given maintenance status.
 * @param {MaintenanceStatus} status - The maintenance status.
 * @returns {string} - The color for the maintenance status.
 * 
 * @method getStatusIcon - Returns the icon for a given maintenance status.
 * @param {MaintenanceStatus} status - The maintenance status.
 * @returns {string} - The icon for the maintenance status.
 * 
 * @method onSubmit - Handles form submission, closes the dialog with the maintenance record data.
 * 
 * @method onCancel - Handles dialog cancellation, closes the dialog without saving.
 */
@Component({
  selector: 'app-maintenance-record-dialog',
  standalone: false, 
  template: `
    <div class="dialog-container">
      <h2 mat-dialog-title>
        <mat-icon>{{isEdit ? 'edit' : 'add'}}_circle</mat-icon>
        {{ isEdit ? 'Edit' : 'Add' }} Maintenance Record
      </h2>

      <mat-dialog-content>
        <form [formGroup]="maintenanceForm" class="maintenance-form">
          <div class="form-row">
            <mat-form-field appearance="outline">
              <mat-label>Maintenance Type</mat-label>
              <mat-select formControlName="maintenanceType" required>
                <mat-option *ngFor="let type of maintenanceTypes" [value]="type">
                  <mat-icon [color]="getMaintenanceTypeColor(type)">
                    {{getMaintenanceTypeIcon(type)}}
                  </mat-icon>
                  {{type}}
                </mat-option>
              </mat-select>
              <mat-error *ngIf="maintenanceForm.get('maintenanceType')?.hasError('required')">
                Maintenance type is required
              </mat-error>
            </mat-form-field>

            <mat-form-field appearance="outline">
              <mat-label>Category</mat-label>
              <mat-select formControlName="maintenanceCategory" required>
                <mat-option *ngFor="let category of maintenanceCategories" [value]="category">
                  <mat-icon>{{getCategoryIcon(category)}}</mat-icon>
                  {{category}}
                </mat-option>
              </mat-select>
              <mat-error *ngIf="maintenanceForm.get('maintenanceCategory')?.hasError('required')">
                Category is required
              </mat-error>
            </mat-form-field>
          </div>

          <div class="form-row">
            <mat-form-field appearance="outline">
              <mat-label>Maintenance Date</mat-label>
              <input matInput [matDatepicker]="maintenancePicker" 
                     formControlName="MaintenanceDate" required>
              <mat-datepicker-toggle matSuffix [for]="maintenancePicker">
              </mat-datepicker-toggle>
              <mat-datepicker #maintenancePicker></mat-datepicker>
              <mat-error *ngIf="maintenanceForm.get('MaintenanceDate')?.hasError('required')">
                Maintenance date is required
              </mat-error>
            </mat-form-field>

            <mat-form-field appearance="outline">
              <mat-label>Next Due Date</mat-label>
              <input matInput [matDatepicker]="duePicker" 
                     formControlName="nextDueDate" required>
              <mat-datepicker-toggle matSuffix [for]="duePicker">
              </mat-datepicker-toggle>
              <mat-datepicker #duePicker></mat-datepicker>
              <mat-error *ngIf="maintenanceForm.get('nextDueDate')?.hasError('required')">
                Next due date is required
              </mat-error>
            </mat-form-field>
          </div>

          <mat-form-field appearance="outline">
            <mat-label>Technician</mat-label>
            <input matInput formControlName="Technician" required>
            <mat-icon matSuffix>person</mat-icon>
            <mat-error *ngIf="maintenanceForm.get('Technician')?.hasError('required')">
              Technician name is required
            </mat-error>
          </mat-form-field>

          <mat-form-field appearance="outline">
            <mat-label>Status</mat-label>
            <mat-select formControlName="maintenanceStatus" required>
              <mat-option *ngFor="let status of maintenanceStatuses" [value]="status">
                <mat-icon [color]="getStatusColor(status)">
                  {{getStatusIcon(status)}}
                </mat-icon>
                {{status}}
              </mat-option>
            </mat-select>
            <mat-error *ngIf="maintenanceForm.get('maintenanceStatus')?.hasError('required')">
              Status is required
            </mat-error>
          </mat-form-field>

          <mat-form-field appearance="outline">
            <mat-label>Details</mat-label>
            <textarea matInput formControlName="Details" 
                      rows="4" required 
                      placeholder="Enter maintenance details...">
            </textarea>
            <mat-icon matSuffix>description</mat-icon>
            <mat-error *ngIf="maintenanceForm.get('Details')?.hasError('required')">
              Details are required
            </mat-error>
          </mat-form-field>
        </form>
      </mat-dialog-content>

      <mat-dialog-actions align="end">
        <button mat-button color="basic" (click)="onCancel()">
          <mat-icon>close</mat-icon>
          Cancel
        </button>
        <button mat-raised-button color="primary" 
                [disabled]="!maintenanceForm.valid"
                (click)="onSubmit()">
          <mat-icon>{{isEdit ? 'save' : 'add'}}</mat-icon>
          {{ isEdit ? 'Update' : 'Add' }}
        </button>
      </mat-dialog-actions>
    </div>
  `,
  styles: [`
    .dialog-container {
      padding: 0;
      max-width: 800px;
    }

    mat-dialog-title {
      display: flex;
      align-items: center;
      gap: 8px;
      background: #1e1e1e;
      margin: -24px -24px 0 -24px !important;
      padding: 16px 24px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }

    mat-dialog-content {
      margin: 0 -24px;
      padding: 24px;
      max-height: 70vh;
    }

    .maintenance-form {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .form-row {
      display: flex;
      gap: 16px;
      
      mat-form-field {
        flex: 1;
      }
    }

    mat-form-field {
      width: 100%;
    }

    textarea {
      min-height: 100px;
      resize: vertical;
    }

    mat-dialog-actions {
      margin: 0 -24px -24px -24px;
      padding: 16px 24px;
      background: #1e1e1e;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    button {
      min-width: 120px;
    }

    mat-icon {
      margin-right: 8px;
    }

    @media (max-width: 600px) {
      .form-row {
        flex-direction: column;
      }
    }
  `]
})
export class MaintenanceRecordDialogComponent implements OnInit {
  maintenanceForm: FormGroup;
  isEdit = false;
  maintenanceTypes = Object.values(MaintenanceType);
  maintenanceStatuses = Object.values(MaintenanceStatus);
  maintenanceCategories = Object.values(MaintenanceCategory);

  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<MaintenanceRecordDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { 
      aircraftId: number, 
      record?: MaintenanceRecord 
    }
  ) {
    this.isEdit = !!data.record;
    this.maintenanceForm = this.fb.group({
      MaintenanceDate: ['', Validators.required],
      nextDueDate: ['', Validators.required],
      Details: ['', Validators.required],
      Technician: ['', Validators.required],
      maintenanceType: ['', Validators.required],
      maintenanceStatus: ['', Validators.required],
      maintenanceCategory: ['', Validators.required]
    });
  }

  ngOnInit() {
    if (this.isEdit && this.data.record) {
      this.maintenanceForm.patchValue({
        MaintenanceDate: new Date(this.data.record.MaintenanceDate),
        nextDueDate: new Date(this.data.record.nextDueDate),
        Details: this.data.record.Details,
        Technician: this.data.record.Technician,
        maintenanceType: this.data.record.maintenanceType,
        maintenanceStatus: this.data.record.maintenanceStatus,
        maintenanceCategory: this.data.record.maintenanceCategory
      });
    }
  }

  getMaintenanceTypeColor(type: MaintenanceType): string {
    switch (type) {
      case MaintenanceType.REPAIR:
        return 'warn';
      case MaintenanceType.INSPECTION:
        return 'accent';
      case MaintenanceType.ROUTINE:
        return 'primary';
      case MaintenanceType.OVERHAUL:
        return 'warn';
      default:
        return 'primary';
    }
  }

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

  onSubmit() {
    if (this.maintenanceForm.valid) {
      const formValue = this.maintenanceForm.value;
      const maintenanceRecord: MaintenanceRecord = {
        ...formValue,
        AircraftID: this.data.aircraftId,
        MaintenanceID: this.isEdit ? this.data.record!.MaintenanceID : 0
      };
      this.dialogRef.close(maintenanceRecord);
    }
  }

  onCancel() {
    this.dialogRef.close();
  }
}