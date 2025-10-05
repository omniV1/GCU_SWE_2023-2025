# GCU Events Management System - Spring Boot Security Demo Script
**Target Duration: 5 minutes or less**

---

## **INTRODUCTION (30 seconds)**

"Hello, I'm Owen Lindsey from Grand Canyon University, CST-407 Application Security Foundations. Today I'll demonstrate the Spring Boot Security implementation in our GCU Events Management System. This application has been transformed from a basic events system into a secure, enterprise-grade application with proper authentication, authorization, and professional GCU branding."

---

## **APPLICATION WALKTHROUGH (1 minute)**

"Let me start by showing you the application interface. As you can see, we have the official Grand Canyon University branding with our purple and gold color scheme. The navigation bar shows 'Register' and 'Login' options for unauthenticated users, while the Events page remains accessible to all visitors.

When I click on the Events page, you can see the events listing is publicly accessible. Notice that the 'Create New Event' link is not visible, and the Actions column with Edit and Delete options is also hidden. This demonstrates our public access controls.

Now let me show you the user registration process. I'll click Register and create a new user account. Notice the form validation and the secure password handling. When I submit the form, the password is automatically hashed using BCrypt encryption before being stored in the database."

---

## **SECURITY FEATURES DEMONSTRATION (2 minutes)**

"Now let's examine the core security features. I'll log in with the account I just created. Notice how the navigation dynamically changes after authentication. The Register and Login links disappear, and instead we see a welcome message with my username and a Logout option.

More importantly, the Create New Event link now appears, and if I go back to the Events page, the Actions column with Edit and Delete options is now visible. This demonstrates our conditional rendering based on authentication status.

Let me create a new event to show the protected functionality. I'll fill out the event form and submit it. Notice that this operation is only available to authenticated users.

Now let me demonstrate the logout functionality. When I click Logout, my session is properly cleared, and I'm redirected back to the login page. Notice how the navigation reverts to showing Register and Login options, and all protected functionality becomes hidden again.

Let me also show you what happens when an unauthenticated user tries to access protected URLs directly. If I try to access the create event page while logged out, Spring Security automatically redirects me to the login page."

---

## **KEY CODE CHANGES (2 minutes)**

"Now let me highlight the key code changes that made this security implementation possible.

First, let's look at the SecurityConfig.java file. This configuration class defines our security rules and authentication mechanisms. It implements HTTP security with URL-based authorization, custom login and logout URLs with appropriate redirects, BCrypt password encoding, method-level security, and proper exception handling.

Next, we have the CustomUserDetailsService.java file. This service bridges the gap between our existing user repository and Spring Security's authentication system. It converts our UserEntity objects to Spring Security UserDetails and implements role-based authority mapping.

In the UserService.java file, we modified the password encoding process to use BCrypt instead of plain text storage. This ensures password security follows industry standards.

The EventController.java file received @PreAuthorize annotations on all sensitive methods. This ensures only authenticated users can access event creation, modification, and deletion functionality.

Finally, our Thymeleaf templates use Spring Security integration. The layout.html template implements conditional navigation rendering using sec:authorize attributes. The events.html template conditionally displays protected functionality based on user authentication status.

The login.html template was updated to work seamlessly with Spring Security, using the proper form action and input names as required by the framework."

---

## **TECHNICAL IMPLEMENTATION SUMMARY (30 seconds)**

"Our implementation leverages Spring Boot 3.x with Spring Security 6.x, providing enterprise-grade security features including BCrypt password hashing, method-level security annotations, CSRF protection, and proper session management. The application follows security best practices with clear separation of public and authenticated functionality, automatic session invalidation on logout, and comprehensive error handling.

The complete transformation involved modifications to eight existing files and creation of two new security configuration files, resulting in five major security components being added to the application."

---

## **CONCLUSION (30 seconds)**

"This implementation demonstrates comprehensive understanding of Spring Boot Security framework, modern web development practices, and professional UI/UX design principles. The GCU Events Management System now represents a complete transformation from a basic events application to an enterprise-grade, secure system with professional GCU branding and intuitive user experience.

The security implementation follows industry best practices and ensures the application meets modern application security foundations requirements. Thank you for watching this demonstration of our Spring Boot Security implementation."

---

## **PRESENTATION TIPS:**

1. **Speak clearly and at a moderate pace** - aim for about 150 words per minute
2. **Use the application live** - demonstrate features as you describe them
3. **Highlight code sections** - point to specific files and methods
4. **Emphasize security aspects** - mention BCrypt, authentication, authorization
5. **Keep transitions smooth** - use phrases like "Now let me show you..." and "Notice how..."
6. **End with confidence** - summarize the key achievements

**Total estimated duration: 5 minutes**
