using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization; // For [JsonIgnore] attribute
using AircraftMaintenanceAPI.Models;

public class Aircraft
{
    public int Id { get; set; }
    public string Model { get; set; } = string.Empty;
    public string SerialNumber { get; set; } = string.Empty;
    public DateTime LastMaintenanceDate { get; set; }
    public bool MaintenancePerformed { get; set; }

    [JsonIgnore]
    public ICollection<MaintenanceRecord> MaintenanceRecords { get; set; } = new List<MaintenanceRecord>();
}
