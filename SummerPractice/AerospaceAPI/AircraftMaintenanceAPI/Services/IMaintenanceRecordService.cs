using System.Collections.Generic;
using System.Threading.Tasks;
using AircraftMaintenanceAPI.Models;

namespace AircraftMaintenanceAPI.Services
{
public interface IMaintenanceRecordService
{
    Task<MaintenanceRecord> CreateMaintenanceRecordAsync(MaintenanceRecord maintenanceRecord);
    Task<IEnumerable<MaintenanceRecord>> GetAllMaintenanceRecordsAsync();
    Task<IEnumerable<MaintenanceRecord>> GetMaintenanceRecordsByAircraftIdAsync(int aircraftId);
    Task<bool> AircraftExistsAsync(int aircraftId);
    Task<MaintenanceRecord?> GetMaintenanceRecordByIdAsync(int id);
    Task<bool> UpdateMaintenanceRecordAsync(MaintenanceRecord maintenanceRecord);
    Task<bool> DeleteMaintenanceRecordAsync(int id);
}
}
