using AircraftMaintenanceAPI.Models;

namespace AircraftMaintenanceAPI.Services
{
    public interface IAircraftService
    {
        Task<IEnumerable<Aircraft>> GetAllAircraftsAsync();
        Task<Aircraft?> GetAircraftByIdAsync(int id);
        Task<Aircraft> CreateAircraftAsync(Aircraft aircraft);
        Task<Aircraft?> UpdateAircraftAsync(int id, Aircraft aircraft);
        Task<bool> DeleteAircraftAsync(int id);
    }
}
