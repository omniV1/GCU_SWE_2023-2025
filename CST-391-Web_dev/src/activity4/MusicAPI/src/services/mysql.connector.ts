import { createPool, Pool } from "mysql";

// Define a variable to hold the MySQL connection pool
let pool: Pool | null = null;

// Function to initialize the MySQL connection pool
const initializeMySqlConnector = () => {
    try {
        // Log environment variables related to MySQL configuration
        console.log(`MY_SQL_DB_HOST:${process.env.MY_SQL_DB_HOST}`);
        console.log(`MY_SQL_DB_USER:${process.env.MY_SQL_DB_USER}`);
        console.log(`MY_SQL_DB_PASSWORD:${process.env.MY_SQL_DB_PASSWORD}`);
        console.log(`MY_SQL_DB_PORT:${process.env.MY_SQL_DB_PORT}`);
        console.log(`MY_SQL_DB_DATABASE:${process.env.MY_SQL_DB_DATABASE}`);
        console.log(`MY_SQL_DB_CONNECTION_LIMIT:${process.env.MY_SQL_DB_CONNECTION_LIMIT}`);

        // Create the MySQL connection pool using environment variables
        pool = createPool({
            connectionLimit: parseInt(process.env.MY_SQL_DB_CONNECTION_LIMIT != undefined ? process.env.MY_SQL_DB_CONNECTION_LIMIT : ""),
            port: parseInt(process.env.MY_SQL_DB_PORT != undefined ? process.env.MY_SQL_DB_PORT : ""),
            host: process.env.MY_SQL_DB_HOST,
            user: process.env.MY_SQL_DB_USER,
            password: process.env.MY_SQL_DB_PASSWORD,
            database: process.env.MY_SQL_DB_DATABASE,
        });

        // Log successful generation of MySQL adapter pool
        console.debug('MySql Adapter Pool generated successfully');
        console.log('process.env.DB_DATABASE', process.env.MY_SQL_DB_DATABASE);

        // Test the connection by acquiring a connection from the pool and releasing it
        pool.getConnection((err, connection) => {
            if (err) {
                console.log('error MySql failed to connect');
                throw new Error('not able to connect to database');
            } else {
                console.log('connection made');
                connection.release();
            }
        })
    } catch (error) {
        // Handle errors during pool initialization
        console.error('[mysql.connector][initializeMySqlConnector][Error]: ', error);
        throw new Error('failed to initialize pool');
    }
}

// Function to execute MySQL queries
export const execute = <T>(query: string, params: string[] | Object): Promise<T> => {
    try {
        // Initialize the MySQL connection pool if it hasn't been initialized yet
        if (!pool) {
            initializeMySqlConnector();
        }

        // Return a promise that resolves with query results or rejects with an error
        return new Promise<T>((resolve, reject) => {
            // Execute the query using the pool
            pool!.query(query, params, (error, results) => {
                if (error) reject(error); // Reject the promise if there's an error
                else resolve(results); // Resolve the promise with query results
            });
        });

    } catch (error) {
        // Handle errors during query execution
        console.error('[mysql.connector][execute][Error]: ', error);
        throw new Error('failed to execute MySQL query');
    }
};
