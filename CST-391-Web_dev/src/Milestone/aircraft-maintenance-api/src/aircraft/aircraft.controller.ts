// aircraft.controller.ts
import { Request, Response, NextFunction } from 'express';
import { AircraftDAO } from './aircraft.dao';
import { NewAircraft, Aircraft } from './aircraft.model';

export class AircraftController {
  private aircraftDAO: AircraftDAO;

  constructor() {
    this.aircraftDAO = new AircraftDAO();
  }

  public getAllAircraft = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const aircraft = await this.aircraftDAO.getAllAircraft();
      res.json(aircraft);
    } catch (error) {
      next(error);
    }
  };

  public getAircraftById = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const id = parseInt(req.params.id);
      const aircraft = await this.aircraftDAO.getAircraftById(id);
      if (aircraft) {
        res.json(aircraft);
      } else {
        res.status(404).json({ message: 'Aircraft not found' });
      }
    } catch (error) {
      next(error);
    }
  };

  public createAircraft = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const newAircraft: NewAircraft = req.body;
      const id = await this.aircraftDAO.createAircraft(newAircraft);
      res.status(201).json({ id, ...newAircraft });
    } catch (error) {
      next(error);
    }
  };

  public updateAircraft = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const id = parseInt(req.params.id);
      const success = await this.aircraftDAO.updateAircraft(id, req.body);
      if (success) {
        res.json({ message: 'Aircraft updated successfully' });
      } else {
        res.status(404).json({ message: 'Aircraft not found' });
      }
    } catch (error) {
      next(error);
    }
  };

  public deleteAircraft = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const id = parseInt(req.params.id);
      const success = await this.aircraftDAO.deleteAircraft(id);
      if (success) {
        res.status(204).send();
      } else {
        res.status(404).json({ message: 'Aircraft not found' });
      }
    } catch (error) {
      next(error);
    }
  };
}