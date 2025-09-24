"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const maintenanceController_1 = require("../controllers/maintenanceController");
const router = express_1.default.Router();
const maintenanceController = new maintenanceController_1.MaintenanceController();
router.get('/', maintenanceController.getAllMaintenanceRecords);
router.get('/:id', maintenanceController.getMaintenanceRecordById);
router.post('/', maintenanceController.createMaintenanceRecord);
router.put('/:id', maintenanceController.updateMaintenanceRecord);
router.delete('/:id', maintenanceController.deleteMaintenanceRecord);
exports.default = router;
