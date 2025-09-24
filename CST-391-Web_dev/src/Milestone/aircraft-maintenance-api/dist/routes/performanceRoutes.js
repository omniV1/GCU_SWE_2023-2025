"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const performanceController_1 = require("../controllers/performanceController");
const router = express_1.default.Router();
const performanceController = new performanceController_1.PerformanceController();
router.get('/', performanceController.getAllPerformanceMetrics);
router.get('/:id', performanceController.getPerformanceMetricById);
router.post('/', performanceController.createPerformanceMetric);
router.put('/:id', performanceController.updatePerformanceMetric);
router.delete('/:id', performanceController.deletePerformanceMetric);
exports.default = router;
