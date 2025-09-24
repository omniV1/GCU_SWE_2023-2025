import React, { useState, useEffect } from 'react';
import { getMaintenanceRecord, updateMaintenanceRecord } from '../services/api';

const EditMaintenanceRecord = ({ recordId, onRecordUpdated }) => {
    const [record, setRecord] = useState({
        id: '',
        aircraftId: '',
        details: '',
        maintenanceDate: '',
        technician: ''
    });
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecord = async () => {
            try {
                const response = await getMaintenanceRecord(recordId);
                setRecord(response.data);
            } catch (error) {
                console.error('Error fetching maintenance record:', error);
                setError('Failed to fetch maintenance record. Please try again.');
            }
        };
        fetchRecord();
    }, [recordId]);

    const handleChange = (e) => {
        setRecord({ ...record, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            await updateMaintenanceRecord(record.id, record);
            onRecordUpdated();
        } catch (error) {
            console.error('Error updating maintenance record:', error);
            setError('Failed to update maintenance record. Please try again.');
        }
    };

    return (
        <div className="p-4 max-w-lg mx-auto bg-white shadow-md rounded-lg">
            {error && <div className="text-red-600 mb-4">{error}</div>}
            <h3 className="text-xl font-semibold mb-4">Edit Maintenance Record</h3>
            <form onSubmit={handleSubmit}>
                <input
                    type="hidden"
                    name="id"
                    value={record.id}
                />
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="aircraftId">Aircraft ID</label>
                    <input
                        id="aircraftId"
                        type="number"
                        name="aircraftId"
                        value={record.aircraftId}
                        onChange={handleChange}
                        className="w-full p-2 border border-gray-300 rounded-md"
                        placeholder="Aircraft ID"
                        required
                    />
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="maintenanceDate">Maintenance Date</label>
                    <input
                        id="maintenanceDate"
                        type="datetime-local"
                        name="maintenanceDate"
                        value={record.maintenanceDate ? record.maintenanceDate.slice(0, 16) : ''}
                        onChange={handleChange}
                        className="w-full p-2 border border-gray-300 rounded-md"
                        required
                    />
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="details">Maintenance Details</label>
                    <input
                        id="details"
                        type="text"
                        name="details"
                        value={record.details}
                        onChange={handleChange}
                        className="w-full p-2 border border-gray-300 rounded-md"
                        placeholder="Maintenance details"
                        required
                    />
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="technician">Technician Name</label>
                    <input
                        id="technician"
                        type="text"
                        name="technician"
                        value={record.technician}
                        onChange={handleChange}
                        className="w-full p-2 border border-gray-300 rounded-md"
                        placeholder="Technician name"
                        required
                    />
                </div>
                <button
                    type="submit"
                    className="w-full py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
                >
                    Update Record
                </button>
            </form>
        </div>
    );
};

export default EditMaintenanceRecord;
