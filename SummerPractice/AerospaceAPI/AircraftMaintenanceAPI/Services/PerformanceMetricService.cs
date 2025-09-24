
using AircraftMaintenanceAPI.Data;
using AircraftMaintenanceAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace AircraftMaintenanceAPI.Services
{
    public class PerformanceMetricService : IPerformanceMetricService
    {
        private readonly AircraftMaintenanceContext _context;

        public PerformanceMetricService(AircraftMaintenanceContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<PerformanceMetric>> GetAllPerformanceMetricsAsync()
        {
            return await _context.PerformanceMetrics.ToListAsync();
        }

        public async Task<PerformanceMetric?> GetPerformanceMetricByIdAsync(int id)
        {
            return await _context.PerformanceMetrics.FindAsync(id);
        }

        public async Task<PerformanceMetric> CreatePerformanceMetricAsync(PerformanceMetric performanceMetric)
        {
            _context.PerformanceMetrics.Add(performanceMetric);
            await _context.SaveChangesAsync();
            return performanceMetric;
        }

        public async Task<PerformanceMetric?> UpdatePerformanceMetricAsync(int id, PerformanceMetric performanceMetric)
        {
            var existingPerformanceMetric = await _context.PerformanceMetrics.FindAsync(id);
            if (existingPerformanceMetric == null)
            {
                return null;
            }

            existingPerformanceMetric.Date = performanceMetric.Date;
            existingPerformanceMetric.MetricValue = performanceMetric.MetricValue;
            existingPerformanceMetric.MetricType = performanceMetric.MetricType;

            await _context.SaveChangesAsync();
            return existingPerformanceMetric;
        }

        public async Task<bool> DeletePerformanceMetricAsync(int id)
        {
            var performanceMetric = await _context.PerformanceMetrics.FindAsync(id);
            if (performanceMetric == null)
            {
                return false;
            }

            _context.PerformanceMetrics.Remove(performanceMetric);
            await _context.SaveChangesAsync();
            return true;
        }
    }
}
