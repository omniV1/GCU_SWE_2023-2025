/**
 * Generic confirmation dialog component used throughout the application
 * for user confirmations before critical actions (delete, update, etc.)
 * 
 * @usage
 * const dialogRef = dialog.open(ConfirmationDialogComponent, {
 *   data: { title: 'Confirm Delete', message: 'Are you sure?' }
 * });
 */
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-confirmation-dialog',
  standalone: false, 
  templateUrl: './confirmation-dialog.component.html',
  styleUrls: ['./confirmation-dialog.component.scss'],
})
export class ConfirmationDialogComponent {
  /**
   * @param dialogRef - Reference to the dialog instance for closing/passing data back
   * @param data - Dialog data containing title and message to display
   */
  constructor(
    private dialogRef: MatDialogRef<ConfirmationDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { title: string; message: string }
  ) {}

  /**
   * Closes the dialog with true value indicating user confirmed the action
   */
  confirm() {
    this.dialogRef.close(true);
  }

  /**
   * Closes the dialog with false value indicating user cancelled the action
   */
  cancel() {
    this.dialogRef.close(false);
  }
}