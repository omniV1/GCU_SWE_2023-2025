using AircraftMaintenanceAPI.Models;

namespace AircraftMaintenanceAPI.Services
{
    public interface IPerformanceMetricService
    {
        Task<IEnumerable<PerformanceMetric>> GetAllPerformanceMetricsAsync();
        Task<PerformanceMetric?> GetPerformanceMetricByIdAsync(int id);
        Task<PerformanceMetric> CreatePerformanceMetricAsync(PerformanceMetric performanceMetric);
        Task<PerformanceMetric?> UpdatePerformanceMetricAsync(int id, PerformanceMetric performanceMetric);
        Task<bool> DeletePerformanceMetricAsync(int id);
    }
}
