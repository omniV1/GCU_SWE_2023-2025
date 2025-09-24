using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

#pragma warning disable CA1814 // Prefer jagged arrays over multidimensional

namespace AircraftMaintenanceAPI.Migrations
{
    /// <inheritdoc />
    public partial class AddUserAndPerformanceMetric : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DeleteData(
                table: "Aircrafts",
                keyColumn: "Id",
                keyValue: 1);

            migrationBuilder.DeleteData(
                table: "Aircrafts",
                keyColumn: "Id",
                keyValue: 2);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.InsertData(
                table: "Aircrafts",
                columns: new[] { "Id", "LastMaintenanceDate", "MaintenancePerformed", "Model", "SerialNumber" },
                values: new object[,]
                {
                    { 1, new DateTime(2024, 8, 24, 8, 48, 26, 970, DateTimeKind.Local).AddTicks(8007), false, "Boeing 747", "SN747" },
                    { 2, new DateTime(2024, 8, 24, 8, 48, 26, 970, DateTimeKind.Local).AddTicks(8016), false, "Airbus A320", "SNA320" }
                });
        }
    }
}
