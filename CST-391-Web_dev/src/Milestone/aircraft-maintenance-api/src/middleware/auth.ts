import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';
import { UserDAO } from '../user/user.dao';

const userDAO = new UserDAO();

// This should be in an environment variable in a real application
const JWT_SECRET = process.env.JWT_SECRET || 'Pickles';

export const login = async (req: Request, res: Response) => {
  const { username, password } = req.body;

  try {
    const user = await userDAO.getUserByUsername(username);
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const isPasswordValid = await bcrypt.compare(password, user.PasswordHash);
    if (!isPasswordValid) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign({ userId: user.UserID, role: user.Role }, JWT_SECRET, { expiresIn: '1h' });

    res.json({ token });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

export const authenticate = async (req: Request, res: Response, next: NextFunction) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) {
    return res.status(401).json({ message: 'No token provided' });
  }

  const [bearer, token] = authHeader.split(' ');
  if (bearer !== 'Bearer' || !token) {
    return res.status(401).json({ message: 'Invalid token format' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET) as { userId: number; role: string };
    const user = await userDAO.getUserById(decoded.userId);
    if (!user) {
      return res.status(401).json({ message: 'User not found' });
    }
    (req as any).user = user;
    next();
  } catch (error) {
    return res.status(401).json({ message: 'Invalid token' });
  }
};

export const authorize = (roles: string[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as any).user;
    const userRole = user?.Role?.toLowerCase(); // Normalize to lowercase
    if (!user || !roles.map(role => role.toLowerCase()).includes(userRole)) {
      return res.status(403).json({ message: 'Insufficient permissions' });
    }
    next();
  };
};


export const mockAuthenticate = (req: Request, res: Response, next: NextFunction) => {
  (req as any).user = { UserID: 1, Username: 'admin', Role: 'Admin' }; // Mock admin user
  next();
};
