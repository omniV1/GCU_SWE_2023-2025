export enum AircraftStatus {
    READY = 'READY',
    NOT_READY = 'NOT_READY',
    IN_MAINTENANCE = 'IN_MAINTENANCE'
  }
  
  export enum MaintenanceStatus {
    COMPLETED = 'COMPLETED',
    IN_PROGRESS = 'IN_PROGRESS',
    SCHEDULED = 'SCHEDULED',
    DEFERRED = 'DEFERRED'
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

  export type NewAircraft = Omit<Aircraft, 'AircraftID'>;