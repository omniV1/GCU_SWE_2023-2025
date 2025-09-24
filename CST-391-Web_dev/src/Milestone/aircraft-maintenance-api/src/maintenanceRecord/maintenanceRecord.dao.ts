import { format } from 'path';
import { execute } from '../services/mysql.connector';
import { MaintenanceRecord, NewMaintenanceRecord } from './maintenanceRecord.model';
import { MaintenanceRecordQueries } from './maintenanceRecord.queries';
import moment from 'moment';

export class MaintenanceRecordDAO {
  public async getAllMaintenanceRecords(): Promise<MaintenanceRecord[]> {
    console.log('DAO: Getting all maintenance records');
    try {
      const result = await execute<MaintenanceRecord[]>(MaintenanceRecordQueries.SELECT_ALL, []);
      console.log(`DAO: Retrieved ${result.length} maintenance records`);
      return result;
    } catch (error) {
      console.error('DAO: Error fetching maintenance records:', error);
      throw error;
    }
  }
  public async getMaintenanceRecordsByAircraftId(aircraftId: number): Promise<MaintenanceRecord[]> {
    console.log(`DAO: Getting maintenance records for aircraft ${aircraftId}`);
    try {
      const results = await execute<MaintenanceRecord[]>(
        MaintenanceRecordQueries.SELECT_BY_AIRCRAFT, 
        [aircraftId]
      );
      console.log(`DAO: Found ${results.length} records for aircraft ${aircraftId}`);
      return results;
    } catch (error) {
      console.error(`DAO: Error fetching maintenance records for aircraft ${aircraftId}:`, error);
      throw error;
    }
  }
  public async getMaintenanceRecordById(id: number): Promise<MaintenanceRecord | null> {
    if (isNaN(id)) {
      console.log('DAO: Invalid ID provided:', id);
      return null;
    }
    console.log(`DAO: Getting maintenance record with id ${id}`);
    try {
      const results = await execute<MaintenanceRecord[]>(MaintenanceRecordQueries.SELECT_BY_ID, [id]);
      console.log(`DAO: Found ${results.length} records for id ${id}`);
      return results.length ? results[0] : null;
    } catch (error) {
      console.error(`DAO: Error fetching maintenance record with id ${id}:`, error);
      throw error;
    }
  }
  public async createMaintenanceRecord(record: NewMaintenanceRecord): Promise<number> {
    console.log('DAO: Creating new maintenance record');
    try {
        if (!(await this.checkAircraftExists(record.AircraftID))) {
            throw new Error(`Aircraft with ID ${record.AircraftID} does not exist`);
        }

        const formattedDate = moment(record.MaintenanceDate).format('YYYY-MM-DD HH:mm:ss');
        const nextDueDate = moment(record.nextDueDate).format('YYYY-MM-DD HH:mm:ss');
        
        const result = await execute<{ insertId: number }>(
            MaintenanceRecordQueries.INSERT,
            [
                record.AircraftID,
                formattedDate,
                record.Details,
                record.Technician,
                record.maintenanceType,
                nextDueDate,
                record.maintenanceStatus,
                record.maintenanceCategory
            ]
        );

        console.log('DAO: Create result:', result);
        return result.insertId;
    } catch (error) {
        console.error('DAO: Error creating maintenance record:', error);
        throw error;
    }
}

public async updateMaintenanceRecord(id: number, record: Partial<MaintenanceRecord>): Promise<boolean> {
  console.log(`DAO: Updating maintenance record with id ${id}`);
  console.log('DAO: Update data:', record);
  try {
      if (!(await this.checkMaintenanceRecordExists(id))) {
          console.log(`DAO: Maintenance record with id ${id} does not exist`);
          return false;
      }

      const setClause: string[] = [];
      const values: any[] = [];

      // Log all the fields we're updating
      Object.entries(record).forEach(([key, value]) => {
          console.log(`Setting ${key} = ${value}`);
      });

      if (record.AircraftID !== undefined) {
          setClause.push('AircraftID = ?');
          values.push(record.AircraftID);
      }
      if (record.MaintenanceDate !== undefined) {
          setClause.push('MaintenanceDate = ?');
          values.push(moment(record.MaintenanceDate).format('YYYY-MM-DD HH:mm:ss'));
      }
      if (record.Details !== undefined) {
          setClause.push('Details = ?');
          values.push(record.Details);
      }
      if (record.Technician !== undefined) {
          setClause.push('Technician = ?');
          values.push(record.Technician);
      }
      if (record.maintenanceType !== undefined) {
          setClause.push('maintenanceType = ?');
          values.push(record.maintenanceType);
      }
      if (record.maintenanceStatus !== undefined) {
          setClause.push('maintenanceStatus = ?');
          values.push(record.maintenanceStatus);
      }
      if (record.maintenanceCategory !== undefined) {
          setClause.push('maintenanceCategory = ?');
          values.push(record.maintenanceCategory);
      }
      if (record.nextDueDate !== undefined) {
          setClause.push('nextDueDate = ?');
          values.push(moment(record.nextDueDate).format('YYYY-MM-DD HH:mm:ss'));
      }

      if (setClause.length === 0) {
          console.log('DAO: No fields to update');
          return false;
      }

      const query = `UPDATE aircraft_maintenance.maintenancerecord SET ${setClause.join(', ')} WHERE MaintenanceID = ?`;
      values.push(id);

      console.log('DAO: Executing query:', query);
      console.log('DAO: With values:', values);

      const result = await execute<{ affectedRows: number }>(query, values);
      console.log('DAO: Update result:', result);
      return result.affectedRows > 0;
  } catch (error) {
      console.error(`DAO: Error updating maintenance record with id ${id}:`, error);
      throw error;
  }
}

  public async deleteMaintenanceRecord(id: number): Promise<boolean> {
    console.log(`DAO: Deleting maintenance record with id ${id}`);
    try {
      if (!(await this.checkMaintenanceRecordExists(id))) {
        console.log(`DAO: Maintenance record with id ${id} does not exist`);
        return false;
      }
      const result = await execute<{ affectedRows: number }>(MaintenanceRecordQueries.DELETE, [id]);
      console.log('DAO: Delete result:', result);
      return result.affectedRows > 0;
    } catch (error) {
      console.error(`DAO: Error deleting maintenance record with id ${id}:`, error);
      throw error;
    }
  }

  private async checkAircraftExists(aircraftId: number): Promise<boolean> {
    const result = await execute<any[]>('SELECT 1 FROM aircraft WHERE AircraftID = ?', [aircraftId]);
    return result.length > 0;
  }

  private async checkMaintenanceRecordExists(id: number): Promise<boolean> {
    const result = await execute<any[]>('SELECT 1 FROM maintenancerecord WHERE MaintenanceID = ?', [id]);
    return result.length > 0;
  }
}