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
exports.UserController = void 0;
const userService_1 = require("../services/userService");
const asyncHandler_1 = require("../utils/asyncHandler");
class UserController {
    constructor() {
        this.getAllUsers = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const users = yield this.userService.getAllUsers();
            res.json(users);
        }));
        this.getUserById = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const user = yield this.userService.getUserById(id);
            if (user) {
                res.json(user);
            }
            else {
                res.status(404).json({ message: 'User not found' });
            }
        }));
        this.createUser = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const user = yield this.userService.createUser(req.body);
            res.status(201).json(user);
        }));
        this.updateUser = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const user = yield this.userService.updateUser(id, req.body);
            if (user) {
                res.json(user);
            }
            else {
                res.status(404).json({ message: 'User not found' });
            }
        }));
        this.deleteUser = (0, asyncHandler_1.asyncHandler)((req, res) => __awaiter(this, void 0, void 0, function* () {
            const id = parseInt(req.params.id);
            const success = yield this.userService.deleteUser(id);
            if (success) {
                res.status(204).send();
            }
            else {
                res.status(404).json({ message: 'User not found' });
            }
        }));
        this.userService = new userService_1.UserService();
    }
}
exports.UserController = UserController;
