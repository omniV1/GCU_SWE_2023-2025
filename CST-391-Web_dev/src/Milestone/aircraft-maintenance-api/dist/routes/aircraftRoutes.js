"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const aircraftController_1 = require("../controllers/aircraftController");
const router = express_1.default.Router();
const aircraftController = new aircraftController_1.AircraftController();
router.get('/', aircraftController.getAllAircraft);
router.get('/:id', aircraftController.getAircraftById);
router.post('/', aircraftController.createAircraft);
router.put('/:id', aircraftController.updateAircraft);
router.delete('/:id', aircraftController.deleteAircraft);
exports.default = router;
