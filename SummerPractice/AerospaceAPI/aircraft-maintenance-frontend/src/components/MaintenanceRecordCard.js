import React from 'react';

const MaintenanceRecordCard = ({ record, onEdit }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6 mb-4 hover:shadow-lg transition-shadow duration-300">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-xl font-semibold text-gray-800">{record.details}</h3>
        <button
          onClick={() => onEdit(record.id)}
          className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300"
        >
          Edit
        </button>
      </div>
      <p className="text-gray-600 mb-2">Date: {new Date(record.maintenanceDate).toLocaleDateString()}</p>
      <p className="text-gray-600 mb-2">Technician: {record.technician}</p>
      <p className="text-gray-600">Aircraft ID: {record.aircraftId}</p>
    </div>
  );
};

export default MaintenanceRecordCard;