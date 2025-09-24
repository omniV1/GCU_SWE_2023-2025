// src/performanceRecord/performanceRecord.model.ts

export interface PerformanceRecord {
    MetricID: number;
    AircraftID: number;
    FlightTime: number;
    OilConsumption: number;
    FuelConsumption: number;
  }
  
  export type NewPerformanceRecord = Omit<PerformanceRecord, 'MetricID'>;