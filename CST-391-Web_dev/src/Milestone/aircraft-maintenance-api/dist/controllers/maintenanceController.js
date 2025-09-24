"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.MaintenanceController = void 0;
const maintenanceService_1 = require("../services/maintenanceService");
const asyncHandler_1 = require("../utils/asyncHandler");
class MaintenanceController {
    constructor() {
        this.getAllMaintenanceRecords = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const records = yield this.maintenanceService.getAllMaintenanceRecords();
            res.json(records);
        }));
        this.getMaintenanceRecordById = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const record = yield this.maintenanceService.getMaintenanceRecordById(id);
            if (record) {
                res.json(record);
            }
            else {
                res.status(404).json({ message: 'Maintenance record not found' });
            }
        }));
        this.createMaintenanceRecord = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const record = yield this.maintenanceService.createMaintenanceRecord(req.body);
            res.status(201).json(record);
        }));
        this.updateMaintenanceRecord = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const record = yield this.maintenanceService.updateMaintenanceRecord(id, req.body);
            if (record) {
                res.json(record);
            }
            else {
                res.status(404).json({ message: 'Maintenance record not found' });
            }
        }));
        this.deleteMaintenanceRecord = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const success = yield this.maintenanceService.deleteMaintenanceRecord(id);
            if (success) {
                res.status(204).send();
            }
            else {
                res.status(404).json({ message: 'Maintenance record not found' });
            }
        }));
        this.maintenanceService = new maintenanceService_1.MaintenanceService();
    }
}
exports.MaintenanceController = MaintenanceController;
