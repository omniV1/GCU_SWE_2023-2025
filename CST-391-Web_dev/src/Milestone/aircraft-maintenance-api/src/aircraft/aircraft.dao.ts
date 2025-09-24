import { execute } from '../services/mysql.connector';
import { Aircraft, NewAircraft } from './aircraft.model';
import { AircraftQueries } from './aircraft.queries';
import moment from 'moment';

export class AircraftDAO {
  public async getAllAircraft(): Promise<Aircraft[]> {
    console.log('DAO: Getting all aircraft');
    try {
      const result = await execute<Aircraft[]>(AircraftQueries.SELECT_ALL, []);
      console.log(`DAO: Retrieved ${result.length} aircraft`);
      return result;
    } catch (error) {
      console.error('DAO: Error fetching aircraft from database:', error);
      throw error;
    }
  }

  public async getAircraftById(id: number): Promise<Aircraft | null> {
    console.log(`DAO: Getting aircraft with id ${id}`);
    try {
      const results = await execute<Aircraft[]>(AircraftQueries.SELECT_BY_ID, [id]);
      console.log(`DAO: Found ${results.length} aircraft for id ${id}`);
      return results.length ? results[0] : null;
    } catch (error) {
      console.error(`DAO: Error fetching aircraft with ID ${id}:`, error);
      throw error;
    }
  }

  public async createAircraft(aircraft: NewAircraft): Promise<number> {
    console.log('DAO: Creating new aircraft');
    try {
      const result = await execute<{ insertId: number }>(AircraftQueries.INSERT, [
        aircraft.model,
        aircraft.serialNumber,
        moment(aircraft.dateOfManufacture).format('YYYY-MM-DD'),
        aircraft.flightTime,
        aircraft.engineHours,
        aircraft.status
      ]);
      console.log('DAO: Create result:', result);
      return result.insertId;
    } catch (error) {
      console.error('DAO: Error creating aircraft:', error);
      throw error;
    }
  }


public async updateAircraft(id: number, aircraft: Partial<Aircraft>): Promise<boolean> {
  console.log(`DAO: Updating aircraft with id ${id}`);
  try {
      const setClause: string[] = [];
      const values: any[] = [];

      // Build dynamic update query based on provided fields
      if (aircraft.model !== undefined) {
          setClause.push('model = ?');
          values.push(aircraft.model);
      }
      if (aircraft.serialNumber !== undefined) {
          setClause.push('serialNumber = ?');
          values.push(aircraft.serialNumber);
      }
      if (aircraft.dateOfManufacture !== undefined) {
          setClause.push('dateOfManufacture = ?');
          values.push(aircraft.dateOfManufacture);
      }
      if (aircraft.flightTime !== undefined) {
          setClause.push('flightTime = ?');
          values.push(aircraft.flightTime);
      }
      if (aircraft.engineHours !== undefined) {
          setClause.push('engineHours = ?');
          values.push(aircraft.engineHours);
      }
      if (aircraft.status !== undefined) {
          setClause.push('status = ?');
          values.push(aircraft.status);
      }

      if (setClause.length === 0) {
          console.log('DAO: No fields to update');
          return false;
      }

      // Add the ID to the values array
      values.push(id);

      const query = `
          UPDATE aircraft_maintenance.aircraft 
          SET ${setClause.join(', ')} 
          WHERE aircraftID = ?
      `;

      console.log('DAO: Update query:', query);
      console.log('DAO: Update values:', values);

      const result = await execute<{ affectedRows: number }>(query, values);
      return result.affectedRows > 0;
  } catch (error) {
      console.error(`DAO: Error updating aircraft with id ${id}:`, error);
      throw error;
  }
}

  public async deleteAircraft(id: number): Promise<boolean> {
    console.log(`DAO: Deleting aircraft with id ${id}`);
    try {
      const result = await execute<{ affectedRows: number }>(AircraftQueries.DELETE, [id]);
      console.log('DAO: Delete result:', result);
      return result.affectedRows > 0;
    } catch (error) {
      console.error(`DAO: Error deleting aircraft with id ${id}:`, error);
      throw error;
    }
  }
}