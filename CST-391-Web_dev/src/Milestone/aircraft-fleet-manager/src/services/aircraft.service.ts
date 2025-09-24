// src/services/aircraft.service.ts

import axios from 'axios';
import { Aircraft, MaintenanceRecord, MaintenanceStatus } from '../types';
import { PerformanceMetric } from '../types/performance';

const API_URL = 'http://localhost:5000/api';

function calculateMaintenanceStatus(nextDueDate?: Date): MaintenanceStatus {
  if (!nextDueDate) return MaintenanceStatus.SCHEDULED;

  const today = new Date();
  const daysUntilMaintenance = Math.ceil(
    (new Date(nextDueDate).getTime() - today.getTime()) / (1000 * 3600 * 24)
  );

  if (daysUntilMaintenance < 0) return MaintenanceStatus.DEFERRED;
  if (daysUntilMaintenance <= 3) return MaintenanceStatus.IN_PROGRESS;
  return MaintenanceStatus.SCHEDULED;
}

export const aircraftService = {
  getAllAircraft: async (): Promise<Aircraft[]> => {
    try {
      // Fetch both aircraft and maintenance data in parallel
      const [aircraftResponse, maintenanceResponse] = await Promise.all([
        axios.get(`${API_URL}/aircraft`),
        axios.get(`${API_URL}/maintenancerecord`)
      ]);

      const aircraft = aircraftResponse.data;
      const maintenanceRecords = maintenanceResponse.data;

      // Merge maintenance data with aircraft data
      return aircraft.map((aircraft: Aircraft) => {
        const aircraftMaintenance = maintenanceRecords
          .filter((record: MaintenanceRecord) => record.AircraftID === aircraft.aircraftID)
          .sort((a: MaintenanceRecord, b: MaintenanceRecord) =>
            new Date(b.MaintenanceDate).getTime() - new Date(a.MaintenanceDate).getTime()
          );

        const latestMaintenance = aircraftMaintenance[0];

        return {
          ...aircraft,
          lastMaintenanceDate: latestMaintenance ? new Date(latestMaintenance.MaintenanceDate) : undefined,
          nextMaintenanceDate: latestMaintenance?.nextDueDate ? new Date(latestMaintenance.nextDueDate) : undefined,
          maintenanceStatus: calculateMaintenanceStatus(latestMaintenance?.nextDueDate)
        };
      });
    } catch (error) {
      console.error('Error fetching aircraft data:', error);
      throw error;
    }
  },

  getAllPerformanceRecords: async (): Promise<PerformanceMetric[]> => {
    try {
      const response = await axios.get(`${API_URL}/performance`);
      return response.data;
    } catch (error) {
      console.error('Error fetching performance records:', error);
      throw error;
    }
  },

  getAircraftById: async (id: number): Promise<Aircraft> => {
    const response = await axios.get(`${API_URL}/aircraft/${id}`);
    return response.data;
  },

  createAircraft: async (aircraft: Omit<Aircraft, 'aircraftID'>): Promise<Aircraft> => {
    const response = await axios.post(`${API_URL}/aircraft`, aircraft);
    return response.data;
  },

  updateAircraft: async (id: number, aircraft: Partial<Aircraft>): Promise<Aircraft> => {
    const response = await axios.put(`${API_URL}/aircraft/${id}`, aircraft);
    return response.data;
  },

  deleteAircraft: async (id: number): Promise<void> => {
    await axios.delete(`${API_URL}/aircraft/${id}`);
  },

  // Maintenance Operations
  getMaintenanceHistory: async (aircraftId: number): Promise<MaintenanceRecord[]> => {
    const response = await axios.get(`${API_URL}/maintenancerecord/aircraft/${aircraftId}`);
    return response.data;
  },

  createMaintenanceRecord: async (aircraftId: number, record: Omit<MaintenanceRecord, 'MaintenanceID'>): Promise<MaintenanceRecord> => {
    const response = await axios.post(`${API_URL}/maintenancerecord/aircraft/${aircraftId}`, record);
    return response.data;
  },

  updateMaintenanceRecord: async (aircraftId: number, record: MaintenanceRecord): Promise<MaintenanceRecord> => {
    const response = await axios.put(`${API_URL}/maintenancerecord/aircraft/${aircraftId}/${record.MaintenanceID}`, record);
    return response.data;
  },

  deleteMaintenanceRecord: async (aircraftId: number, recordId: number): Promise<void> => {
    await axios.delete(`${API_URL}/maintenancerecord/aircraft/${aircraftId}/${recordId}`);
  },

  // Performance Operations
  getPerformanceRecords: async (aircraftId: number): Promise<PerformanceMetric[]> => {
    const response = await axios.get(`${API_URL}/performance/aircraft/${aircraftId}`);
    return response.data;
  },
  getPerformanceMetricById: async (metricId: number): Promise<PerformanceMetric> => {
    try {
      const response = await axios.get(`${API_URL}/Performance/${metricId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching performance metric:', error);
      throw error;
    }
  },
  createPerformanceRecord: async (aircraftId: number, record: Omit<PerformanceMetric, 'MetricID'>): Promise<PerformanceMetric> => {
    const response = await axios.post(`${API_URL}/performance`, { ...record, AircraftID: aircraftId });
    return response.data;
  },

  updatePerformanceRecord: async (aircraftId: number, record: PerformanceMetric): Promise<PerformanceMetric> => {
    const response = await axios.put(`${API_URL}/performance/${record.MetricID}`, record);
    return response.data;
  },

  deletePerformanceRecord: async (aircraftId: number, recordId: number): Promise<void> => {
    await axios.delete(`${API_URL}/performance/${recordId}`);
  }
};