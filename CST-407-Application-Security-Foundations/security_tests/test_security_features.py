import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _parse_properties(path: Path) -> dict:
    props = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            props[key.strip()] = value.strip()
    return props


def _non_comment_lines(text: str) -> list[str]:
    return [
        line
        for line in text.splitlines()
        if not line.strip().startswith("//")
    ]


def test_tls_config_properties_present():
    props_path = PROJECT_ROOT / "src" / "main" / "resources" / "application.properties"
    props = _parse_properties(props_path)

    assert props.get("server.ssl.enabled", "").lower() == "true"
    assert props.get("server.port") == "8443"
    assert props.get("server.ssl.key-store") == "classpath:keystore.p12"
    assert props.get("server.ssl.key-store-type") == "PKCS12"
    assert props.get("server.ssl.key-store-password") == "changeit"
    assert (PROJECT_ROOT / "src" / "main" / "resources" / "keystore.p12").exists()


def test_http_redirect_config_disabled_but_available():
    cfg_off = PROJECT_ROOT / "src" / "main" / "java" / "com" / "shadsluiter" / "eventsapp" / "config" / "HttpsRedirectConfig.java.off"
    cfg_on = cfg_off.with_suffix("")  # would be HttpsRedirectConfig.java

    assert cfg_off.exists(), "Redirect config is present (but disabled via .off suffix)."
    assert not cfg_on.exists(), "A .java redirect config should stay disabled; only the .off file should exist."

    content = cfg_off.read_text(encoding="utf-8")
    assert "SecurityConstraint" in content and "CONFIDENTIAL" in content
    assert "addAdditionalTomcatConnectors" in content and "setRedirectPort" in content


def test_event_repository_queries_are_parameterized():
    repo_path = PROJECT_ROOT / "src" / "main" / "java" / "com" / "shadsluiter" / "eventsapp" / "data" / "EventRepository.java"
    content = repo_path.read_text(encoding="utf-8")

    lines = _non_comment_lines(content)
    assert all('"+' not in line for line in lines), "Detected string concatenation in EventRepository SQL."

    required_patterns = [
        r"SELECT \* FROM events WHERE organizerid = \?",
        r"DELETE FROM events WHERE id = \?",
        r"INSERT INTO events \(name, date, location, organizerid, description\) VALUES \(\?, \?, \?, \?, \?\)",
        r"UPDATE events SET name = \?, date = \?, location = \?, organizerid = \?, description = \? WHERE id = \?",
        r"SELECT \* FROM events WHERE id = \?",
        r"SELECT \* FROM events WHERE description LIKE \?",
    ]
    for pattern in required_patterns:
        assert re.search(pattern, content), f"Missing parameterized query: {pattern}"


def test_user_repository_queries_are_parameterized():
    repo_path = PROJECT_ROOT / "src" / "main" / "java" / "com" / "shadsluiter" / "eventsapp" / "data" / "UserRepository.java"
    content = repo_path.read_text(encoding="utf-8")

    lines = _non_comment_lines(content)
    assert all('"+' not in line for line in lines), "Detected string concatenation in UserRepository SQL."

    required_patterns = [
        r"WHERE u\.login_name = \?",
        r"DELETE FROM users WHERE id = \?",
        r"INSERT INTO users \(login_name, password, enabled, account_non_expired, credentials_non_expired, account_non_locked\) VALUES \(\?, \?, \?, \?, \?, \?\)",
        r"UPDATE users SET login_name = \?, password = \?, enabled = \?, account_non_expired = \?, credentials_non_expired = \?, account_non_locked = \? WHERE id = \?",
        r"INSERT INTO roles \(user_id, role\) VALUES \(\?, \?\)",
        r"DELETE FROM roles WHERE user_id = \?",
        r"WHERE u\.id = \?",
    ]
    for pattern in required_patterns:
        assert re.search(pattern, content), f"Missing parameterized query: {pattern}"


def test_sanitization_service_uses_html_escape():
    service_path = PROJECT_ROOT / "src" / "main" / "java" / "com" / "shadsluiter" / "eventsapp" / "service" / "SanitizationService.java"
    content = service_path.read_text(encoding="utf-8")

    assert "HtmlUtils.htmlEscape" in content
    assert "sanitizeForDisplay" in content


def test_event_controller_sanitizes_before_render():
    controller_path = PROJECT_ROOT / "src" / "main" / "java" / "com" / "shadsluiter" / "eventsapp" / "controllers" / "EventController.java"
    content = controller_path.read_text(encoding="utf-8")

    assert "sanitizeForDisplay(events)" in content
    assert 'sanitizeText("Showing all events")' in content
    assert "safeQuery = sanitizationService.sanitizeText(query)" in content


def test_events_template_uses_utext_with_sanitized_values():
    template_path = PROJECT_ROOT / "src" / "main" / "resources" / "templates" / "events.html"
    content = template_path.read_text(encoding="utf-8")

    for field in ("event.name", "event.location", "event.organizerid", "event.description"):
        assert f'th:utext="${{{field}}}"' in content
