/**
 * Types of maintenance activities
 */
export enum MaintenanceType {
    ROUTINE = 'ROUTINE',
    REPAIR = 'REPAIR',
    INSPECTION = 'INSPECTION',
    OVERHAUL = 'OVERHAUL'
}

/**
 * Current status of maintenance activities
 */
export enum MaintenanceStatus {
    SCHEDULED = 'SCHEDULED',
    IN_PROGRESS = 'IN_PROGRESS',
    COMPLETED = 'COMPLETED',
    DEFERRED = 'DEFERRED'
}

/**
 * Categories of maintenance work
 */
export enum MaintenanceCategory {
    ENGINE = 'ENGINE',
    AIRFRAME = 'AIRFRAME',
    AVIONICS = 'AVIONICS'
}

/**
 * Interface for maintenance record data
 */
export interface MaintenanceRecord {
    MaintenanceID: number;           // Primary identifier for maintenance record
    AircraftID: number;             // Reference to aircraft
    MaintenanceDate: Date;          // Date maintenance performed
    Details: string;                // Maintenance description
    Technician: string;             // Technician name
    maintenanceType: MaintenanceType;    // Type of maintenance
    nextDueDate: Date;                   // Next scheduled maintenance
    maintenanceStatus: MaintenanceStatus;// Current status
    maintenanceCategory: MaintenanceCategory; // Category of maintenance
}