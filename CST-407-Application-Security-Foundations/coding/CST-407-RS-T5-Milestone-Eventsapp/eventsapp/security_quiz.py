"""
Interactive multiple-choice quiz about the EventsApp security features.
Questions reflect what the codebase actually does (TLS/SSL, HTTP vs HTTPS,
SQL injection mitigations, and XSS handling).
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    prompt: str
    choices: List[str]
    correct: str
    explanation: str


def ask(question: Question) -> bool:
    print("\n" + question.prompt)
    for label, choice in zip("ABCD", question.choices):
        print(f"  {label}) {choice}")
    answer = input("Your answer (A-D): ").strip().upper()
    is_correct = answer == question.correct.upper()
    if is_correct:
        print("Correct.")
    else:
        print(f"Incorrect. Correct answer: {question.correct}")
    print("   " + question.explanation)
    return is_correct


def main() -> None:
    questions = [
        Question(
            prompt="Which port does the application listen on for HTTPS according to application.properties?",
            choices=["8080", "443", "8443", "3000"],
            correct="C",
            explanation="server.port=8443 is set in src/main/resources/application.properties.",
        ),
        Question(
            prompt="Which file contains the HTTP-to-HTTPS redirect logic and why is it inactive?",
            choices=[
                "SecurityConfig.java; CSRF disables it",
                "HttpsRedirectConfig.java.off; the .off suffix keeps it from compiling",
                "EventsApplication.java; redirect is disabled in main",
                "application.properties; redirect is disabled by a property flag",
            ],
            correct="B",
            explanation="HttpsRedirectConfig.java.off adds a connector and SecurityConstraint(CONFIDENTIAL), but the .off suffix excludes it from the build.",
        ),
        Question(
            prompt="Which property sets the HTTP port that would be redirected to HTTPS if the redirect config were enabled?",
            choices=["server.port", "server.http.port", "server.ssl.port", "server.redirect.port"],
            correct="B",
            explanation="server.http.port=8080 is defined for the plain HTTP listener used only if HttpsRedirectConfig is activated.",
        ),
        Question(
            prompt="What keystore configuration is used for TLS?",
            choices=[
                "JKS keystore on disk with alias default",
                "PKCS12 keystore at classpath:keystore.p12 with alias eventsapp",
                "PEM key and cert in environment variables",
                "No keystore; TLS is terminated upstream",
            ],
            correct="B",
            explanation="application.properties sets server.ssl.key-store=classpath:keystore.p12, key-store-type=PKCS12, and key-alias=eventsapp.",
        ),
        Question(
            prompt="How does EventRepository prevent SQL injection in its queries?",
            choices=[
                "Manual escaping of quotes",
                "Stored procedures only",
                "Parameterized queries with ? placeholders in JdbcTemplate",
                "Blacklisting dangerous keywords",
            ],
            correct="C",
            explanation="All EventRepository queries use ? placeholders (SELECT/INSERT/UPDATE/DELETE and LIKE search) with JdbcTemplate prepared statements.",
        ),
        Question(
            prompt="What prevents string concatenation-based SQL in EventRepository and UserRepository?",
            choices=[
                "Use of StringBuilder only",
                "Comments warning against concatenation and exclusive use of ? parameters",
                "Runtime SQL parser",
                "ORM auto-escaping",
            ],
            correct="B",
            explanation="Both repositories rely solely on prepared statements with ? placeholders; prior concatenation examples are commented out as vulnerable.",
        ),
        Question(
            prompt="How is the LIKE search for descriptions made safe in EventRepository?",
            choices=[
                "Concatenating '%' in SQL text",
                "Using a parameterized LIKE with '%' added to the bound value",
                "Escaping percent signs manually",
                "Disabling LIKE entirely",
            ],
            correct="B",
            explanation="The query is \"... description LIKE ?\" and the bound parameter is \"%\" + searchTerm + \"%\" so no SQL is concatenated.",
        ),
        Question(
            prompt="How does UserRepository set roles when a new user is created?",
            choices=[
                "Hard-codes ROLE_USER only",
                "Leaves roles empty",
                "Adds ROLE_USER and ROLE_ADMIN when roles are null",
                "Copies roles from the first user in the database",
            ],
            correct="C",
            explanation="On new users, if roles are null it sets a HashSet with ROLE_USER and ROLE_ADMIN before inserting.",
        ),
        Question(
            prompt="Which password encoder is used for hashing user passwords?",
            choices=[
                "No hashing; plain text",
                "MD5PasswordEncoder",
                "BCryptPasswordEncoder",
                "PBKDF2 with defaults",
            ],
            correct="C",
            explanation="SecurityConfig defines a BCryptPasswordEncoder bean used by the authentication stack.",
        ),
        Question(
            prompt="Where is HTML escaping applied to event fields to prevent XSS?",
            choices=[
                "Only in Thymeleaf via th:text",
                "In SanitizationService using HtmlUtils.htmlEscape before rendering",
                "In the database via triggers",
                "Nowhere; raw HTML is rendered",
            ],
            correct="B",
            explanation="SanitizationService escapes each field with HtmlUtils.htmlEscape(UTF-8) and controllers pass sanitized models to the views.",
        ),
        Question(
            prompt="Why is it safe to use th:utext for event fields in events.html?",
            choices=[
                "th:utext escapes automatically",
                "Data is pre-escaped by SanitizationService before reaching the template",
                "Browsers block all scripts in tables",
                "Content Security Policy headers enforce safety",
            ],
            correct="B",
            explanation="th:utext would render raw HTML, but inputs are already escaped, so markup cannot execute.",
        ),
        Question(
            prompt="How is the search feedback message protected from XSS in EventController?",
            choices=[
                "It is not rendered",
                "It uses th:text automatically",
                "The query is escaped via sanitizeText before being concatenated into the message",
                "The query is validated to allow only alphanumerics",
            ],
            correct="C",
            explanation="The controller builds the message with sanitizeText(query) to ensure the echoed search string is escaped.",
        ),
        Question(
            prompt="Which endpoints are publicly accessible in the API security filter chain?",
            choices=[
                "All /api/** endpoints",
                "POST /api/users/login and /api/users/register, GET /api/events/**",
                "Only POST /api/users/register",
                "None; all require JWT",
            ],
            correct="B",
            explanation="SecurityConfig permits POST login/register and GET /api/events/**, requiring JWT for other /api/** calls.",
        ),
        Question(
            prompt="What session policy is applied to the /api/** security filter chain?",
            choices=[
                "STATELESS; JWT filter handles auth and CSRF is disabled",
                "STATEFUL with JSESSIONID",
                "Session fixation protection only",
                "Remember-me tokens",
            ],
            correct="A",
            explanation="The API filter chain sets SessionCreationPolicy.STATELESS, disables CSRF, and adds JwtAuthenticationFilter before UsernamePasswordAuthenticationFilter.",
        ),
        Question(
            prompt="Where is the JWT filter inserted in the API filter chain?",
            choices=[
                "After UsernamePasswordAuthenticationFilter",
                "Before UsernamePasswordAuthenticationFilter",
                "At the very end of the chain",
                "It is not registered",
            ],
            correct="B",
            explanation="SecurityConfig adds JwtAuthenticationFilter before UsernamePasswordAuthenticationFilter for /api/**.",
        ),
        Question(
            prompt="Which endpoints are publicly permitted in the form-login SecurityFilterChain?",
            choices=[
                "Only /",
                "/, /users/register, /users/loginForm, static assets, Swagger UI",
                "All /events/** endpoints",
                "Only /swagger-ui/**",
            ],
            correct="B",
            explanation="Permit list: /, /users/register, /users/loginForm, /css/**, /js/**, /images/**, /swagger-ui/**, /v3/api-docs/**, /swagger-ui.html.",
        ),
        Question(
            prompt="What is the CSRF configuration for the form-login security filter chain?",
            choices=[
                "Enabled with tokens in forms",
                "Disabled at the end of the chain",
                "Enabled only for GET",
                "Enabled only for /users/**",
            ],
            correct="B",
            explanation="The formLogin filter chain ends with csrf().disable().",
        ),
        Question(
            prompt="How are JWT secrets and expiration configured?",
            choices=[
                "Hard-coded in SecurityConfig",
                "Pulled from environment variables only",
                "Loaded from application.properties as app.jwt.secret and app.jwt.expiration",
                "Generated per request",
            ],
            correct="C",
            explanation="application.properties defines app.jwt.secret and app.jwt.expiration (ms) used by JwtService/JwtAuthenticationFilter.",
        ),
        Question(
            prompt="Which property sets the keystore password used for TLS?",
            choices=[
                "server.ssl.key-store-password=changeit",
                "server.ssl.trust-store-password",
                "spring.datasource.password",
                "app.jwt.secret",
            ],
            correct="A",
            explanation="application.properties sets server.ssl.key-store-password=changeit for the PKCS12 keystore.",
        ),
        Question(
            prompt="Which alias is used to select the certificate from the keystore?",
            choices=[
                "tomcat",
                "eventsapp",
                "default",
                "server",
            ],
            correct="B",
            explanation="server.ssl.key-alias=eventsapp is set in application.properties.",
        ),
        Question(
            prompt="What is the default state of CSRF protection for the /api/** chain?",
            choices=[
                "Enabled with tokens",
                "Disabled explicitly",
                "Enabled only for POST",
                "Enabled only for GET",
            ],
            correct="B",
            explanation="The API security chain calls csrf().disable() to suit stateless JWT usage.",
        ),
        Question(
            prompt="Which configuration controls public Swagger/OpenAPI access?",
            choices=[
                "OpenApiConfig permits all automatically",
                "SecurityConfig form chain permits /swagger-ui/**, /v3/api-docs/**, and /swagger-ui.html",
                "JwtAuthenticationFilter bypasses swagger paths",
                "application.properties security.swagger.enabled",
            ],
            correct="B",
            explanation="SecurityConfig explicitly permits the Swagger UI and docs paths in the form-login chain.",
        ),
        # Expert-level questions
        Question(
            prompt="How does the application map a JWT authentication failure to an HTTP response?",
            choices=[
                "SecurityConfig sets a default 401 without a handler",
                "JwtAuthenticationEntryPoint is configured as the authenticationEntryPoint for /api/**",
                "UsernamePasswordAuthenticationFilter writes the 401 directly",
                "JwtService throws an exception caught by a @ControllerAdvice",
            ],
            correct="B",
            explanation="SecurityConfig apiFilterChain registers JwtAuthenticationEntryPoint for exceptionHandling().",
        ),
        Question(
            prompt="Which authentication flows coexist, and how are they isolated?",
            choices=[
                "Only form-login is used; JWT is unused",
                "Only JWT is used; form-login is unused",
                "Separate security filter chains: @Order(1) JWT stateless for /api/**, @Order(2) form login for web",
                "Both flows run in the same filter chain for all paths",
            ],
            correct="C",
            explanation="Two SecurityFilterChain beans: ordered JWT stateless for /api/**, form-login for MVC pages.",
        ),
        Question(
            prompt="How is password hashing enforced across user creation and authentication?",
            choices=[
                "Plain text passwords; no encoder",
                "BCryptPasswordEncoder bean is provided; user passwords must be stored already-hashed",
                "MD5 hashing in UserService",
                "SHA-1 hashing in JdbcTemplate",
            ],
            correct="B",
            explanation="SecurityConfig exposes BCryptPasswordEncoder; user persistence must use the encoder before storage.",
        ),
        Question(
            prompt="Which HTTP methods are explicitly permitted without authentication on /api/events/**?",
            choices=[
                "All methods",
                "GET only",
                "GET and POST",
                "POST only",
            ],
            correct="B",
            explanation="SecurityConfig permits HttpMethod.GET for /api/events/**; other methods require JWT.",
        ),
        Question(
            prompt="What is the token lifetime configuration for JWTs?",
            choices=[
                "No expiration",
                "Configured via app.jwt.expiration in application.properties",
                "Hard-coded in JwtAuthenticationFilter",
                "Computed from system time in SecurityConfig",
            ],
            correct="B",
            explanation="application.properties sets app.jwt.expiration=3600000 (ms).",
        ),
        Question(
            prompt="How does SanitizationService handle null inputs when escaping?",
            choices=[
                "Throws NullPointerException",
                "Returns None",
                "Returns empty string for null input",
                "Skips escaping",
            ],
            correct="C",
            explanation="sanitizeText returns \"\" when input is null before calling HtmlUtils.htmlEscape.",
        ),
        Question(
            prompt="Why is th:utext used instead of th:text in events.html despite XSS risk?",
            choices=[
                "To allow raw HTML from users",
                "Because th:text is unavailable",
                "To preserve user formatting while relying on pre-escaped values from SanitizationService",
                "By mistake; it should be th:text",
            ],
            correct="C",
            explanation="SanitizationService escapes content so th:utext can render formatting without executing scripts.",
        ),
        Question(
            prompt="What is the default role assignment logic for new users and how could that affect access control?",
            choices=[
                "Assigns no roles, blocking access",
                "Assigns ROLE_USER only, least privilege",
                "Assigns ROLE_USER and ROLE_ADMIN, granting admin rights by default",
                "Copies roles from the registering user’s session",
            ],
            correct="C",
            explanation="UserRepository sets ROLE_USER and ROLE_ADMIN when roles are null; this grants admin access by default.",
        ),
        Question(
            prompt="How are database connections authenticated according to application.properties?",
            choices=[
                "Anonymous access to MySQL",
                "Using username and password both set to eventsapp",
                "Using integrated OS authentication",
                "Using TLS client certificates",
            ],
            correct="B",
            explanation="spring.datasource.username=eventsapp and spring.datasource.password=eventsapp in application.properties.",
        ),
        Question(
            prompt="Which parts of SecurityConfig disable CSRF, and why is that acceptable or risky?",
            choices=[
                "Only the API chain disables CSRF; stateless JWT justifies it",
                "Only the form chain disables CSRF; form logins are stateless",
                "Both chains disable CSRF; acceptable for stateless API but risky for form-based endpoints if cookies are used",
                "Neither chain disables CSRF",
            ],
            correct="C",
            explanation="Both apiFilterChain and formFilterChain call csrf().disable(); OK for stateless JWT, but form endpoints could be exposed to CSRF if cookies/JSESSIONID are in play.",
        ),
        # General security concepts
        Question(
            prompt="What is the primary difference between HTTP and HTTPS?",
            choices=[
                "HTTPS compresses data only",
                "HTTPS encrypts transport with TLS to provide confidentiality and integrity",
                "HTTPS changes the HTTP verbs",
                "HTTPS is only for APIs, not browsers",
            ],
            correct="B",
            explanation="HTTPS wraps HTTP in TLS, providing encryption and integrity.",
        ),
        Question(
            prompt="What is the role of a Certificate Authority (CA) in TLS?",
            choices=[
                "Issuing JWT tokens",
                "Signing server certificates to establish trust",
                "Managing DNS records",
                "Configuring firewalls",
            ],
            correct="B",
            explanation="A CA signs server certificates so clients can trust the server’s identity.",
        ),
        Question(
            prompt="What does HSTS (HTTP Strict Transport Security) do?",
            choices=[
                "Forces the browser to always use HTTPS for the site",
                "Enables HTTP/2",
                "Blocks all cookies",
                "Disables caching",
            ],
            correct="A",
            explanation="HSTS tells browsers to refuse HTTP and use HTTPS only for the host.",
        ),
        Question(
            prompt="Why do prepared statements mitigate SQL injection?",
            choices=[
                "They escape quotes automatically",
                "They send SQL and parameters separately so user data cannot alter the query structure",
                "They run faster",
                "They use stored procedures by default",
            ],
            correct="B",
            explanation="Prepared statements bind parameters separately, preventing user input from changing SQL syntax.",
        ),
        Question(
            prompt="When using LIKE with user input, what is the safest pattern?",
            choices=[
                "Concatenate '%' and the input directly in SQL",
                "Use parameter binding and add '%' to the parameter value, not to the SQL string",
                "Disallow LIKE entirely",
                "Escape only single quotes",
            ],
            correct="B",
            explanation="Keep SQL static and bind \"%{input}%\" as a parameter to avoid injection.",
        ),
        Question(
            prompt="What distinguishes stored XSS from reflected XSS?",
            choices=[
                "Stored XSS is only on mobile devices",
                "Stored XSS is persisted on the server and served to users; reflected is delivered in the immediate response",
                "Reflected XSS requires login; stored does not",
                "They are the same",
            ],
            correct="B",
            explanation="Stored XSS lives in persisted data; reflected comes from the current request.",
        ),
        Question(
            prompt="Why is output encoding (escaping) important for XSS defense?",
            choices=[
                "It validates input length",
                "It ensures untrusted data is rendered as text rather than executable markup/script",
                "It encrypts the page",
                "It blocks all HTML tags",
            ],
            correct="B",
            explanation="Proper context-aware escaping prevents execution of untrusted content when rendered.",
        ),
        Question(
            prompt="Why is bcrypt preferred over plain SHA-256 for password storage?",
            choices=[
                "It is faster",
                "It is reversible",
                "It is deliberately slow and includes a salt, resisting brute force and rainbow tables",
                "It stores passwords in cleartext",
            ],
            correct="C",
            explanation="BCrypt is salted and tunably slow, making offline cracking harder than fast hashes like SHA-256.",
        ),
        Question(
            prompt="What is the purpose of issuer/audience claims in JWTs?",
            choices=[
                "To compress the token",
                "To specify which server issued the token and which recipients it is intended for",
                "To choose the hashing algorithm",
                "To store passwords",
            ],
            correct="B",
            explanation="iss/aud identify the token’s source and intended recipients to prevent token replay across services.",
        ),
        Question(
            prompt="When are CSRF tokens generally required?",
            choices=[
                "For stateless APIs using Authorization headers",
                "For any state-changing requests that rely on browser cookies for auth",
                "Only for GET requests",
                "Never, if TLS is used",
            ],
            correct="B",
            explanation="If auth is cookie-based, state-changing requests should include CSRF tokens to prevent cross-site submission.",
        ),
        Question(
            prompt="What does the HttpOnly flag on cookies protect against?",
            choices=[
                "Man-in-the-middle attacks",
                "Reading the cookie via client-side scripts (e.g., in XSS)",
                "SQL injection",
                "CSRF",
            ],
            correct="B",
            explanation="HttpOnly prevents JavaScript from accessing the cookie, reducing XSS impact on session theft.",
        ),
        Question(
            prompt="How does the SameSite cookie attribute help with CSRF?",
            choices=[
                "It encrypts cookies",
                "It blocks all cookies",
                "It limits cookies from being sent on cross-site requests, reducing CSRF risk",
                "It forces HTTPS",
            ],
            correct="C",
            explanation="SameSite restricts cross-site cookie sending, mitigating CSRF in many cases.",
        ),
        Question(
            prompt="Why use least-privilege database credentials for an app account?",
            choices=[
                "To speed up queries",
                "To minimize damage if the app is compromised",
                "To enable TLS",
                "To allow OS logins",
            ],
            correct="B",
            explanation="Restricting DB permissions limits impact if injection or credential theft occurs.",
        ),
        Question(
            prompt="What is input validation’s role compared to output encoding for XSS defense?",
            choices=[
                "Validation alone stops XSS",
                "Validation checks allowed formats; output encoding neutralizes whatever passes validation before rendering",
                "Encoding is unnecessary if validation exists",
                "They are identical controls",
            ],
            correct="B",
            explanation="Validation constrains inputs; encoding ensures any remaining untrusted data is safe to render.",
        ),
        Question(
            prompt="What is the main goal of the TLS handshake?",
            choices=[
                "To set HTTP headers",
                "To negotiate cipher suites and establish shared keys for encrypted communication",
                "To compress responses",
                "To validate SQL queries",
            ],
            correct="B",
            explanation="TLS handshake agrees on cryptographic parameters and keys for secure transport.",
        ),
    ]

    score = sum(ask(q) for q in questions)
    total = len(questions)
    percent = (score / total) * 100 if total else 0
    print(f"\nScore: {score} / {total} correct ({percent:.1f}%)")


if __name__ == "__main__":
    main()
