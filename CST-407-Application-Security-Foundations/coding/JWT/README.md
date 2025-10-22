# Activity 6 – Implementing REST API Security with JWT

This document distills the instructions from `CST-407-RS-T6-Activity-6-Implementing-REST-API-Security-JWT.docx` into a concise implementation guide. It covers the project goals, architecture, and the tasks completed in this repository.

## Objectives
- Explain JWT structure (header, payload, signature) and how stateless authentication works.
- Integrate JWT-based security in a Spring Boot REST API.
- Generate, validate, and parse JWT tokens with expiration and signature checks.
- Secure controller endpoints via Spring Security filters.
- Hash and store passwords securely using BCrypt.
- Test the secured API using tools such as Postman or the included sample JavaScript client.

## Project Overview
- **Application Type:** Spring Boot REST API secured with JWT.
- **API Resources:** Users (`/api/users`) and Orders (`/api/orders`).
- **Authentication Flow:** Username/password login → JWT token issuance → clients include the token in the `Authorization: Bearer <token>` header for protected endpoints.
- **Persistence:** In-memory H2 database with JPA entities for users and orders.
- **Password Security:** BCrypt hashing.
- **JWT Utilities:** Token generation, validation, and claim extraction encapsulated in `JwtTokenProvider`.
- **Security Filter:** `JwtAuthenticationFilter` intercepts requests and sets the authentication in the security context.

## Key Components
- `pom.xml` – Spring Boot project definition with JWT and security dependencies.
- `JwtTokenProvider` – creates, validates, and parses JWT tokens.
- `JwtAuthenticationFilter` – inspects incoming requests for valid JWT tokens.
- `SecurityConfig` – configures Spring Security to use the JWT filter, disable session state, and define protected endpoints.
- `UsersController` – handles user registration and login, returning JWT tokens on successful authentication.
- `OrdersController` – exposes CRUD endpoints protected by JWT authentication.
- `UserService` – manages user registration, password hashing, and authentication helpers.
- Data initialization via `DataInitializer` seeds sample users and orders for quick testing.

## JWT Configuration
Adjust JWT settings in `src/main/resources/application.properties`:

```properties
jwt.secret=change-me-in-production
jwt.expiration=3600000 # milliseconds (1 hour)
```

## Running the Project
1. Ensure JDK 17+ and Maven are installed.
2. From the `JWT/jwt-secured-api` directory run:
   ```sh
   mvn spring-boot:run
   ```
3. Use Postman, curl, or the sample JS client to:
   - Register or authenticate a user via `POST /api/users/register` or `POST /api/users/login`.
   - Use the returned JWT token to access protected endpoints such as `GET /api/orders`.

## Testing the API Manually
```sh
# Register a user
curl -X POST http://localhost:8080/api/users/register \
  -H 'Content-Type: application/json' \
  -d '{ "username": "dev", "password": "Password!23", "fullName": "Dev Team" }'

# Authenticate and capture token
TOKEN=$(curl -s -X POST http://localhost:8080/api/users/login \
  -H 'Content-Type: application/json' \
  -d '{ "username": "dev", "password": "Password!23" }' | jq -r '.token')

# Call a protected endpoint
curl http://localhost:8080/api/orders \
  -H "Authorization: Bearer $TOKEN"
```

_Tip:_ Install `jq` if you want to parse JSON in shell scripts.

## Deliverables Checklist
- ✅ Markdown implementation guide (this document).
- ✅ Spring Boot source code with JWT security.
- 📸 Add your own screenshots of the running application to the Word document as required by the assignment.
- 📦 Zip the project directory for submission when finished.
- 📝 (Optional) Export the API contract by running `curl http://localhost:8080/v3/api-docs -o swagger-spec.json` and include the file in your submission. Your reviewer can drag-and-drop `swagger-spec.json` into [https://editor.swagger.io](https://editor.swagger.io) or open `swagger-ui.html` in a browser to explore the endpoints.
