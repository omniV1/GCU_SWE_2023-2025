export enum AircraftStatus {
  READY = 'ready',
  NOT_READY = 'not ready',
  IN_MAINTENANCE = 'in maintenance'
}

export interface Aircraft {
  aircraftID: number; // Match database column name
  model: string;
  serialNumber: string;
  dateOfManufacture: Date;
  flightTime: number;
  engineHours: number;
  status: AircraftStatus;
}

export type NewAircraft = Omit<Aircraft, 'aircraftID'>;