import { Request, Response, NextFunction } from 'express';
import moment from 'moment';
import { MaintenanceRecordDAO } from './maintenanceRecord.dao';
import { MaintenanceRecord, NewMaintenanceRecord } from './maintenanceRecord.model';

export class MaintenanceRecordController {
  private maintenanceRecordDAO: MaintenanceRecordDAO;

  constructor() {
    this.maintenanceRecordDAO = new MaintenanceRecordDAO();
  }

  public getAllMaintenanceRecords = async (req: Request, res: Response, next: NextFunction) => {
    console.log('Controller: getAllMaintenanceRecords method called');
    try {
      console.log('Controller: Calling DAO getAllMaintenanceRecords');
      const records = await this.maintenanceRecordDAO.getAllMaintenanceRecords();
      console.log(`Controller: Retrieved ${records.length} maintenance records`);
      console.log('Controller: First record:', records[0]);
      res.json(records);
    } catch (error) {
      console.error('Controller: Error getting all maintenance records:', error);
      next(error);
    }
  }

  public getMaintenanceRecordById = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      console.log('Invalid ID provided:', req.params.id);
      res.status(400).json({ message: 'Invalid ID provided' });
      return;
    }
    console.log(`Controller: Getting maintenance record with id ${id}`);
    try {
      const record = await this.maintenanceRecordDAO.getMaintenanceRecordById(id);
      if (record) {
        console.log('Controller: Maintenance record found:', record);
        res.json(record);
      } else {
        console.log(`Controller: No maintenance record found with id ${id}`);
        res.status(404).json({ message: 'Maintenance record not found' });
      }
    } catch (error) {
      console.error(`Controller: Error getting maintenance record with id ${id}:`, error);
      next(error);
    }
  }
  public getMaintenanceRecordsByAircraftId = async (req: Request, res: Response, next: NextFunction) => {
    const aircraftId = parseInt(req.params.aircraftId);
    console.log(`Controller: Getting maintenance records for aircraft ${aircraftId}`);
    try {
      const records = await this.maintenanceRecordDAO.getMaintenanceRecordsByAircraftId(aircraftId);
      if (records) {
        console.log(`Controller: Found ${records.length} maintenance records`);
        res.json(records);
      } else {
        console.log(`Controller: No maintenance records found for aircraft ${aircraftId}`);
        res.json([]);
      }
    } catch (error) {
      console.error(`Controller: Error getting maintenance records for aircraft ${aircraftId}:`, error);
      next(error);
    }
  }

  public createMaintenanceRecord = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    console.log('Controller: Creating new maintenance record');
    try {
      const newRecord: NewMaintenanceRecord = {
        ...req.body,
        MaintenanceDate: moment(req.body.MaintenanceDate).toDate()
      };
      console.log('Controller: New record data:', newRecord);
      const id = await this.maintenanceRecordDAO.createMaintenanceRecord(newRecord);
      console.log(`Controller: Created new maintenance record with id ${id}`);
      res.status(201).json({ MaintenanceID: id, ...newRecord });
    } catch (error) {
      console.error('Controller: Error creating maintenance record:', error);
      next(error);
    }
  }
  public updateMaintenanceRecord = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const id = parseInt(req.params.id, 10);
    const aircraftId = parseInt(req.params.aircraftId, 10);
    console.log(`Controller: Updating maintenance record with id ${id} for aircraft ${aircraftId}`);
    
    try {
        if (isNaN(id) || isNaN(aircraftId)) {
            console.log('Controller: Invalid ID or aircraft ID provided');
            res.status(400).json({ message: 'Invalid ID provided' });
            return;
        }

        const recordUpdate: Partial<MaintenanceRecord> = {
            ...req.body,
            AircraftID: aircraftId // Ensure the aircraft ID matches the URL
        };

        if (req.body.MaintenanceDate) {
            recordUpdate.MaintenanceDate = moment(req.body.MaintenanceDate).toDate();
        }

        console.log('Controller: Update data:', recordUpdate);

        const success = await this.maintenanceRecordDAO.updateMaintenanceRecord(id, recordUpdate);
        
        if (success) {
            console.log(`Controller: Successfully updated maintenance record with id ${id}`);
            res.json({ message: 'Maintenance record updated successfully' });
        } else {
            console.log(`Controller: No maintenance record found with id ${id} or no changes applied`);
            res.status(404).json({ message: 'Maintenance record not found or no changes applied' });
        }
    } catch (error) {
        console.error(`Controller: Error updating maintenance record with id ${id}:`, error);
        next(error);
    }
}

  public deleteMaintenanceRecord = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const id = parseInt(req.params.id);
    console.log(`Controller: Deleting maintenance record with id ${id}`);
    try {
      const success = await this.maintenanceRecordDAO.deleteMaintenanceRecord(id);
      if (success) {
        console.log(`Controller: Successfully deleted maintenance record with id ${id}`);
        res.status(204).send();
      } else {
        console.log(`Controller: No maintenance record found with id ${id}`);
        res.status(404).json({ message: 'Maintenance record not found' });
      }
    } catch (error) {
      console.error(`Controller: Error deleting maintenance record with id ${id}:`, error);
      next(error);
    }
  }
}