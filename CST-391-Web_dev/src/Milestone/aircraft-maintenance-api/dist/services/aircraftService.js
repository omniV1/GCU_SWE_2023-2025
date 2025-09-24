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
exports.AircraftService = void 0;
const database_1 = require("../config/database");
class AircraftService {
    getAllAircraft() {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM Aircraft');
            return rows;
        });
    }
    getAircraftById(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM Aircraft WHERE id = ?', [id]);
            return rows[0] || null;
        });
    }
    createAircraft(aircraft) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('INSERT INTO Aircraft (model, serialNumber, lastMaintenanceDate, maintenancePerformed, totalFlightTime, status) VALUES (?, ?, ?, ?, ?, ?)', [aircraft.model, aircraft.serialNumber, aircraft.lastMaintenanceDate, aircraft.maintenancePerformed, aircraft.totalFlightTime, aircraft.status]);
            const id = result.insertId;
            return Object.assign({ id }, aircraft);
        });
    }
    updateAircraft(id, aircraft) {
        return __awaiter(this, void 0, void 0, function* () {
            yield database_1.db.query('UPDATE Aircraft SET model = ?, serialNumber = ?, lastMaintenanceDate = ?, maintenancePerformed = ?, totalFlightTime = ?, status = ? WHERE id = ?', [aircraft.model, aircraft.serialNumber, aircraft.lastMaintenanceDate, aircraft.maintenancePerformed, aircraft.totalFlightTime, aircraft.status, id]);
            return this.getAircraftById(id);
        });
    }
    deleteAircraft(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('DELETE FROM Aircraft WHERE id = ?', [id]);
            return result.affectedRows > 0;
        });
    }
}
exports.AircraftService = AircraftService;
