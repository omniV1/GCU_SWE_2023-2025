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
exports.PerformanceService = void 0;
const database_1 = require("../config/database");
class PerformanceService {
    getAllPerformanceMetrics() {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM PerformanceMetric');
            return rows;
        });
    }
    getPerformanceMetricById(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM PerformanceMetric WHERE id = ?', [id]);
            return rows[0] || null;
        });
    }
    createPerformanceMetric(metric) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('INSERT INTO PerformanceMetric (aircraftId, notes, value, date, metricType) VALUES (?, ?, ?, ?, ?)', [metric.aircraftId, metric.notes, metric.value, metric.date, metric.metricType]);
            const id = result.insertId;
            return Object.assign({ id }, metric);
        });
    }
    updatePerformanceMetric(id, metric) {
        return __awaiter(this, void 0, void 0, function* () {
            yield database_1.db.query('UPDATE PerformanceMetric SET aircraftId = ?, notes = ?, value = ?, date = ?, metricType = ? WHERE id = ?', [metric.aircraftId, metric.notes, metric.value, metric.date, metric.metricType, id]);
            return this.getPerformanceMetricById(id);
        });
    }
    deletePerformanceMetric(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('DELETE FROM PerformanceMetric WHERE id = ?', [id]);
            return result.affectedRows > 0;
        });
    }
}
exports.PerformanceService = PerformanceService;
