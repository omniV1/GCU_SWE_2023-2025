using Microsoft.EntityFrameworkCore;
using AircraftMaintenanceAPI.Models;

namespace AircraftMaintenanceAPI.Data
{
    public class AircraftMaintenanceContext : DbContext
    {
        public AircraftMaintenanceContext(DbContextOptions<AircraftMaintenanceContext> options)
            : base(options)
        {
        }

        public DbSet<Aircraft> Aircrafts { get; set; }
        public DbSet<MaintenanceRecord> MaintenanceRecords { get; set; }
        public DbSet<User> Users { get; set; }
        public DbSet<PerformanceMetric> PerformanceMetrics { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Aircraft>().ToTable("Aircrafts");
            modelBuilder.Entity<MaintenanceRecord>().ToTable("MaintenanceRecords");
            modelBuilder.Entity<User>().ToTable("Users");
            modelBuilder.Entity<PerformanceMetric>().ToTable("PerformanceMetrics");
        }
    }
}