import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getAircraftById, updateAircraft } from '../services/api';
import '../styles/AircraftEdit.css';

const AircraftEdit = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [aircraft, setAircraft] = useState({
        model: '',
        serialNumber: '',
        lastMaintenanceDate: ''
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchAircraftDetails = async () => {
            try {
                const response = await getAircraftById(id);
                setAircraft(response.data);
            } catch (err) {
                setError('Error fetching aircraft details.');
            } finally {
                setLoading(false);
            }
        };
        fetchAircraftDetails();
    }, [id]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setAircraft({ ...aircraft, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await updateAircraft(id, aircraft);
            navigate('/'); // Navigate back to the aircraft list
        } catch (err) {
            setError('Error updating aircraft.');
        }
    };

    if (loading) {
        return <div className="loading">Loading...</div>;
    }

    return (
        <div className="aircraft-edit-container">
            <h1 className="title">Edit Aircraft</h1>
            {error && <p className="error-message">{error}</p>}
            <form onSubmit={handleSubmit} className="aircraft-edit-form">
                <div className="form-group">
                    <label className="form-label">Model</label>
                    <input
                        type="text"
                        name="model"
                        value={aircraft.model}
                        onChange={handleChange}
                        className="form-input"
                        required
                    />
                </div>
                <div className="form-group">
                    <label className="form-label">Serial Number</label>
                    <input
                        type="text"
                        name="serialNumber"
                        value={aircraft.serialNumber}
                        onChange={handleChange}
                        className="form-input"
                        required
                    />
                </div>
                <div className="form-group">
                    <label className="form-label">Last Maintenance Date</label>
                    <input
                        type="date"
                        name="lastMaintenanceDate"
                        value={aircraft.lastMaintenanceDate.split('T')[0]}
                        onChange={handleChange}
                        className="form-input"
                        required
                    />
                </div>
                <button type="submit" className="submit-button">Update Aircraft</button>
            </form>
        </div>
    );
};

export default AircraftEdit;
