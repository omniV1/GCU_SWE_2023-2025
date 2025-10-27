package com.shadsluiter.eventsapp.controllers.api;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.shadsluiter.eventsapp.models.EventModel;
import com.shadsluiter.eventsapp.service.EventService;

import jakarta.validation.Valid;
import io.swagger.v3.oas.annotations.tags.Tag;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;

@RestController
@RequestMapping("/api/events")
@Tag(name = "Events", description = "Operations on event records")
public class EventsApiController {

    private final EventService eventService;

    public EventsApiController(EventService eventService) {
        this.eventService = eventService;
    }

    @GetMapping
    public ResponseEntity<List<EventModel>> getAllEvents() {
        return ResponseEntity.ok(eventService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<EventModel> getEventById(@PathVariable String id) {
        EventModel event = eventService.findById(id);
        if (event == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(event);
    }

    @GetMapping("/search")
    public ResponseEntity<List<EventModel>> searchEvents(@RequestParam("q") String query) {
        return ResponseEntity.ok(eventService.findByDescription(query));
    }

    @PostMapping
    @PreAuthorize("isAuthenticated()")
    @SecurityRequirement(name = "bearerAuth")
    public ResponseEntity<EventModel> createEvent(@RequestBody @Valid EventModel eventModel) {
        EventModel created = eventService.save(eventModel);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @PutMapping("/{id}")
    @PreAuthorize("isAuthenticated()")
    @SecurityRequirement(name = "bearerAuth")
    public ResponseEntity<EventModel> updateEvent(@PathVariable String id, @RequestBody @Valid EventModel eventModel) {
        EventModel existing = eventService.findById(id);
        if (existing == null) {
            return ResponseEntity.notFound().build();
        }
        eventModel.setId(id);
        EventModel updated = eventService.updateEvent(id, eventModel);
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("isAuthenticated()")
    @SecurityRequirement(name = "bearerAuth")
    public ResponseEntity<Void> deleteEvent(@PathVariable String id) {
        EventModel existing = eventService.findById(id);
        if (existing == null) {
            return ResponseEntity.notFound().build();
        }
        eventService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
