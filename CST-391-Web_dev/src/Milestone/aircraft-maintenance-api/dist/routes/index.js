"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const aircraftRoutes_1 = __importDefault(require("./aircraftRoutes"));
const maintenanceRoutes_1 = __importDefault(require("./maintenanceRoutes"));
const performanceRoutes_1 = __importDefault(require("./performanceRoutes"));
const userRoutes_1 = __importDefault(require("./userRoutes"));
const router = express_1.default.Router();
router.use('/aircraft', aircraftRoutes_1.default);
router.use('/maintenance', maintenanceRoutes_1.default);
router.use('/performance', performanceRoutes_1.default);
router.use('/users', userRoutes_1.default);
exports.default = router;
