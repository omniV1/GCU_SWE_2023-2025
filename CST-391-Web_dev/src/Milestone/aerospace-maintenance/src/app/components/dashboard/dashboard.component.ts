
/**
 * Dashboard component for aircraft maintenance management system
 * Displays overview statistics, quick actions, and navigation options
 */
import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { MatMenu } from '@angular/material/menu';
import { AircraftService } from '../../services/aircraft.service';
import { AircraftWithMaintenance } from '../../models/aircraft.model';
import { MaintenanceStatus } from '../../models/maintenance.model';

@Component({
  selector: 'app-dashboard',
  standalone: false, 
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  // References to Material menus for aircraft selection
  @ViewChild('maintenanceMenu') maintenanceMenu!: MatMenu;
  @ViewChild('performanceMenu') performanceMenu!: MatMenu;

  // Dashboard statistics
  totalAircraft: number = 0;
  maintenanceRequired: number = 0;
  totalFlightHours: number = 0;
  
  // Lists for aircraft data
  upcomingMaintenance: DashboardAircraft[] = [];
  aircraftList: AircraftWithMaintenance[] = [];

  constructor(
    private aircraftService: AircraftService,
    private router: Router
  ) {}

  ngOnInit() {
    this.loadDashboardData();
  }

  /**
   * Loads and processes dashboard data from the aircraft service
   * Calculates statistics and filters maintenance requirements
   */
  private loadDashboardData() {
    this.aircraftService.getAllAircraft().subscribe((aircraft: AircraftWithMaintenance[]) => {
      this.aircraftList = aircraft;
      
      // Calculate total aircraft count
      this.totalAircraft = aircraft.length;
      
      // Count aircraft requiring maintenance
      this.maintenanceRequired = aircraft.filter(a => 
        a.maintenanceStatus === MaintenanceStatus.DEFERRED || 
        a.maintenanceStatus === MaintenanceStatus.SCHEDULED
      ).length;
      
      // Calculate total flight hours across fleet
      this.totalFlightHours = aircraft.reduce((sum, a) => sum + (a.flightTime || 0), 0);
      
      // Get upcoming maintenance list (top 3)
      this.upcomingMaintenance = aircraft
        .filter(a => a.maintenanceStatus === MaintenanceStatus.SCHEDULED)
        .map(a => ({
          aircraftID: a.aircraftID,
          model: a.model,
          serialNumber: a.serialNumber,
          nextMaintenanceDate: a.nextMaintenanceDate
        }))
        .slice(0, 3);
    });
  }

  /**
   * Navigation methods for different sections
   */
  navigateToAircraft() {
    this.router.navigate(['/aircraft']);
  }

  navigateToMaintenance(aircraftId: number) {
    this.router.navigate(['/aircraft', aircraftId, 'maintenance']);
  }

  navigateToPerformance(aircraftId: number) {
    this.router.navigate(['/aircraft', aircraftId, 'performance']);
  }
}

/**
 * Interface for simplified aircraft data used in dashboard
 */
interface DashboardAircraft {
  aircraftID: number;
  model: string;
  serialNumber: string;
  nextMaintenanceDate?: Date;
}