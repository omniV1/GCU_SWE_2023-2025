export const AircraftQueries = {
  SELECT_ALL: 'SELECT * FROM aircraft_maintenance.aircraft',
  SELECT_BY_ID: 'SELECT * FROM aircraft_maintenance.aircraft WHERE aircraftID = ?',
  INSERT: 'INSERT INTO aircraft_maintenance.aircraft (model, serialNumber, dateOfManufacture, flightTime, engineHours, status) VALUES (?, ?, ?, ?, ?, ?)',
  UPDATE: 'UPDATE aircraft_maintenance.aircraft SET model = ?, serialNumber = ?, dateOfManufacture = ?, flightTime = ?, engineHours = ?, status = ? WHERE aircraftID = ?',
  DELETE: 'DELETE FROM aircraft_maintenance.aircraft WHERE aircraftID = ?'
};