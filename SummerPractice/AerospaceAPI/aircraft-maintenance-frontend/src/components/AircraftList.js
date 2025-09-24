import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getAircrafts, deleteAircraft } from '../services/api';


const AircraftList = () => {
    const [aircrafts, setAircrafts] = useState([]);

    useEffect(() => {
        fetchAircrafts();
    }, []);

    const fetchAircrafts = async () => {
        try {
            const response = await getAircrafts();
            setAircrafts(response.data);
        } catch (error) {
            console.error("Error fetching aircrafts:", error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await deleteAircraft(id);
            fetchAircrafts();
        } catch (error) {
            console.error("Error deleting aircraft:", error);
        }
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold mb-6">Aircraft List</h1>
            <table className="min-w-full bg-white">
                <thead>
                    <tr>
                        <th className="text-left py-2">Model</th>
                        <th className="text-left py-2">Serial Number</th>
                        <th className="text-left py-2">Last Maintenance Date</th>
                        <th className="text-left py-2">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {aircrafts.map(aircraft => (
                        <tr key={aircraft.id}>
                            <td className="py-2">{aircraft.model}</td>
                            <td className="py-2">{aircraft.serialNumber}</td>
                            <td className="py-2">
                                {aircraft.lastMaintenanceDate 
                                    ? new Date(aircraft.lastMaintenanceDate).toLocaleDateString() 
                                    : 'No Maintenance Records'}
                            </td>
                            <td className="py-2">
                                <button onClick={() => handleDelete(aircraft.id)} className="action-btn delete-btn">Delete</button>
                                <Link to={`/aircrafts/edit/${aircraft.id}`} className="action-btn edit-btn">Edit</Link>
                                <Link to={`/aircrafts/${aircraft.id}`} className="action-btn view-btn">View</Link>
                                <Link to={`/aircrafts/${aircraft.id}/maintenance`} className="action-btn maintenance-btn">Maintenance</Link>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AircraftList;