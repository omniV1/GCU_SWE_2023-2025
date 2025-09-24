public class MaintenanceRecord
{
    public int Id { get; set; }
    public int AircraftId { get; set; }
    public required string Details { get; set; }
    public DateTime MaintenanceDate { get; set; }
    public required string Technician { get; set; }
    public Aircraft? Aircraft { get; set; }
}