<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;">
  <h1>Spring Security Configuration</h1>
  <h2>Owen Lindsey</h2>
  <h2>Professor Sluiter, Shad</h2>
  <h2>CST-407</h2>
  <h2>Grand Canyon University</h2>
</div>

<div style="page-break-after: always;"></div>

### **Spring Security Coding activity**

Download the [prepackaged java code utilizing Spring](https://halo.gcu.edu/resource/cb74c27f-f989-440b-83a6-c1b35abb107a) initialize the Maven repository, update and clean any package errors or paths. Then add Spring boot starter security.

```json
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

This dependency is a collection of other security dependencies for authentication and authorization. The security dependencies included in the starter group include:

**spring-security-core whose classes include:**

| Classes               | Function                                                            | Typical Methods/Usage                                          |
| --------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------- |
| AuthenticationManager | Orchestrates authentication by delegating to one or more providers  | `authenticate(Authentication)`                                 |
| UserDetails           | Contract describing the authenticated user                          | Getters like `getUsername()`, `getPassword()`, authorities     |
| UserService           | Application service to manage users (domain + security integration) | `save(...)`, `findByLoginName(...)`, `loadUserByUsername(...)` |
| BCryptPasswordEncoder | Password hashing using BCrypt                                       | `encode(rawPassword)`, `matches(raw, encoded)`                 |
| GrantedAuthority      | Represents a permission/role granted to the user                    | Implementations like `SimpleGrantedAuthority("ROLE_ADMIN")`    |

**spring-security-config whose classes include:**

| Class                        | Function                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| WebSecurityConfigurerAdapter | Legacy base class for configuring web security (deprecated in Spring Security 6)      |
| HttpSecurity                 | Fluent API to configure web security: authorize rules, login, logout, CSRF, etc.      |
| AuthenticationManagerBuilder | Builds the global `AuthenticationManager` (providers, `UserDetailsService`, encoders) |

spring-security-web whose classes include:

| Class                                | Function                                                    |
| ------------------------------------ | ----------------------------------------------------------- |
| UsernamePasswordAuthenticationFilter | Processes form login (`/login`) and attempts authentication |
| LogoutFilter                         | Handles logout requests and clears security context/session |
| BasicAuthenticationFilter            | Processes HTTP Basic auth headers                           |
| RememberMeAuthenticationFilter       | Restores authentication from remember-me cookie             |
| CsrfFilter                           | Applies CSRF protection to state-changing HTTP requests     |
| SecurityContextPersistenceFilter     | Loads/saves `SecurityContext` for each request              |

### **Security Configuration Class**

Now we will configure the Security class within our code. Start with creating a _config_ folder in the root of _ordersapp_. Create a new class **SecurityConfig.java** in the _config_ folder.

![[Pasted image 20250929105522.png]]
_the error seen is from the linter in the IDE nothing is wrong with this code._

<div style="page-break-before: always;"></div>

### \*\*Password Encoding Config

Create a new class **PasswordConfig.java** in the _config_ folder. This code will use BCrypt hashing. See table for alternative hashing options.

![[Pasted image 20250929111550.png]]

**For Production:** Use BCryptPasswordEncoder, Pbkdf2PasswordEncoder, SCryptPasswordEncoder, or Argon2PasswordEncoder.

**For Testing:** Use NoOpPasswordEncoder only in non-production environments for simplicity.

![[Pasted image 20250929111649.png]]

<div style="page-break-before: always;"></div>

### **Update User Service for Password Encoding and Spring Authentication**

**Key Updates in UserService Class**

1. Implementation of UserDetailsService Interface:
   - Implements UserDetailsService and provides the loadUserByUsername method for integrating with Spring Security.

2. Password Encoding:
   - Uses PasswordEncoder to encode passwords before saving them.

3. Password Verification:
   - Has a commented-out verifyPassword method because Spring Security handles password verification.

   - Previously: Includes a verifyPassword method that compares plain text passwords.

4. Authorities and Roles:
   - In loadUserByUsername, assigns default roles (ROLE_USER, ROLE_ADMIN) to the authenticated user.

   - Previously: Did not handle roles or authorities since it does not integrate with Spring Security.

5. Security Integration:
   - Fully integrated with Spring Security, using UserDetailsService to load user details for authentication.

![[Pasted image 20250929111915.png]]
![[Pasted image 20250929111930.png]]

### **Update Login Form**

Modify the login and registration forms to handle authentication through the Spring Security filter chain instead of the UsersController.

![[Pasted image 20250929112221.png]]

**Key Updates**

1. Form Action URL:
   - Original The form action is @{/users/login}, indicating that the login form will be submitted to the /users/login endpoint which was part of the UsersController (now removed in favor of Spring Security).

   - Update: The form action is @{/login}, indicating that the login form will be submitted to the /login endpoint, which is part of the Spring Security filter chain.

2. Thymeleaf Object Binding:
   - Original: The form uses th:object="${user}" to bind the form fields to a user object. This means that the form fields will be bound to the properties of the user object.

   - Update: The form does not use object binding with th:object

3. Field Names:
   - Original: Uses th:field="_{userName}" and th:field="_{password}" to bind the form fields directly to the userName and password properties of the user object.

   - Update: Uses standard HTML name attributes (name="username" and name="password") without Thymeleaf object binding. The username and password are part of the user object in Spring Security.

4. Error Handling:
   - Original: Uses th:if="${error}" and th:text="${error}" to display an error message if there is an error attribute in the model.

   - Update: Uses th:if="${param.error}" and displays a static error message "Invalid login credentials" if the error parameter is present in the request

<div style="page-break-before: always;"></div>

### **Update the User Controller**

Ensure the controller uses the new security configurations.

![[Pasted image 20250929112429.png]]

**Key Differences**

1. Removed Login Method:
   - Original Version: Contains a @PostMapping("/login") method that handles user login by checking user existence and password correctness.

   - New Version: This method is commented out, indicating a shift to using Spring Security's built-in login functionality.

2. Logout Method Enhancement:
   - Original Version: The logout method simply redirects to the login form without any session management.

   - New Version: The logout method now takes an HttpSession parameter and invalidates the session to properly log out the user.

3. Imports:
   - New Version: Uses jakarta.servlet.http.HttpSession for session management.

   - Original Version: Does not use HttpSession for logout handling.

4. The UserController is no longer responsible for processing logins. Spring SecurityConfig relies on the UserService and implements UserDetailsService and the method loadUserByUsername method

### **Test the Application\***

Run the application and ensure that users can register, log in, and access protected resources.

1. Register a new user.
   ![[Pasted image 20250929115833.png]]
2. Log in with the new user.
   ![[Pasted image 20250929115839.png]]
3. Access protected resources (e.g., /orders, create, edit).

_logged in as Admin to edit orders_
![[Pasted image 20250929120029.png]]

_logged in as Admin to create an order_ ![[Pasted image 20250929115909.png]]
_logged in as user to view orders_
![[Pasted image 20250929120052.png]] 4. Logout

5. Attempt to access protected resources.

_while logged in with user not admin_
![[Pasted image 20250929120243.png]]

_while logged out it reroutes to login to perform action_
![[Pasted image 20250929120338.png]]

<div style="page-break-before: always;"></div>

### **Part 2 Thymeleaf Security**

What can you do with Thymeleaf and Security?

1. Authorization Tags are used to conditionally display parts of a template based on the current user's roles or authorities.

```html
<div sec:authorize="hasRole('ADMIN')">
  This content is only visible to users with the ADMIN role.
</div>
```

2. Authentication Tags are used to display information about the authenticated user.

```html
<p>Welcome, <span sec:authentication="name"></span>!</p>
```

3. Access Control Expressions support various expressions for access control checks, such as isAuthenticated(), isAnonymous(), hasRole(), hasAuthority(), etc.

```html
<li sec:authorize="isAuthenticated()">
  <a th:href="@{/logout}">Logout</a>
</li>
```

4. Conditional Rendering allows the app to display content based on the logged in user.
   - sec:isAuthenticated() renders content only if the user is authenticated.

   - sec:isAnonymous() renders content only if the user is not authenticated.

   - sec:hasRole('ROLE_USER') renders content only if the user has a specific role.

   - sec:hasAnyRole('ROLE_USER', 'ROLE_ADMIN')": renders content if the user has any of the specified roles.

5. Display User Details allow you to show properties of the authenticated user, such as username and authorities (roles).

```html
<p>User: <span sec:authentication="name"></span></p>

<p>
  Authorities:
  <span
    th:each="auth : ${#authentication.principal.authorities}"
    th:text="${auth.authority}"
  ></span>
</p>
```

**Update the Application to user Thymeleaf Security Extras**

Update pom.xml to include Thymeleaf extras for Spring Security.

![[Pasted image 20250929120936.png]]

_updated thymeleaf security dependency allows us to see if user is logged in on the nav bar_
![[Pasted image 20250929120758.png]]

\*This also allows us to see the users role and username when logged in![[Pasted image 20250929120840.png]]

<div style="page-break-before: always;"></div>

### Summary of Key Concepts

Spring Security integrates authentication (who you are) and authorization (what you can do) using components such as the AuthenticationManager, UserDetailsService, and GrantedAuthority. Passwords must be stored as secure hashes like BCrypt; encoding on save and verifying with matches on login prevents plaintext storage and replay attacks. Modern configuration relies on a SecurityFilterChain bean configured via HttpSecurity rather than the legacy WebSecurityConfigurerAdapter, enabling clear authorization rules (for example, hasRole('ADMIN')) while the security filter chain, not controllers, manages the login and logout flow. With Thymeleaf Extras for Spring Security (thymeleaf-extras-springsecurity6), the UI can react to authentication state—showing content conditionally for isAuthenticated() or hasRole(...)—and display details of the authenticated principal. For database-backed users, a working datasource is essential; authentication will fail if the application cannot reach MySQL. From a UX perspective, good patterns include redirecting anonymous users to the login page, displaying the current username and roles, and hiding administrative options from users who lack the necessary privileges.
