// src/performanceRecord/performanceRecord.queries.ts

export const PerformanceRecordQueries = {
    SELECT_ALL: 'SELECT * FROM aircraft_maintenance.performancemetric',
    SELECT_BY_ID: 'SELECT * FROM aircraft_maintenance.performancemetric WHERE MetricID = ?',
    INSERT: `
    INSERT INTO aircraft_maintenance.performancemetric 
    (AircraftID, FlightTime, OilConsumption, FuelConsumption) 
    VALUES (?, ?, ?, ?)
  `.trim(),
    UPDATE: 'UPDATE aircraft_maintenance.performancemetric SET AircraftID = ?, FlightTime = ?, OilConsumption = ?, FuelConsumption = ? WHERE MetricID = ?',
    DELETE: 'DELETE FROM aircraft_maintenance.performancemetric WHERE MetricID = ?'
  };