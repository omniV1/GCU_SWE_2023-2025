import axios from 'axios';

const API_BASE_URL = 'http://localhost:5240/api';
const AIRCRAFTS_URL = `${API_BASE_URL}/aircrafts`;
const MAINTENANCE_RECORDS_URL = `${API_BASE_URL}/MaintenanceRecords`;

export const getAircrafts = async () => {
    return await axios.get(AIRCRAFTS_URL);
};

export const getAircraftById = async (id) => {
    return await axios.get(`${AIRCRAFTS_URL}/${id}`);
};

export const createAircraft = async (aircraft) => {
    return await axios.post(AIRCRAFTS_URL, aircraft);
};

export const updateAircraft = async (id, aircraft) => {
    return await axios.put(`${AIRCRAFTS_URL}/${id}`, aircraft);
};

export const deleteAircraft = async (id) => {
    return await axios.delete(`${AIRCRAFTS_URL}/${id}`);
};

export const getMaintenanceRecordsByAircraftId = async (id) => {
    return await axios.get(`${AIRCRAFTS_URL}/${id}/maintenance-records`);
};

export const addMaintenanceRecord = async (record) => {
    return await axios.post(MAINTENANCE_RECORDS_URL, record);
};

export const updateMaintenanceRecord = async (id, record) => {
    return await axios.put(`${MAINTENANCE_RECORDS_URL}/${id}`, record);
};

export const getMaintenanceRecord = async (id) => {
    return await axios.get(`${MAINTENANCE_RECORDS_URL}/${id}`);
};

export const deleteMaintenanceRecord = async (id) => {
    try {
        await fetch(`http://localhost:5240/api/MaintenanceRecords/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        });
    } catch (error) {
        console.error('Error deleting maintenance record:', error);
        throw error;
    }
};