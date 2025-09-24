export enum MaintenanceType {
  ROUTINE = 'ROUTINE',
  REPAIR = 'REPAIR',
  INSPECTION = 'INSPECTION',
  OVERHAUL = 'OVERHAUL'
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

export interface NewMaintenanceRecord {
  AircraftID: number;
  MaintenanceDate: Date;
  Details: string;
  Technician: string;
  maintenanceType: MaintenanceType;
  nextDueDate: Date;
  maintenanceStatus: MaintenanceStatus;
  maintenanceCategory: MaintenanceCategory;
}