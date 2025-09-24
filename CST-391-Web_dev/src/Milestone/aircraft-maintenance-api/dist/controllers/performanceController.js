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
exports.PerformanceController = void 0;
const performanceService_1 = require("../services/performanceService");
const asyncHandler_1 = require("../utils/asyncHandler");
class PerformanceController {
    constructor() {
        this.getAllPerformanceMetrics = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const metrics = yield this.performanceService.getAllPerformanceMetrics();
            res.json(metrics);
        }));
        this.getPerformanceMetricById = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const metric = yield this.performanceService.getPerformanceMetricById(id);
            if (metric) {
                res.json(metric);
            }
            else {
                res.status(404).json({ message: 'Performance metric not found' });
            }
        }));
        this.createPerformanceMetric = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const metric = yield this.performanceService.createPerformanceMetric(req.body);
            res.status(201).json(metric);
        }));
        this.updatePerformanceMetric = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const metric = yield this.performanceService.updatePerformanceMetric(id, req.body);
            if (metric) {
                res.json(metric);
            }
            else {
                res.status(404).json({ message: 'Performance metric not found' });
            }
        }));
        this.deletePerformanceMetric = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const success = yield this.performanceService.deletePerformanceMetric(id);
            if (success) {
                res.status(204).send();
            }
            else {
                res.status(404).json({ message: 'Performance metric not found' });
            }
        }));
        this.performanceService = new performanceService_1.PerformanceService();
    }
}
exports.PerformanceController = PerformanceController;
