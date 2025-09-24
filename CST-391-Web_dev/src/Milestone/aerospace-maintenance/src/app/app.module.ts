import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { NgxChartsModule } from '@swimlane/ngx-charts';

// Material Imports
import { MatTableModule } from '@angular/material/table';
import { MatSortModule } from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatChipsModule } from '@angular/material/chips';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatSelectModule } from '@angular/material/select';
import { MatMenuModule } from '@angular/material/menu';

// Component Imports
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AircraftListComponent } from './components/aircraft-list/aircraft-list.component';
import { MaintenanceHistoryComponent } from './components/maintenance-history/maintenance-history.component';
import { AddAircraftDialogComponent } from './components/aircraft-list/add-aircraft-dialog/add-aircraft-dialog.component';
import { EditAircraftDialogComponent } from './components/aircraft-list/edit-aircraft-dialog/edit-aircraft-dialog.component';
import { ConfirmationDialogComponent } from './components/aircraft-list/confimation-dialog/confirmation-dialog.component';
import { MaintenanceRecordDialogComponent } from './components/maintenance-history/maintenance-record-dialog/maintenance-record-dialog.component';
import { PerformanceMetricsComponent } from './components/performance-metrics/performance-metrics.component';
import { PerformanceAnalyticsComponent } from './components/performance-analytics/performance-analytics.component';
import { AddPerformanceDialogComponent } from './components/performance-metrics/add-performance-dialog/add-performance-dialog.component';
import { EditPerformanceDialogComponent } from './components/performance-metrics/edit-performance-dialog/edit-performance-dialog.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { NavigationComponent } from './components/dashboard/navigation/navigation.component';


/**
 * The main module of the aerospace maintenance application.
 * 
 * This module declares all the components used in the application and imports
 * necessary Angular and third-party modules to provide required functionalities.
 * 
 */
@NgModule({
  declarations: [
    AppComponent,
    AircraftListComponent,
    MaintenanceHistoryComponent, 
    AddAircraftDialogComponent,
    EditAircraftDialogComponent,
    ConfirmationDialogComponent,
    MaintenanceRecordDialogComponent,
    PerformanceMetricsComponent,
    PerformanceAnalyticsComponent,
    AddPerformanceDialogComponent,
    EditPerformanceDialogComponent,
    DashboardComponent,
    NavigationComponent
    
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    CommonModule,
    NgxChartsModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule,
    MatTableModule,
    MatSortModule,
    MatButtonToggleModule,
    MatPaginatorModule,
    MatInputModule,
    MatCardModule,
    MatDividerModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatIconModule,
    MatButtonModule,
    MatChipsModule,
    MatTooltipModule,
    MatSidenavModule,
    MatProgressSpinnerModule,
    ReactiveFormsModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatSelectModule,
    MatDialogModule,
    MatMenuModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [NO_ERRORS_SCHEMA]
})
export class AppModule { }
