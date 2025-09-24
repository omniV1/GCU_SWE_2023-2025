import express from 'express';
import { PerformanceRecordController } from './performanceRecord.controller';

const router = express.Router();
const performanceRecordController = new PerformanceRecordController();

// Get all performance records
router.get('/', performanceRecordController.getAllPerformanceRecords);

// Add this new route for getting aircraft-specific performance records
router.get('/aircraft/:aircraftId', performanceRecordController.getPerformanceRecordsByAircraftId);

// Other existing routes
router.get('/:id', performanceRecordController.getPerformanceRecordById);
router.post('/', performanceRecordController.createPerformanceRecord);
router.put('/:id', performanceRecordController.updatePerformanceRecord);
router.delete('/:id', performanceRecordController.deletePerformanceRecord);

export default router;