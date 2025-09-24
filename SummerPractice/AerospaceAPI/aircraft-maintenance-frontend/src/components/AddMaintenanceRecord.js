import React, { useState } from 'react';
import { addMaintenanceRecord } from '../services/api';
import '../styles/MaintenanceRecords.css';


const AddMaintenanceRecord = ({ aircraftId, onRecordAdded }) => {
    const [record, setRecord] = useState({
        details: '',
        maintenanceDate: '',
        technician: ''
    });

    const handleChange = (e) => {
        setRecord({ ...record, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await addMaintenanceRecord({
                aircraftId: aircraftId,
                details: record.details,
                maintenanceDate: record.maintenanceDate,
                technician: record.technician
            });
            onRecordAdded();
            setRecord({ details: '', maintenanceDate: '', technician: '' }); // Reset form
        } catch (error) {
            console.error('Error adding maintenance record:', error);
        }
    };

    return (
        <div className="add-maintenance-record">
            <h3>Add New Maintenance Record</h3>
            <form onSubmit={handleSubmit}>
                <input
                    type="date"
                    name="maintenanceDate"
                    value={record.maintenanceDate}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="details"
                    value={record.details}
                    onChange={handleChange}
                    placeholder="Maintenance details"
                    required
                />
                <input
                    type="text"
                    name="technician"
                    value={record.technician}
                    onChange={handleChange}
                    placeholder="Technician name"
                    required
                />
                <button type="submit">Add Record</button>
            </form>
        </div>
    );
};

export default AddMaintenanceRecord;
