export enum MaintenanceStatus {
    SCHEDULED = 'SCHEDULED',
    IN_PROGRESS = 'IN_PROGRESS',
    COMPLETED = 'COMPLETED',
    DEFERRED = 'DEFERRED'
}

export enum MaintenanceType {
    ROUTINE = 'ROUTINE',
    REPAIR = 'REPAIR',
    INSPECTION = 'INSPECTION',
    OVERHAUL = 'OVERHAUL'
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