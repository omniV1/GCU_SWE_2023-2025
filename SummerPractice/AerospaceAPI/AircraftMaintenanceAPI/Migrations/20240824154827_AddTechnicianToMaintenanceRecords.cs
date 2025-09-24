using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace AircraftMaintenanceAPI.Migrations
{
    /// <inheritdoc />
   public partial class AddTechnicianToMaintenanceRecords : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.AddColumn<string>(
            name: "Technician",
            table: "MaintenanceRecords",
            type: "varchar(100)",
            maxLength: 100,
            nullable: false,
            defaultValue: "");
    }

    protected override void Down(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.DropColumn(
            name: "Technician",
            table: "MaintenanceRecords");
    }
}
}
