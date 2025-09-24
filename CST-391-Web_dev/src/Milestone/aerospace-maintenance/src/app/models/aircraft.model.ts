import { MaintenanceStatus } from './maintenance.model';

export enum AircraftStatus {
    READY = 'ready',
    NOT_READY = 'not ready',
    IN_MAINTENANCE = 'in maintenance'
}

export interface Aircraft {
    aircraftID: number;  // Changed from aircraftid to match your API response
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

/**
 * Interface for aircraft data with maintenance information
 */
/**
 * Interface representing an aircraft with maintenance details.
 * 
 * @property {number} aircraftID - Unique identifier for the aircraft.
 * @property {string} model - Model of the aircraft.
 * @property {string} serialNumber - Serial number of the aircraft.
 * @property {Date} dateOfManufacture - Date when the aircraft was manufactured.
 * @property {number} flightTime - Total flight time of the aircraft in hours.
 * @property {number} engineHours - Total engine hours of the aircraft.
 * @property {AircraftStatus} status - Current status of the aircraft.
 * @property {Date} [lastMaintenanceDate] - Date when the aircraft last underwent maintenance (optional).
 * @property {Date} [nextMaintenanceDate] - Date when the aircraft is scheduled for next maintenance (optional).
 * @property {MaintenanceStatus} [maintenanceStatus] - Current maintenance status of the aircraft (optional).
 */
export interface AircraftWithMaintenance {
    aircraftID: number;
    model: string;
    serialNumber: string;
    dateOfManufacture: Date;
    flightTime: number;
    engineHours: number;
    status: AircraftStatus;
    // Optional maintenance-related fields
    lastMaintenanceDate?: Date;
    nextMaintenanceDate?: Date;
    maintenanceStatus?: MaintenanceStatus;
  }