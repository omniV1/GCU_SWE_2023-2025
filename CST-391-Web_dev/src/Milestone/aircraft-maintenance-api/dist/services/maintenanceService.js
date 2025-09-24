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
exports.MaintenanceService = void 0;
const database_1 = require("../config/database");
class MaintenanceService {
    getAllMaintenanceRecords() {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM MaintenanceRecord');
            return rows;
        });
    }
    getMaintenanceRecordById(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM MaintenanceRecord WHERE id = ?', [id]);
            return rows[0] || null;
        });
    }
    createMaintenanceRecord(record) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('INSERT INTO MaintenanceRecord (aircraftId, details, maintenanceDate, technician, maintenanceType) VALUES (?, ?, ?, ?, ?)', [record.aircraftId, record.details, record.maintenanceDate, JSON.stringify(record.technician), record.maintenanceType]);
            const id = result.insertId;
            return Object.assign({ id }, record);
        });
    }
    updateMaintenanceRecord(id, record) {
        return __awaiter(this, void 0, void 0, function* () {
            yield database_1.db.query('UPDATE MaintenanceRecord SET aircraftId = ?, details = ?, maintenanceDate = ?, technician = ?, maintenanceType = ? WHERE id = ?', [record.aircraftId, record.details, record.maintenanceDate, JSON.stringify(record.technician), record.maintenanceType, id]);
            return this.getMaintenanceRecordById(id);
        });
    }
    deleteMaintenanceRecord(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('DELETE FROM MaintenanceRecord WHERE id = ?', [id]);
            return result.affectedRows > 0;
        });
    }
}
exports.MaintenanceService = MaintenanceService;
