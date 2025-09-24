
export enum AircraftStatus {
    READY = 'READY',
    NOT_READY = 'NOT READY',
    IN_MAINTENANCE = 'IN MAINTENANCE'
  }
  
  export enum MaintenanceStatus {
    SCHEDULED = 'SCHEDULED',
    IN_PROGRESS = 'IN_PROGRESS',
    COMPLETED = 'COMPLETED',
    DEFERRED = 'DEFERRED'
  }
  
  export enum MaintenanceCategory {
    ENGINE = 'ENGINE',
    AIRFRAME = 'AIRFRAME',
    AVIONICS = 'AVIONICS'
  }
  
  export enum MaintenanceType {
    ROUTINE = 'ROUTINE',
    REPAIR = 'REPAIR',
    INSPECTION = 'INSPECTION',
    OVERHAUL = 'OVERHAUL'
  }
  
  export interface Aircraft {
    aircraftID: number;
    model: string;
    serialNumber: string;
    dateOfManufacture: Date;
    flightTime: number;
    engineHours: number;
    status: AircraftStatus;
    lastMaintenanceDate?: Date;
    nextMaintenanceDate?: Date;
    maintenanceStatus?: MaintenanceStatus;
  }
  
  export interface MaintenanceRecord {
    MaintenanceID: number;
    AircraftID: number;
    MaintenanceDate: Date;
    Details: string;
    Technician: string;
    maintenanceType: MaintenanceType;
    nextDueDate: Date;
    maintenanceStatus: MaintenanceStatus;
    maintenanceCategory: MaintenanceCategory;
  }
  
  export interface PerformanceRecord {
    MetricID: number;
    AircraftID: number;
    FlightTime: number;
    OilConsumption: number;
    FuelConsumption: number;
  }