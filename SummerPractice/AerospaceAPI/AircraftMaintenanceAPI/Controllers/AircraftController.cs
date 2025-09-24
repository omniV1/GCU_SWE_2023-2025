using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AircraftMaintenanceAPI.Models;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Linq;
using AircraftMaintenanceAPI.Data;

namespace AircraftMaintenanceAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AircraftsController : ControllerBase
    {
        private readonly AircraftMaintenanceContext _context;

        public AircraftsController(AircraftMaintenanceContext context)
        {
            _context = context;
        }

        /// <summary>
        /// Get all aircrafts.
        /// </summary>
        /// <returns>List of all aircrafts</returns>
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Aircraft>>> GetAircrafts()
        {
            return await _context.Aircrafts.ToListAsync();
        }

        /// <summary>
        /// Get aircraft by ID.
        /// </summary>
        /// <param name="id">Aircraft ID</param>
        /// <returns>Aircraft details</returns>
        [HttpGet("{id}")]
        public async Task<ActionResult<Aircraft>> GetAircraft(int id)
        {
            var aircraft = await _context.Aircrafts.FindAsync(id);

            if (aircraft == null)
            {
                return NotFound();
            }

            return aircraft;
        }

        /// <summary>
        /// Add a new aircraft.
        /// </summary>
        /// <param name="aircraft">Aircraft details</param>
        /// <returns>Created aircraft</returns>
        [HttpPost]
        public async Task<ActionResult<Aircraft>> PostAircraft(Aircraft aircraft)
        {
            // Validate the model state
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            // Ensure the model and serial number are not null or empty
            if (string.IsNullOrWhiteSpace(aircraft.Model) || string.IsNullOrWhiteSpace(aircraft.SerialNumber))
            {
                return BadRequest("Model and Serial Number are required.");
            }

            // Add the aircraft to the context
            _context.Aircrafts.Add(aircraft);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetAircraft", new { id = aircraft.Id }, aircraft);
        }

        /// <summary>
        /// Update an aircraft.
        /// </summary>
        /// <param name="id">Aircraft ID</param>
        /// <param name="aircraft">Updated aircraft details</param>
        /// <returns>HTTP status code</returns>
        [HttpPut("{id}")]
        public async Task<IActionResult> PutAircraft(int id, Aircraft aircraft)
        {
            if (id != aircraft.Id)
            {
                return BadRequest("Aircraft ID mismatch.");
            }

            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            if (string.IsNullOrWhiteSpace(aircraft.Model) || string.IsNullOrWhiteSpace(aircraft.SerialNumber))
            {
                return BadRequest("Model and Serial Number are required.");
            }

            _context.Entry(aircraft).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!AircraftExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }


        /// <summary>
        /// Delete an aircraft.
        /// </summary>
        /// <param name="id">Aircraft ID</param>
        /// <returns>HTTP status code</returns>
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteAircraft(int id)
        {
            var aircraft = await _context.Aircrafts.FindAsync(id);
            if (aircraft == null)
            {
                return NotFound();
            }

            // Remove the aircraft from the context
            _context.Aircrafts.Remove(aircraft);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        /// <summary>
        /// Check if an aircraft exists.
        /// </summary>
        /// <param name="id">Aircraft ID</param>
        /// <returns>True if the aircraft exists, otherwise false</returns>
        private bool AircraftExists(int id)
        {
            return _context.Aircrafts.Any(e => e.Id == id);
        }

        [HttpGet("{id}/maintenance-records")]
public async Task<ActionResult<IEnumerable<MaintenanceRecord>>> GetMaintenanceRecords(int id)
{
    var aircraft = await _context.Aircrafts
        .Include(a => a.MaintenanceRecords)
        .FirstOrDefaultAsync(a => a.Id == id);

    if (aircraft == null)
    {
        return NotFound();
    }

    return Ok(aircraft.MaintenanceRecords);
}


    }
}
