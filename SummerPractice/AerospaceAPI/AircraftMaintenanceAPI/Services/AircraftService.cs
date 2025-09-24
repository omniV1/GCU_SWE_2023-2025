using AircraftMaintenanceAPI.Data;
using AircraftMaintenanceAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace AircraftMaintenanceAPI.Services
{
    public class AircraftService : IAircraftService
    {
        private readonly AircraftMaintenanceContext _context;

        public AircraftService(AircraftMaintenanceContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Aircraft>> GetAllAircraftsAsync()
        {
            return await _context.Aircrafts.ToListAsync();
        }

        public async Task<Aircraft?> GetAircraftByIdAsync(int id)
        {
            return await _context.Aircrafts.FindAsync(id);
        }

        public async Task<Aircraft> CreateAircraftAsync(Aircraft aircraft)
        {
            _context.Aircrafts.Add(aircraft);
            await _context.SaveChangesAsync();
            return aircraft;
        }

        public async Task<Aircraft?> UpdateAircraftAsync(int id, Aircraft aircraft)
        {
            var existingAircraft = await _context.Aircrafts.FindAsync(id);
            if (existingAircraft == null)
            {
                return null;
            }

            existingAircraft.Model = aircraft.Model;
            existingAircraft.SerialNumber = aircraft.SerialNumber;
            existingAircraft.LastMaintenanceDate = aircraft.LastMaintenanceDate;

            await _context.SaveChangesAsync();
            return existingAircraft;
        }

        public async Task<bool> DeleteAircraftAsync(int id)
        {
            var aircraft = await _context.Aircrafts.FindAsync(id);
            if (aircraft == null)
            {
                return false;
            }

            _context.Aircrafts.Remove(aircraft);
            await _context.SaveChangesAsync();
            return true;
        }
    }
}
