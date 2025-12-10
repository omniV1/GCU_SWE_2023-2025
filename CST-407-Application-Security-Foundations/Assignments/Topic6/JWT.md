
<br>
<br><div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;">
  <h1>GCU Events Management System - Spring Boot Security Implementation</h1>
  <h2>Owen Lindsey</h2>
  <h2>Professor Sluiter, Shad</h2>
  <h2>CST-407</h2>
  <h2>Grand Canyon University</h2>
</div>

> This implementation guide distills `CST-407-RS-T6-Activity-6-Implementing-REST-API-Security-JWT.docx` into a working reference for the completed codebase. It highlights the security architecture, the development workflow, and the test evidence captured in the accompanying screenshots.

## Objectives

- **JWT Fundamentals:** describe token anatomy (header, payload, signature) and stateless authentication.
- **Secure Integration:** wire JWT-based security into a Spring Boot REST API.
- **Token Lifecycle:** issue, validate, and parse tokens with signed expiration claims.
- **Request Guarding:** route traffic through Spring Security filters instead of sessions.
- **Credential Safety:** hash and verify passwords via BCrypt.
- **Hands-on Testing:** exercise the API with curl, Swagger UI, or the provided sample client.

## Project Overview

Spring Boot hosts two main resource collections; users and orders, secured with JWT. The authentication journey is simple: submit credentials, receive a signed token, and present that token on each protected call. 

Key runtime traits:

- **API surface:** `/api/users` (registration, login, profile) and `/api/orders` (CRUD).
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpYXQiOjE3NjExNTkzOTMsImV4cCI6MTc2MTE2Mjk5M30.dF7l2fWLE0nbeyPvp1nef63QalWPQlcLaf2L_ab7xSs- **Security flow:** login → receive `Authorization: Bearer <token>` → access guarded endpoints.
- **Data storage:** H2 in-memory DB with JPA mappings for `UserAccount` and `CustomerOrder`.
- **Secret storage:** BCrypt password hashing ensures credentials are never stored in plain text.
- **Token services:** `JwtTokenProvider` encapsulates signing, validation, and claim extraction.
- **Filter chain:** `JwtAuthenticationFilter` inspects every request to populate the security context.

## Key Components

| Area                    | Files / Classes                                                 | Purpose                                                                |
| ----------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Build + Dependencies    | `pom.xml`                                                       | Declares Spring Boot starters, JWT libs, H2, and validation.           |
| Security Infrastructure | `SecurityConfig`, `JwtAuthenticationFilter`, `JwtTokenProvider` | Configures stateless security, validates tokens, and loads principals. |
| Authentication Services | `AuthService`, `CustomUserDetailsService`, `UserService`        | Authenticate credentials, fetch user details, and manage registration. |
| API Layer               | `UsersController`, `OrdersController`, `GlobalExceptionHandler` | Expose REST endpoints and standardize error responses.                 |
| Data Tier               | `UserAccount`, `CustomerOrder`, repositories, `DataInitializer` | Model domain entities, persist data, and seed demo records.            |

## JWT Configuration

JWT behavior is tuned via `src/main/resources/application.properties`:

```properties
jwt.secret=change-me-in-production
jwt.expiration=3600000 # milliseconds (1 hour)
```

## Running the Project

1. **Prepare tooling.** JDK 17+ and Maven must be available on your PATH.
2. **Start the service.**

   ```sh
   cd JWT/jwt-secured-api
   mvn spring-boot:run
   ```

3. **Authenticate and test.** Issue requests with curl, Swagger UI, or Postman to register/login and then supply the bearer token on protected routes.

> Need a UI? Launch `http://localhost:8080/swagger-ui/index.html` and interact with every endpoint in the browser.

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


## Screenshots & Scenario Walkthrough

Every image in `Screenshots/` corresponds to a checkpoint in the security flow:

- **Bootstrapping:** ![[AppRuns.png]]

confirms the service, H2 database, and filter chain all start successfully.

- **Onboarding:** ![[Successful_Registration.png]]

demonstrates server-side validation and BCrypt hashing when creating users.

- **Authentication:** ![[SuccessfulLogin.png]]

records the JWT payload returned to the caller.

- **Identity Verification:** ![[FindUser.png]] 
shows that `/api/users/me` is unreachable without a bearer token.

- **Data Access:**  ![[SuccessfullyFindingOrder.png]]

Gets the id 1 itmeprove orders are filtered by the authenticated principal.

- **State Changes:** ![[SuccessfulDelete.png]]

and `SuccessfulDelete.png` capture protected POST/DELETE flows that succeed only with valid credentials.

- **Add an Order:** ![[AddAnOrder.png]]

- **Order Look up:*
- ![[Pasted image 20251022124714.png]]

