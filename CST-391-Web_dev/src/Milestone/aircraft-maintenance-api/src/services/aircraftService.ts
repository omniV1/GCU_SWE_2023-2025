// src/services/aircraftService.ts

import { execute } from './mysql.connector';
import { Aircraft, NewAircraft } from '../aircraft/aircraft.model';

export const getAllAircraft = async (): Promise<Aircraft[]> => {
    const query = 'SELECT * FROM Aircraft';
    return execute<Aircraft[]>(query, []);
};

export const getAircraftById = async (id: number): Promise<Aircraft | null> => {
    const query = 'SELECT * FROM Aircraft WHERE id = ?';
    const results = await execute<Aircraft[]>(query, [id]);
    return results.length > 0 ? results[0] : null;
};

export const createAircraft = async (aircraft: NewAircraft): Promise<number> => {
    const query = 'INSERT INTO Aircraft (model, serialNumber, lastMaintenanceDate, maintenancePerformed, totalFlightTime, status) VALUES (?, ?, ?, ?, ?, ?)';
    const result = await execute<{ insertId: number }>(query, [
        aircraft.model,
        aircraft.serialNumber,
        aircraft.flightTime,
        aircraft.engineHours,
        aircraft.dateOfManufacture,
        aircraft.status,
    ]);
    return result.insertId;
};

export const updateAircraft = async (id: number, aircraft: Partial<Aircraft>): Promise<boolean> => {
    const fields = Object.keys(aircraft).map(key => `${key} = ?`).join(', ');
    const values = Object.values(aircraft);
    const query = `UPDATE Aircraft SET ${fields} WHERE id = ?`;
    const result = await execute<{ affectedRows: number }>(query, [...values, id]);
    return result.affectedRows > 0;
};

export const deleteAircraft = async (id: number): Promise<boolean> => {
    const query = 'DELETE FROM Aircraft WHERE id = ?';
    const result = await execute<{ affectedRows: number }>(query, [id]);
    return result.affectedRows > 0;
};