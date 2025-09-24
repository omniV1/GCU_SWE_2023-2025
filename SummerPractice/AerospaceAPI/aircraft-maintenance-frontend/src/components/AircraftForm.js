import React, { useState } from 'react';
import { createAircraft } from '../services/api';

const AircraftForm = () => {
    const [model, setModel] = useState('');
    const [serialNumber, setSerialNumber] = useState('');
    const [lastMaintenanceDate, setLastMaintenanceDate] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newAircraft = {
            model,
            serialNumber,
            lastMaintenanceDate,
        };
        await createAircraft(newAircraft);
        setModel('');
        setSerialNumber('');
        setLastMaintenanceDate('');
    };

    return (
        <div className="max-w-md mx-auto mt-10 bg-white p-8 border border-gray-300 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-6 text-center">Add Aircraft</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-4">
                    <label htmlFor="model" className="block text-gray-700 text-sm font-bold mb-2">Model</label>
                    <input
                        type="text"
                        id="model"
                        value={model}
                        onChange={(e) => setModel(e.target.value)}
                        required
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="serialNumber" className="block text-gray-700 text-sm font-bold mb-2">Serial Number</label>
                    <input
                        type="text"
                        id="serialNumber"
                        value={serialNumber}
                        onChange={(e) => setSerialNumber(e.target.value)}
                        required
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                <div className="mb-6">
                    <label htmlFor="lastMaintenanceDate" className="block text-gray-700 text-sm font-bold mb-2">Last Maintenance Date</label>
                    <input
                        type="date"
                        id="lastMaintenanceDate"
                        value={lastMaintenanceDate}
                        onChange={(e) => setLastMaintenanceDate(e.target.value)}
                        required
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                <button type="submit" className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    Add Aircraft
                </button>
            </form>
        </div>
    );
};

export default AircraftForm;