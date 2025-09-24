// maintenanceRecord.routes.ts
import express from 'express';
import { MaintenanceRecordController } from './maintenanceRecord.controller';

const router = express.Router();
const maintenanceRecordController = new MaintenanceRecordController();

// Get all maintenance records
router.get('/', maintenanceRecordController.getAllMaintenanceRecords);

// Get maintenance records by aircraft ID
router.get('/aircraft/:aircraftId', maintenanceRecordController.getMaintenanceRecordsByAircraftId);

// Get specific maintenance record by ID
router.get('/:id([0-9]+)', maintenanceRecordController.getMaintenanceRecordById);

// Create new maintenance record for an aircraft
router.post('/aircraft/:aircraftId', maintenanceRecordController.createMaintenanceRecord);

// Update maintenance record for an aircraft
router.put('/aircraft/:aircraftId/:id', maintenanceRecordController.updateMaintenanceRecord);

// Delete maintenance record
router.delete('/aircraft/:aircraftId/:id', maintenanceRecordController.deleteMaintenanceRecord);

export default router;