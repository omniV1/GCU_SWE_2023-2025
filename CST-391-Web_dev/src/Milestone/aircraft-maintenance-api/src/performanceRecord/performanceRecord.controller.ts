import { Request, Response, NextFunction } from 'express';
import { PerformanceRecordDAO } from './performanceRecord.dao';
import { NewPerformanceRecord, PerformanceRecord } from './performanceRecord.model';

export class PerformanceRecordController {
  private performanceRecordDAO: PerformanceRecordDAO;

  constructor() {
    this.performanceRecordDAO = new PerformanceRecordDAO();
  }

  public getAllPerformanceRecords = async (req: Request, res: Response, next: NextFunction) => {
    console.log('Controller: Getting all performance records');
    try {
      const records = await this.performanceRecordDAO.getAllPerformanceRecords();
      console.log(`Controller: Retrieved ${records.length} performance records`);
      res.json(records);
    } catch (error) {
      console.error('Controller: Error getting all performance records:', error);
      next(error);
    }
  }
  public getPerformanceRecordsByAircraftId = async (req: Request, res: Response, next: NextFunction) => {
    const aircraftId = parseInt(req.params.aircraftId);
    console.log(`Controller: Getting performance records for aircraft ${aircraftId}`);
    
    try {
      // Add this method to your DAO
      const records = await this.performanceRecordDAO.getPerformanceRecordsByAircraftId(aircraftId);
      if (records) {
        console.log(`Controller: Found ${records.length} performance records`);
        res.json(records);
      } else {
        console.log(`Controller: No performance records found for aircraft ${aircraftId}`);
        res.json([]);
      }
    } catch (error) {
      console.error(`Controller: Error getting performance records for aircraft ${aircraftId}:`, error);
      next(error);
    }
  };
  public getPerformanceRecordById = async (req: Request, res: Response, next: NextFunction) => {
    const id = parseInt(req.params.id);
    console.log(`Controller: Getting performance record with id ${id}`);
    try {
      const record = await this.performanceRecordDAO.getPerformanceRecordById(id);
      if (record) {
        console.log('Controller: Performance record found:', record);
        res.json(record);
      } else {
        console.log(`Controller: No performance record found with id ${id}`);
        res.status(404).json({ message: 'Performance record not found' });
      }
    } catch (error) {
      console.error(`Controller: Error getting performance record with id ${id}:`, error);
      next(error);
    }
  }

  public createPerformanceRecord = async (req: Request, res: Response, next: NextFunction) => {
    console.log('Controller: Creating new performance record');
    try {
      const newRecord: NewPerformanceRecord = req.body;
      console.log('Controller: New performance record data:', newRecord);
      const id = await this.performanceRecordDAO.createPerformanceRecord(newRecord);
      console.log(`Controller: Created new performance record with id ${id}`);
      res.status(201).json({ MetricID: id, ...newRecord });
    } catch (error) {
      console.error('Controller: Error creating performance record:', error);
      next(error);
    }
  }

  public updatePerformanceRecord = async (req: Request, res: Response, next: NextFunction) => {
    const id = parseInt(req.params.id);
    console.log(`Controller: Updating performance record with id ${id}`);
    try {
      const recordUpdate: Partial<PerformanceRecord> = req.body;
      console.log('Controller: Performance record update data:', recordUpdate);
      const success = await this.performanceRecordDAO.updatePerformanceRecord(id, recordUpdate);
      if (success) {
        console.log(`Controller: Successfully updated performance record with id ${id}`);
        res.json({ message: 'Performance record updated successfully' });
      } else {
        console.log(`Controller: No performance record found with id ${id}`);
        res.status(404).json({ message: 'Performance record not found' });
      }
    } catch (error) {
      console.error(`Controller: Error updating performance record with id ${id}:`, error);
      next(error);
    }
  }

  public deletePerformanceRecord = async (req: Request, res: Response, next: NextFunction) => {
    const id = parseInt(req.params.id);
    console.log(`Controller: Deleting performance record with id ${id}`);
    try {
      const success = await this.performanceRecordDAO.deletePerformanceRecord(id);
      if (success) {
        console.log(`Controller: Successfully deleted performance record with id ${id}`);
        res.status(204).send();
      } else {
        console.log(`Controller: No performance record found with id ${id}`);
        res.status(404).json({ message: 'Performance record not found' });
      }
    } catch (error) {
      console.error(`Controller: Error deleting performance record with id ${id}:`, error);
      next(error);
    }
  }
}