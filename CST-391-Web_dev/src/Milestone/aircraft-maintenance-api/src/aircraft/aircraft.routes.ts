// aircraft.routes.ts
import { Router, Request, Response, NextFunction } from 'express';
import { AircraftController } from './aircraft.controller';

const router = Router();
const controller = new AircraftController();

// Wrap controller methods to ensure proper error handling
const asyncHandler = (fn: (req: Request, res: Response, next: NextFunction) => Promise<void>) => 
  (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };

router.get('/', asyncHandler(controller.getAllAircraft));
router.get('/:id', asyncHandler(controller.getAircraftById));
router.post('/', asyncHandler(controller.createAircraft));
router.put('/:id', asyncHandler(controller.updateAircraft));
router.delete('/:id', asyncHandler(controller.deleteAircraft));

export default router;