/**
 * Types of performance metrics tracked
 */
export enum MetricType {
  FLIGHT_TIME = 'FLIGHT_TIME',
  OIL_CONSUMPTION = 'OIL_CONSUMPTION',
  FUEL_CONSUMPTION = 'FUEL_CONSUMPTION',
  MAINTENANCE_TIME = 'MAINTENANCE_TIME'
}

/**
 * Interface for performance metric records
 */
export interface PerformanceMetric {
  MetricID: number;          // Primary identifier
  AircraftID: number;        // Reference to aircraft
  FlightTime: number;        // Hours flown
  OilConsumption: number;    // Oil usage
  FuelConsumption: number;//  fuel consumption
}

/**
 * Type for new performance metrics (without ID)
 */
export type NewPerformanceMetric = Omit<PerformanceMetric, 'MetricID'>;