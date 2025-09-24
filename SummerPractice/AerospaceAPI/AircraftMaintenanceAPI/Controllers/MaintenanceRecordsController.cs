using Microsoft.AspNetCore.Mvc;
using AircraftMaintenanceAPI.Services;

namespace AircraftMaintenanceAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class MaintenanceRecordsController : ControllerBase
    {
        private readonly IMaintenanceRecordService _maintenanceRecordService;
        private readonly ILogger<MaintenanceRecordsController> _logger;

        public MaintenanceRecordsController(IMaintenanceRecordService maintenanceRecordService, ILogger<MaintenanceRecordsController> logger)
        {
            _maintenanceRecordService = maintenanceRecordService;
            _logger = logger;
        }
        
        [HttpPut("{id:int}")]
public async Task<IActionResult> UpdateMaintenanceRecord(int id, [FromBody] MaintenanceRecord record)
{
    _logger.LogInformation($"Attempting to update maintenance record {id}");
    
    // Log only non-sensitive fields
    _logger.LogDebug($"Update details: AircraftId: {record.AircraftId}, MaintenanceDate: {record.MaintenanceDate}, Technician: {record.Technician}");

    if (id != record.Id)
    {
        _logger.LogWarning($"Mismatched ID: URL ID = {id}, Record ID = {record.Id}");
        return BadRequest("The ID in the URL must match the ID in the record.");
    }

    if (!ModelState.IsValid)
    {
        _logger.LogWarning($"Invalid model state: {string.Join(", ", ModelState.Values.SelectMany(v => v.Errors).Select(e => e.ErrorMessage))}");
        return BadRequest(ModelState);
    }

    try
    {
        var result = await _maintenanceRecordService.UpdateMaintenanceRecordAsync(record);

        if (!result)
        {
            _logger.LogWarning($"Record not found: {id}");
            return NotFound();
        }

        _logger.LogInformation($"MaintenanceRecord updated successfully. Id: {id}");
        return NoContent();
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, $"Error occurred while updating maintenance record {id}");
        return StatusCode(500, "An error occurred while updating the maintenance record.");
    }
}
        // GET: api/MaintenanceRecords
        [HttpGet]
        public async Task<ActionResult<IEnumerable<MaintenanceRecord>>> GetMaintenanceRecords()
        {
            _logger.LogInformation("GetMaintenanceRecords called");
            return Ok(await _maintenanceRecordService.GetAllMaintenanceRecordsAsync());
        }

        // GET: api/MaintenanceRecords/5
        [HttpGet("{id:int}")]
        public async Task<ActionResult<MaintenanceRecord>> GetMaintenanceRecord(int id)
        {
            _logger.LogInformation("GetMaintenanceRecord called with id: {Id}", id);
            var maintenanceRecord = await _maintenanceRecordService.GetMaintenanceRecordByIdAsync(id);

            if (maintenanceRecord == null)
            {
                _logger.LogWarning("MaintenanceRecord not found for id: {Id}", id);
                return NotFound();
            }

            return Ok(maintenanceRecord);
        }

        // POST: api/MaintenanceRecords
        [HttpPost]
        public async Task<ActionResult<MaintenanceRecord>> PostMaintenanceRecord(CreateMaintenanceRecordDto dto)
        {
            _logger.LogInformation("PostMaintenanceRecord called with dto: {@Dto}", dto);

            if (!ModelState.IsValid)
            {
                _logger.LogWarning("Invalid ModelState: {@ModelState}", ModelState);
                return BadRequest(ModelState);
            }

            if (!await _maintenanceRecordService.AircraftExistsAsync(dto.AircraftId))
            {
                _logger.LogWarning("Invalid AircraftId: {AircraftId}", dto.AircraftId);
                return BadRequest("Invalid AircraftId");
            }

            var maintenanceRecord = new MaintenanceRecord
            {
                AircraftId = dto.AircraftId,
                Details = dto.Details,
                MaintenanceDate = dto.MaintenanceDate,
                Technician = dto.Technician
            };

            try
            {
                var createdRecord = await _maintenanceRecordService.CreateMaintenanceRecordAsync(maintenanceRecord);
                _logger.LogInformation("MaintenanceRecord created successfully: {@CreatedRecord}", createdRecord);
                return CreatedAtAction(nameof(GetMaintenanceRecord), new { id = createdRecord.Id }, createdRecord);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error occurred while creating MaintenanceRecord");
                return StatusCode(500, "An error occurred while creating the maintenance record.");
            }
        }

        // PUT: api/MaintenanceRecords/5
        [HttpPut("{id}")]
        public async Task<IActionResult> PutMaintenanceRecord(int id, MaintenanceRecord maintenanceRecord)
        {
            _logger.LogInformation("PutMaintenanceRecord called with id: {Id} and record: {@Record}", id, maintenanceRecord);

            if (id != maintenanceRecord.Id)
            {
                _logger.LogWarning("Mismatched Id in PutMaintenanceRecord. Path id: {PathId}, Record id: {RecordId}", id, maintenanceRecord.Id);
                return BadRequest();
            }

            var result = await _maintenanceRecordService.UpdateMaintenanceRecordAsync(maintenanceRecord);

            if (!result)
            {
                _logger.LogWarning("MaintenanceRecord not found for update. Id: {Id}", id);
                return NotFound();
            }

            _logger.LogInformation("MaintenanceRecord updated successfully. Id: {Id}", id);
            return NoContent();
        }

        // DELETE: api/MaintenanceRecords/5
        [HttpDelete("{id:int}")]
        public async Task<IActionResult> DeleteMaintenanceRecord(int id)
        {
            _logger.LogInformation("DeleteMaintenanceRecord called with id: {Id}", id);

            var result = await _maintenanceRecordService.DeleteMaintenanceRecordAsync(id);
            if (!result)
            {
                _logger.LogWarning("MaintenanceRecord not found for deletion. Id: {Id}", id);
                return NotFound();
            }

            _logger.LogInformation("MaintenanceRecord deleted successfully. Id: {Id}", id);
            return NoContent();
        }

        [HttpGet("aircraft/{aircraftId}")]
        public async Task<ActionResult<IEnumerable<MaintenanceRecord>>> GetMaintenanceRecordsByAircraftId(int aircraftId)
        {
            _logger.LogInformation("GetMaintenanceRecordsByAircraftId called with aircraftId: {AircraftId}", aircraftId);

            var records = await _maintenanceRecordService.GetMaintenanceRecordsByAircraftIdAsync(aircraftId);

            if (records == null || !records.Any())
            {
                _logger.LogWarning("No MaintenanceRecords found for aircraftId: {AircraftId}", aircraftId);
                return NotFound();
            }

            _logger.LogInformation("Retrieved {Count} MaintenanceRecords for aircraftId: {AircraftId}", records.Count(), aircraftId);
            return Ok(records);
        }
        
    }
}