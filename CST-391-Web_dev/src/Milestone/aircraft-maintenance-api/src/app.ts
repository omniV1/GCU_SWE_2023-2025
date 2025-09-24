import express, { Router } from 'express';
import helmet from 'helmet';
import cors from 'cors';
import dotenv from 'dotenv';
import { errorHandler } from './middleware/errorHandler';

// Routes
import aircraftRoutes from './aircraft/aircraft.routes';
import maintenanceRecordRoutes from './maintenanceRecord/maintenanceRecord.routes';
import performanceRecordRoutes from './performanceRecord/performanceRecord.routes';


dotenv.config();

const app = express();

// Middleware
app.use(helmet());

app.use(cors({
  origin: ['http://localhost:5173', 'http://localhost:5174'], // Add both ports
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));
app.use(express.json());

// Add this new middleware here
app.use((req, res, next) => {
  req.url = decodeURIComponent(req.url).replace(/\s+$/, '');
  console.log(`Incoming request (after trim): ${req.method} ${req.url}`);
  next();
});

// Routes
app.use('/api/aircraft', aircraftRoutes);
app.use('/api/performance', performanceRecordRoutes);

// Modify this line to include the new logging
app.use('/api/maintenance', (req, res, next) => {
  console.log(`Entering maintenance route handler: ${req.method} ${req.url}`);
  maintenanceRecordRoutes(req, res, next);
});


app.use('/api/maintenancerecord', maintenanceRecordRoutes);


// Move the test route here, before the 404 handler
app.get('/api/maintenance/test', (req, res) => {
  res.send('Maintenance test route');
});

// Log all routes (keep this where it is)
app._router.stack.forEach((middleware: any) => {
  if (middleware.route) { // routes registered directly on the app
    console.log(`Route: ${Object.keys(middleware.route.methods)} ${middleware.route.path}`);
  } else if (middleware.name === 'router') { // router middleware 
    (middleware.handle as Router).stack.forEach((handler: any) => {
      if (handler.route) {
        console.log(`Route: ${Object.keys(handler.route.methods)} ${(middleware as any).regexp} ${handler.route.path}`);
      }
    });
  }
});

// 404 handler
app.use((req, res, next) => {
  console.log(`Unmatched route: ${req.method} ${req.url}`);
  res.status(404).send('Route not found');
});

// Error handling middleware
app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

console.log("Database Host:", process.env.MY_SQL_DB_HOST);
console.log("Database User:", process.env.MY_SQL_DB_USER);
console.log("Database Password:", process.env.MY_SQL_DB_PASSWORD);
console.log("Database Name:", process.env.MY_SQL_DB_NAME);


export default app;