/**
 * Performance Analytics Component
 * Displays various performance metrics and charts for a specific aircraft
 * Uses ngx-charts for data visualization
 */
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AircraftService } from '../../services/aircraft.service';
import { Color, ScaleType, LegendPosition } from '@swimlane/ngx-charts';
import { PerformanceMetric } from '../../models/performance.model';




@Component({
  selector: 'app-performance-analytics',
  standalone: false, 
  templateUrl: './performance-analytics.component.html',
  styleUrls: ['./performance-analytics.component.scss'],
})
export class PerformanceAnalyticsComponent implements OnInit {
  // Color scheme definitions for different charts
  timelineColorScheme: Color = {
    name: 'timelineColors',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#2196F3']  // Blue theme for timeline
  };

  efficiencyColorScheme: Color = {
    name: 'efficiencyColors',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#4CAF50']  // Green theme for efficiency
  };

  gaugeColorScheme: Color = {
    name: 'gaugeColors',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#FF9800']  // Orange theme for gauge
  };

  // Component properties
  aircraftId: number = 0;
  performanceData: PerformanceMetric[] = [];
  trendData: any[] = [];        // Flight hours timeline data
  efficiencyData: any[] = [];   // Efficiency analysis data
  gaugeValue: any[] = [];       // Current fuel consumption data

  // Chart dimension configurations
  chartView: [number, number] = [500, 300];
  gaugeView: [number, number] = [400, 300];

  // Common chart configuration
  showXAxis = true;
  showYAxis = true;
  gradient = true;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  animations = true;
  timeline = false;

  // Gauge chart specific configuration
  gaugeMin = 0;
  gaugeMax = 3000;
  gaugeAngleSpan = 240;
  gaugeStartAngle = -120;
  gaugeShowAxis = true;
  gaugeLargeSegments = 10;
  gaugeSmallSegments = 5;
  gaugeUnits = "gal/hr";

  // Chart styling configuration
  backgroundGrid = true;
  backgroundColor = '#121212';
  gridLinesColor = 'rgba(255,255,255,0.1)';

  constructor(
    private route: ActivatedRoute,
    private aircraftService: AircraftService
  ) {}

  /**
   * Initialize component and load aircraft data
   */
  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');
    if (idParam) {
      this.aircraftId = +idParam;
      this.loadPerformanceData();
    }
  }

  /**
   * Load performance data for the selected aircraft
   */
  loadPerformanceData(): void {
    this.aircraftService.getPerformanceRecordsByAircraftId(this.aircraftId).subscribe({
      next: (records: PerformanceMetric[]) => {
        this.performanceData = records;
        this.formatChartData();
      },
      error: (error: Error) => {
        console.error('Error loading performance data:', error);
      }
    });
  }

  /**
   * Format raw performance data for different chart types
   */
  private formatChartData(): void {
    if (!this.performanceData || this.performanceData.length === 0) return;

    // Sort data chronologically
    const sortedData = [...this.performanceData].sort((a, b) => a.MetricID - b.MetricID);

    // Format data for flight hours timeline chart
    this.trendData = [{
      name: 'Flight Hours',
      series: sortedData.map(record => ({
        name: `ID ${record.MetricID}`,
        value: record.FlightTime
      }))
    }];

    // Format data for efficiency analysis bubble chart
    this.efficiencyData = [{
      name: 'Efficiency',
      series: sortedData.map(record => ({
        name: `ID ${record.MetricID}`,
        x: record.FlightTime,
        y: record.FuelConsumption,
        r: 8,
        value: record.FuelConsumption,
        tooltipText: `Flight Time: ${record.FlightTime} hrs\nFuel Rate: ${record.FuelConsumption} gal/hr`
      }))
    }];

    // Format data for fuel consumption gauge
    const currentFuelRate = sortedData[sortedData.length - 1]?.FuelConsumption || 0;
    this.gaugeMax = Math.max(3000, Math.ceil(currentFuelRate * 1.2));
    this.gaugeValue = [{
      name: "Current Consumption",
      value: currentFuelRate
    }];
  }

  /**
   * Calculate total flight hours from performance data
   */
  getTotalFlightHours(): number {
    if (!this.performanceData || this.performanceData.length === 0) return 0;
    return this.performanceData.reduce((sum, record) => sum + record.FlightTime, 0);
  }

  /**
   * Calculate average fuel efficiency from performance data
   */
  getAverageFuelEfficiency(): number {
    if (!this.performanceData || this.performanceData.length === 0) return 0;
    const validRecords = this.performanceData.filter(record => record.FuelConsumption > 0);
    if (validRecords.length === 0) return 0;
    const total = validRecords.reduce((sum, record) => sum + record.FuelConsumption, 0);
    return total / validRecords.length;
  }
}