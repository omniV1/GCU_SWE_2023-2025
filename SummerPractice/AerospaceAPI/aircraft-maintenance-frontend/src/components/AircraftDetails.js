import React, { useEffect, useState, useCallback } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getAircraftById } from '../services/api';

const AircraftDetails = () => {
    const { id } = useParams();
    const [aircraft, setAircraft] = useState(null);

    const fetchAircraftDetails = useCallback(async () => {
        try {
            const response = await getAircraftById(id);
            setAircraft(response.data);
        } catch (error) {
            console.error('Error fetching aircraft details:', error);
        }
    }, [id]);

    useEffect(() => {
        fetchAircraftDetails();
    }, [fetchAircraftDetails]);

    if (!aircraft) return <div className="text-center mt-10">Loading...</div>;

    return (
        <div className="max-w-2xl mx-auto mt-10 bg-white p-8 border border-gray-300 rounded-lg shadow-lg">
            <h1 className="text-3xl font-bold mb-6">Aircraft Details</h1>
            <div className="mb-4">
                <p className="text-gray-700"><span className="font-semibold">Model:</span> {aircraft.model}</p>
            </div>
            <div className="mb-4">
                <p className="text-gray-700"><span className="font-semibold">Serial Number:</span> {aircraft.serialNumber}</p>
            </div>
            <div className="mb-6">
                <p className="text-gray-700">
                    <span className="font-semibold">Last Maintenance Date:</span> {
                        aircraft.lastMaintenanceDate 
                        ? new Date(aircraft.lastMaintenanceDate).toLocaleDateString() 
                        : 'No maintenance record'
                    }
                </p>
            </div>
            <Link 
                to={`/aircrafts/${id}/maintenance`}
                className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded inline-block transition duration-300"
            >
                View Maintenance Records
            </Link>
        </div>
    );
};

export default AircraftDetails;