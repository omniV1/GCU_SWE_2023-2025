using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using AircraftMaintenanceAPI.Models;
using AircraftMaintenanceAPI.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AircraftMaintenanceAPI.Services
{
    public class MaintenanceRecordService : IMaintenanceRecordService
    {
        private readonly AircraftMaintenanceContext _context;
        private readonly ILogger<MaintenanceRecordService> _logger;

        public MaintenanceRecordService(AircraftMaintenanceContext context, ILogger<MaintenanceRecordService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<MaintenanceRecord> CreateMaintenanceRecordAsync(MaintenanceRecord maintenanceRecord)
        {
            try
            {
                _context.MaintenanceRecords.Add(maintenanceRecord);
                await _context.SaveChangesAsync();
                return maintenanceRecord;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error creating maintenance record");
                throw;
            }
        }

        public async Task<IEnumerable<MaintenanceRecord>> GetAllMaintenanceRecordsAsync()
        {
            return await _context.MaintenanceRecords
                .Include(m => m.Aircraft)
                .ToListAsync();
        }

        public async Task<IEnumerable<MaintenanceRecord>> GetMaintenanceRecordsByAircraftIdAsync(int aircraftId)
        {
            return await _context.MaintenanceRecords
                .Where(m => m.AircraftId == aircraftId)
                .Include(m => m.Aircraft)
                .ToListAsync();
        }

        public async Task<bool> AircraftExistsAsync(int aircraftId)
        {
            return await _context.Aircrafts.AnyAsync(a => a.Id == aircraftId);
        }

        public async Task<MaintenanceRecord?> GetMaintenanceRecordByIdAsync(int id)
        {
            return await _context.MaintenanceRecords
                .Include(m => m.Aircraft)
                .FirstOrDefaultAsync(m => m.Id == id);
        }

        public async Task<bool> UpdateMaintenanceRecordAsync(MaintenanceRecord maintenanceRecord)
        {
            try
            {
                _context.Entry(maintenanceRecord).State = EntityState.Modified;
                await _context.SaveChangesAsync();
                _logger.LogInformation($"MaintenanceRecord updated successfully. Id: {maintenanceRecord.Id}");
                return true;
            }
            catch (DbUpdateConcurrencyException ex)
            {
                if (!await MaintenanceRecordExistsAsync(maintenanceRecord.Id))
                {
                    _logger.LogWarning($"Failed to update MaintenanceRecord. Record not found. Id: {maintenanceRecord.Id}");
                    return false;
                }
                _logger.LogError(ex, $"Concurrency error occurred while updating MaintenanceRecord. Id: {maintenanceRecord.Id}");
                throw;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error occurred while updating MaintenanceRecord. Id: {maintenanceRecord.Id}");
                throw;
            }
        }

        public async Task<bool> DeleteMaintenanceRecordAsync(int id)
        {
            var maintenanceRecord = await _context.MaintenanceRecords.FindAsync(id);
            if (maintenanceRecord == null)
            {
                _logger.LogWarning($"Attempted to delete non-existent MaintenanceRecord. Id: {id}");
                return false;
            }

            _context.MaintenanceRecords.Remove(maintenanceRecord);
            await _context.SaveChangesAsync();
            _logger.LogInformation($"MaintenanceRecord deleted successfully. Id: {id}");
            return true;
        }

        private async Task<bool> MaintenanceRecordExistsAsync(int id)
        {
            return await _context.MaintenanceRecords.AnyAsync(e => e.Id == id);
        }
    }
}