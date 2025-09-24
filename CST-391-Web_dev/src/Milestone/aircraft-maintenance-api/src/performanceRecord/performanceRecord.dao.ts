import { execute } from '../services/mysql.connector';
import { PerformanceRecord, NewPerformanceRecord } from './performanceRecord.model';
import { PerformanceRecordQueries } from './performanceRecord.queries';

export class PerformanceRecordDAO {
  public async getAllPerformanceRecords(): Promise<PerformanceRecord[]> {
    console.log('DAO: Getting all performance records');
    try {
      const result = await execute<PerformanceRecord[]>(PerformanceRecordQueries.SELECT_ALL, []);
      console.log(`DAO: Retrieved ${result.length} performance records`);
      return result;
    } catch (error) {
      console.error('DAO: Error fetching performance records from database:', error);
      throw error;
    }
  }

  public async getPerformanceRecordById(id: number): Promise<PerformanceRecord | null> {
    console.log(`DAO: Getting performance record with id ${id}`);
    try {
      const results = await execute<PerformanceRecord[]>(PerformanceRecordQueries.SELECT_BY_ID, [id]);
      console.log(`DAO: Found ${results.length} performance records for id ${id}`);
      return results.length ? results[0] : null;
    } catch (error) {
      console.error(`DAO: Error fetching performance record with ID ${id}:`, error);
      throw error;
    }
  }
  public async getPerformanceRecordsByAircraftId(aircraftId: number): Promise<PerformanceRecord[]> {
    console.log(`DAO: Getting performance records for aircraft ${aircraftId}`);
    try {
      const results = await execute<PerformanceRecord[]>(
        'SELECT * FROM aircraft_maintenance.performancemetric WHERE AircraftID = ?',
        [aircraftId]
      );
      console.log(`DAO: Found ${results.length} performance records for aircraft ${aircraftId}`);
      return results;
    } catch (error) {
      console.error(`DAO: Error fetching performance records for aircraft ${aircraftId}:`, error);
      throw error;
    }
  }
  public async createPerformanceRecord(record: NewPerformanceRecord): Promise<number> {
    console.log('DAO: Creating new performance record with data:', record); // Add this log
    try {
      const result = await execute<{ insertId: number }>(PerformanceRecordQueries.INSERT, [
        record.AircraftID,  // Make sure this matches your database column name
        record.FlightTime,
        record.OilConsumption,
        record.FuelConsumption
      ]);
      return result.insertId;
    } catch (error) {
      console.error('DAO: Error creating performance record:', error);
      throw error;
    }
  }

  public async updatePerformanceRecord(id: number, record: Partial<PerformanceRecord>): Promise<boolean> {
    console.log(`DAO: Updating performance record with id ${id}`);
    try {
      const setClause: string[] = [];
      const values: any[] = [];

      if (record.AircraftID !== undefined) {
        setClause.push('AircraftID = ?');
        values.push(record.AircraftID);
      }
      if (record.FlightTime !== undefined) {
        setClause.push('FlightTime = ?');
        values.push(record.FlightTime);
      }
      if (record.OilConsumption !== undefined) {
        setClause.push('OilConsumption = ?');
        values.push(record.OilConsumption);
      }
      if (record.FuelConsumption !== undefined) {
        setClause.push('FuelConsumption = ?');
        values.push(record.FuelConsumption);
      }

      if (setClause.length === 0) {
        console.log('DAO: No fields to update');
        return false;
      }

      const query = `UPDATE aircraft_maintenance.performancemetric SET ${setClause.join(', ')} WHERE MetricID = ?`;
      values.push(id);

      console.log('DAO: Update query:', query);
      console.log('DAO: Update values:', values);

      const result = await execute<{ affectedRows: number }>(query, values);
      console.log('DAO: Update result:', result);
      return result.affectedRows > 0;
    } catch (error) {
      console.error(`DAO: Error updating performance record with id ${id}:`, error);
      throw error;
    }
  }

  public async deletePerformanceRecord(id: number): Promise<boolean> {
    console.log(`DAO: Deleting performance record with id ${id}`);
    try {
      const result = await execute<{ affectedRows: number }>(PerformanceRecordQueries.DELETE, [id]);
      console.log('DAO: Delete result:', result);
      return result.affectedRows > 0;
    } catch (error) {
      console.error(`DAO: Error deleting performance record with id ${id}:`, error);
      throw error;
    }
  }
}