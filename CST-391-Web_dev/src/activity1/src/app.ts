import dotenv from "dotenv";
import express, { Request, Response, NextFunction } from 'express';
import albumsRouter from './albums/albums.routes';
import artistsRouter from './artists/artist.routes'
import logger from './middleware/logger.middleware'
import cors from 'cors';
import helmet from "helmet";

dotenv.config();
const app = express();
const port = process.env.PORT;

// Basic middleware setup
app.use(cors()); // enables all CORS requests
app.use(helmet()); // adding set of security middleware

// Logging middleware (if in development mode)
if (process.env.NODE_ENV == 'development') {
    app.use(logger);
    console.log(process.env.GREETING + ' in dev mode');
}

// Body parsing debugging middleware
app.use((req, res, next) => {
    console.log('Request body before parsing:', req.body);
    express.json()(req, res, (err) => {
        if (err) {
            console.error('Error parsing JSON:', err);
            return res.status(400).json({ error: 'Invalid JSON' });
        }
        console.log('Request body after parsing:', req.body);
        next();
    });
});

// Regular body parsing middleware
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({extended: true})); // Parse URL-encoded bodies

// Routes
app.use('/', [albumsRouter, artistsRouter]);

// Error handling middleware (should be last)
app.use((err: any, req: Request, res: Response, next: NextFunction) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});