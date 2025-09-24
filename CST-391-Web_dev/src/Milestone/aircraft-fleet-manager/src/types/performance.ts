// src/types/performance.ts
export interface PerformanceMetric {
    MetricID: number;
    AircraftID: number;
    FlightTime: number;
    OilConsumption: number;
    FuelConsumption: number;
  }
  
  export type NewPerformanceMetric = Omit<PerformanceMetric, 'MetricID'>;