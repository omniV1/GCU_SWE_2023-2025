package com.shadsluiter.eventsapp.service;

import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;
import org.springframework.web.util.HtmlUtils;

import com.shadsluiter.eventsapp.models.EventModel;

/**
 * Escapes user-controlled values so we can safely render them with th:utext.
 * This preserves the original input (users see exactly what they typed)
 * while ensuring the browser never executes the markup.
 */
@Service
public class SanitizationService {

    public String sanitizeText(String input) {
        if (input == null) {
            return "";
        }
        return HtmlUtils.htmlEscape(input, StandardCharsets.UTF_8.name());
    }

    public EventModel sanitizeForDisplay(EventModel eventModel) {
        if (eventModel == null) {
            return null;
        }
        EventModel sanitized = new EventModel();
        sanitized.setId(eventModel.getId());
        sanitized.setName(sanitizeText(eventModel.getName()));
        sanitized.setDate(eventModel.getDate());
        sanitized.setLocation(sanitizeText(eventModel.getLocation()));
        sanitized.setOrganizerid(sanitizeText(eventModel.getOrganizerid()));
        sanitized.setDescription(sanitizeText(eventModel.getDescription()));
        return sanitized;
    }

    public List<EventModel> sanitizeForDisplay(List<EventModel> events) {
        if (events == null) {
            return List.of();
        }
        return events.stream()
                .filter(Objects::nonNull)
                .map(this::sanitizeForDisplay)
                .collect(Collectors.toList());
    }
}
