
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;">
  <h1>GCU Events Management System - JWT REST API Expansion</h1>
  <h2>Owen Lindsey</h2>
  <h2>Professor Sluiter, Shad</h2>
  <h2>CST-407</h2>
  <h2>Grand Canyon University</h2>
</div>



## Project Overview

This milestone extends the Spring Boot security foundation by delivering a full-featured REST API secured with JSON Web Tokens (JWT). Two controller layers were introduced: `EventsApiController` delivers CRUD endpoints for the `eventsapp` schema, while `UsersApiController` manages registration, authentication, and token inspection. With JWT enforced at the filter chain, the application now supports stateless integration scenarios alongside the existing Thymeleaf experience showcased in Milestone 1.

Key goals achieved:

- REST endpoints hosted at `/api/events` and `/api/users`, organized with OpenAPI metadata for quick discovery.
- Secure create/update/delete/event-admin flows accessible only to JWT-authenticated users.
- Public read/search endpoints enabling anonymous discovery of event content.
- Documentation-first workflow through Swagger UI (and Postman parity) to accelerate partner onboarding.

<div style="page-break-after: always;"></div>

## Video Demonstration

**Link to 5-minute demonstration video:** _Pending upload (Milestone 2 recording in progress)._

The Milestone 2 video will highlight:

1. **JWT Login Flow** – obtaining a token via `/api/users/login` and storing it in Swagger's or Postman's Authorization context.
2. **Secure CRUD** – creating, updating, and deleting events with the `Authorization: Bearer <token>` header, contrasted against rejected unauthenticated attempts.
3. **Public Access** – browsing `/api/events` and `/api/events/search` without credentials.
4. **User Lifecycle** – registering a new account, logging in, and verifying `/api/users/me`.

Screenshots captured during rehearsal are archived in the `@Photos` album for quick reference; the final recording will mirror those flows.

<div style="page-break-after: always;"></div>

## API Architecture

### Events API (`/api/events`)

- `GET /api/events` – Lists all events; open to everyone.
- `GET /api/events/{id}` – Retrieves a single record or returns HTTP 404.
- `GET /api/events/search?q=term` – Full text search across event descriptions.
- `POST /api/events` – Creates a new event; JWT required.
- `PUT /api/events/{id}` – Updates an existing event; JWT required.
- `DELETE /api/events/{id}` – Removes an event; JWT required.

Validation is applied through `@Valid` and `EventModel`, keeping the API consistent with the service layer. Responses return `EventModel` payloads to align with future mobile or SPA consumers.

### Users API (`/api/users`)

- `POST /api/users/register` – Accepts `RegisterRequest` to create a user backed by BCrypt hashing.
- `POST /api/users/login` – Authenticates credentials and returns `AuthResponse` (JWT, expiration, user payload).
- `GET /api/users/me` – Returns the authenticated profile; secured by `@PreAuthorize("isAuthenticated()")`.

Role assignment defaults to `ROLE_USER`; additional roles can be added without modifying controller logic because Spring Security inspects the JWT claims exposed by `JwtService`.

<div style="page-break-after: always;"></div>

## JWT Authentication Flow

1. **Login** – `/api/users/login` authenticates against `AuthenticationManager` using `UsernamePasswordAuthenticationToken`.
2. **Token Issuance** – `JwtService.generateToken` issues a signed token with issuer, expiration, and username claims.
3. **Request Filtering** – `JwtAuthenticationFilter` intercepts `/api/**` traffic, validating tokens and populating the `SecurityContext`.
4. **Authorization** – `SecurityConfig` gates sensitive routes; unauthenticated calls receive HTTP 401 via `JwtAuthenticationEntryPoint`.
5. **Stateless Sessions** – `SessionCreationPolicy.STATELESS` ensures scalability for API clients and microservice consumers.

The secret, issuer, and expiration settings live in `application.properties`. Updates to those values invalidate existing tokens, reinforcing controlled access.

<div style="page-break-after: always;"></div>

## API Tooling & Demonstration Notes

### Swagger UI

- Hosted at `http://localhost:8080/swagger-ui/index.html`.
- Uses the OpenAPI configuration (`OpenApiConfig`) to expose the `bearerAuth` security scheme.
- “Authorize” button accepts the JWT from the login response. Once authorized, Swagger persists the header for subsequent secured endpoints.
- Screenshots in `@Photos` capture login, authorized POST/PUT/DELETE flows, and 401 responses when omitting the token.

### Postman Parity (per assignment instructions)

- **Login Collection** – Send `POST http://localhost:8080/api/users/login` with JSON body:
  ```json
  {
    "userName": "root",
    "password": "root"
  }
  ```
- **Set Environment Variable** – Store the `token` field as `{{jwt_token}}`.
- **Protected Call** – Example update:
  ```
  PUT http://localhost:8080/api/events/3
  Authorization: Bearer {{jwt_token}}
  Content-Type: application/json
  ```
- **Negative Test** – Duplicate the request without Authorization header to capture the 401 response required by the rubric.

The forthcoming screencast will walk through this collection to satisfy the deliverable.

<div style="page-break-after: always;"></div>

## Database & Data Seeding

- MariaDB 12.0.2 running locally on Arch Linux (`systemctl enable --now mariadb`).
- `eventsapp.sql` loaded into `eventsapp` schema with seeded `users`, `roles`, and `events` tables.
- `AuthenticationManager` relies on `CustomUserDetailsService`, which fetches users from the seeded data (initial admin user: `root` / `root`).
- Future demos can register new accounts through the API without manual SQL scripts.

<div style="page-break-after: always;"></div>

## Testing & Verification Checklist

1. `GET /api/events` – succeeds without token.
2. `POST /api/events` – succeeds with token, fails with 401 without token.
3. `PUT /api/events/{id}` – similar success/failure scenarios recorded.
4. `DELETE /api/events/{id}` – confirms audit trail by removing test data created earlier in the session.
5. `GET /api/users/me` – returns authenticated user details when token is present.

Logs (`spring.jpa.show-sql=true` and `spring.jpa.hibernate.ddl-auto=update`) assist in verifying database persistence during the demo.

<div style="page-break-after: always;"></div>

## Next Steps & Submission Notes

- **Video Production** – Record the 5-minute walkthrough covering the flows outlined above, ensuring both successful and unauthorized attempts are shown.
- **Deliverables Package** – Submit source tree (excluding `target/`), the SQL dump, and the demonstration video link.
- **Optional Enhancements** – Add role-based authorization (e.g., `ROLE_ADMIN`) or token refresh endpoints if future milestones request extended functionality.

With these additions, the application now satisfies the Milestone 2 objectives by providing JWT-secured REST services, thorough documentation, and reproducible demonstrations via Swagger UI and Postman.

