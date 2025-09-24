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
exports.AircraftController = void 0;
const aircraftService_1 = require("../services/aircraftService");
const asyncHandler_1 = require("../utils/asyncHandler");
class AircraftController {
    constructor() {
        this.getAllAircraft = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const aircraft = yield this.aircraftService.getAllAircraft();
            res.json(aircraft);
        }));
        this.getAircraftById = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const aircraft = yield this.aircraftService.getAircraftById(id);
            if (aircraft) {
                res.json(aircraft);
            }
            else {
                res.status(404).json({ message: 'Aircraft not found' });
            }
        }));
        this.createAircraft = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const aircraft = yield this.aircraftService.createAircraft(req.body);
            res.status(201).json(aircraft);
        }));
        this.updateAircraft = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const aircraft = yield this.aircraftService.updateAircraft(id, req.body);
            if (aircraft) {
                res.json(aircraft);
            }
            else {
                res.status(404).json({ message: 'Aircraft not found' });
            }
        }));
        this.deleteAircraft = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const success = yield this.aircraftService.deleteAircraft(id);
            if (success) {
                res.status(204).send();
            }
            else {
                res.status(404).json({ message: 'Aircraft not found' });
            }
        }));
        this.aircraftService = new aircraftService_1.AircraftService();
    }
}
exports.AircraftController = AircraftController;
