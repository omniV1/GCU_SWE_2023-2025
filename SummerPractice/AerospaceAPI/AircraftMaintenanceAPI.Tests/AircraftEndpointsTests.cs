using System.Net;
using System.Net.Http.Json;
using AircraftMaintenanceAPI.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace AircraftMaintenanceAPI.Tests;

public class AircraftEndpointsTests : IClassFixture<AircraftApiFactory>
{
    private readonly HttpClient _client;

    public AircraftEndpointsTests(AircraftApiFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetAircraft_WhenAircraftDoesNotExist_ReturnsNotFound()
    {
        var response = await _client.GetAsync("/api/aircrafts/999");

        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
    }

    [Fact]
    public async Task PostAircraft_WithValidAircraft_CreatesRetrievableAircraft()
    {
        var aircraft = new Aircraft
        {
            Model = "Cessna 172",
            SerialNumber = "TEST-172",
            LastMaintenanceDate = new DateTime(2026, 7, 1, 0, 0, 0, DateTimeKind.Utc)
        };

        var createResponse = await _client.PostAsJsonAsync("/api/aircrafts", aircraft);

        Assert.Equal(HttpStatusCode.Created, createResponse.StatusCode);
        var createdAircraft = await createResponse.Content.ReadFromJsonAsync<Aircraft>();
        Assert.NotNull(createdAircraft);
        Assert.True(createdAircraft.Id > 0);

        var savedAircraft = await _client.GetFromJsonAsync<Aircraft>(
            $"/api/aircrafts/{createdAircraft.Id}");
        Assert.Equal("TEST-172", savedAircraft?.SerialNumber);
    }

    [Fact]
    public async Task PostAircraft_WithoutModel_ReturnsBadRequest()
    {
        var aircraft = new Aircraft { SerialNumber = "TEST-MISSING-MODEL" };

        var response = await _client.PostAsJsonAsync("/api/aircrafts", aircraft);

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }
}

public sealed class AircraftApiFactory : WebApplicationFactory<Program>
{
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.UseEnvironment("Development");
        var databaseName = $"AircraftApiTests-{Guid.NewGuid()}";

        builder.ConfigureServices(services =>
        {
            services.RemoveAll<DbContextOptions<AircraftMaintenanceContext>>();
            services.RemoveAll<AircraftMaintenanceContext>();
            services.AddDbContext<AircraftMaintenanceContext>(options =>
                options.UseInMemoryDatabase(databaseName));
        });
    }
}
