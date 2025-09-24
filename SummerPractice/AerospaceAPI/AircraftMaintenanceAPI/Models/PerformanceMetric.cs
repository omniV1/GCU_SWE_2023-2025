using System;
using System.ComponentModel.DataAnnotations;

namespace AircraftMaintenanceAPI.Models
{
    public class PerformanceMetric
    {
        public int Id { get; set; }

        [Required]
        public int AircraftId { get; set; }

        [Required]
        public DateTime Date { get; set; }

        [Required]
        public double MetricValue { get; set; }

        [Required]
        [StringLength(100)]
        public string MetricType { get; set; } = string.Empty;

        public Aircraft? Aircraft { get; set; }
    }
}