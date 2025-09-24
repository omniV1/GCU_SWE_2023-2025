import React, { useEffect, useState, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import { getMaintenanceRecordsByAircraftId } from '../services/api';
import AddMaintenanceRecord from './AddMaintenanceRecord';
import EditMaintenanceRecord from './EditMaintenanceRecord';
import '../styles/MaintenanceRecords.css';
import { deleteMaintenanceRecord } from '../services/api'; // Adjust the path as needed


const MaintenanceRecords = () => {
    const { id } = useParams();
    const [records, setRecords] = useState([]);
    const [editingRecordId, setEditingRecordId] = useState(null);

    const fetchMaintenanceRecords = useCallback(async () => {
        try {
            const response = await getMaintenanceRecordsByAircraftId(id);
            setRecords(response.data);
        } catch (error) {
            console.error('Error fetching maintenance records:', error);
        }
    }, [id]);

    useEffect(() => {
        fetchMaintenanceRecords();
    }, [fetchMaintenanceRecords]);

    const handleRecordAdded = () => {
        fetchMaintenanceRecords(); // Refresh the records list after adding a new record
    };

    const handleRecordUpdated = () => {
        fetchMaintenanceRecords(); // Refresh the records list after updating a record
        setEditingRecordId(null); // Exit editing mode
    };

    const handleDelete = async (recordId) => {
        try {
            await deleteMaintenanceRecord(recordId);
            fetchMaintenanceRecords(); // Refresh the records list after deletion
        } catch (error) {
            console.error('Error deleting maintenance record:', error);
        }
    };

    return (
        <div className="maintenance-records-container">
            <h2 className="title">Maintenance Records for Aircraft {id}</h2>
            <div className="table-wrapper">
                <table className="records-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Details</th>
                            <th>Technician</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {records.map(record => (
                            <tr key={record.id}>
                                <td>{new Date(record.maintenanceDate).toLocaleDateString()}</td>
                                <td>{record.details}</td>
                                <td>{record.technician}</td>
                                <td>
                                    <button 
                                        onClick={() => setEditingRecordId(record.id)} 
                                        className="edit-button"
                                    >
                                        Edit
                                    </button>
                                    <button 
                                        onClick={() => handleDelete(record.id)} 
                                        className="delete-button"
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            {editingRecordId ? (
                <div className="add-maintenance-record">
                    <EditMaintenanceRecord 
                        recordId={editingRecordId} 
                        onRecordUpdated={handleRecordUpdated} 
                    />
                </div>
            ) : (
                <div className="add-maintenance-record">
                    <AddMaintenanceRecord 
                        aircraftId={id} 
                        onRecordAdded={handleRecordAdded} 
                    />
                </div>
            )}
        </div>
    );
};

export default MaintenanceRecords;