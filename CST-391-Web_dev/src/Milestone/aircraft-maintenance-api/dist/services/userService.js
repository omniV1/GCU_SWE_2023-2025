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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UserService = void 0;
const database_1 = require("../config/database");
const bcrypt_1 = __importDefault(require("bcrypt"));
class UserService {
    getAllUsers() {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT id, username, role FROM User');
            return rows;
        });
    }
    getUserById(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT id, username, role FROM User WHERE id = ?', [id]);
            return rows[0] || null;
        });
    }
    createUser(user) {
        return __awaiter(this, void 0, void 0, function* () {
            const hashedPassword = yield bcrypt_1.default.hash(user.password, 10);
            const [result] = yield database_1.db.query('INSERT INTO User (username, password, role) VALUES (?, ?, ?)', [user.username, hashedPassword, user.role]);
            const id = result.insertId;
            return { id, username: user.username, role: user.role };
        });
    }
    updateUser(id, user) {
        return __awaiter(this, void 0, void 0, function* () {
            if (user.password) {
                user.password = yield bcrypt_1.default.hash(user.password, 10);
            }
            yield database_1.db.query('UPDATE User SET username = ?, password = ?, role = ? WHERE id = ?', [user.username, user.password, user.role, id]);
            return this.getUserById(id);
        });
    }
    deleteUser(id) {
        return __awaiter(this, void 0, void 0, function* () {
            const [result] = yield database_1.db.query('DELETE FROM User WHERE id = ?', [id]);
            return result.affectedRows > 0;
        });
    }
    findByUsername(username) {
        return __awaiter(this, void 0, void 0, function* () {
            const [rows] = yield database_1.db.query('SELECT * FROM User WHERE username = ?', [username]);
            return rows[0] || null;
        });
    }
    verifyPassword(user, password) {
        return __awaiter(this, void 0, void 0, function* () {
            return bcrypt_1.default.compare(password, user.password);
        });
    }
}
exports.UserService = UserService;
