export const MaintenanceRecordQueries = {
  SELECT_ALL: 'SELECT * FROM aircraft_maintenance.maintenancerecord',
  SELECT_BY_ID: 'SELECT * FROM aircraft_maintenance.maintenancerecord WHERE MaintenanceID = ?',
  INSERT: `
        INSERT INTO aircraft_maintenance.maintenancerecord 
        (AircraftID, MaintenanceDate, Details, Technician, 
         maintenanceType, nextDueDate, maintenanceStatus, maintenanceCategory) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `,
  UPDATE: `
      UPDATE aircraft_maintenance.maintenancerecord 
      SET AircraftID = ?, 
          MaintenanceDate = ?, 
          Details = ?, 
          Technician = ?,
          maintenanceType = ?,
          nextDueDate = ?,
          maintenenaceStatus = ?,
          maintenanceCategory = ?
      WHERE MaintenanceID = ?
  `,
  DELETE: 'DELETE FROM aircraft_maintenance.maintenancerecord WHERE MaintenanceID = ?',
  
  // Additional useful queries
  SELECT_BY_AIRCRAFT: 'SELECT * FROM aircraft_maintenance.maintenancerecord WHERE AircraftID = ? ORDER BY MaintenanceDate DESC',
  SELECT_LATEST_BY_AIRCRAFT: `
      SELECT * FROM aircraft_maintenance.maintenancerecord 
      WHERE AircraftID = ? 
      ORDER BY MaintenanceDate DESC 
      LIMIT 1
  `
};