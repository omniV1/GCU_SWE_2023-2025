# Finish the Music Application – Integration with Back End

## Overview

In this activity, we completed the Music application by integrating the front end with back end services. This required running MAMP and our Express MusicAPI to supply live data to our Angular application.

## Execution

The execution of this assignment was carried out according to the specified guidelines. We began by creating a copy of our existing Music application, followed by several steps including the addition of the HTTP Client Module and refactoring our Music Service to utilize live data.

### Steps included:

1. **Copying the Application:** Created a directory for the updated Music application and copied all necessary files.
2. **Setting Up the Workspace:** Opened the updated application in VS Code and refreshed the Workspace.
3. **Adding HTTP Client Module:** Included the HttpClientModule in the app.module.ts imports array.
4. **Refactoring Music Service:** Updated methods to fetch live data using HttpClient and removed hard-coded data.

## Submission Deliverables

### Captioned Screenshots:

- **Main Application Screen:**
  ![Main Screen](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/main-screen.png)

- **Artist List Screen:**
  ![Artist List](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/artist-list.png)
  
- **Album List Screen:**
 ![Album List](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/album-list.png)

- **Album Display Screen:**
![Album Display](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/album-display.png)

- **Add Album Screen:**
 ![Create Album Initial](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/create-album-inital.png)
 ![Create Album POST](https://github.com/omniV1/CST-391/blob/main/docs/activity4/screenshots/create-album-POST.png)

## Research

### How an Angular Application Maintains a Logged-in State

An Angular application can maintain a logged-in state and communicate this to the server using the following mechanisms:

### Authentication
When users log in, the server **validates their credentials**. On success, it issues a token, often a **JSON Web Token (JWT)**.

### Token Storage
The token is sent to the Angular application, which then stores it securely, typically in `localStorage` or `sessionStorage`.

### Sending Token in HTTP Headers
Angular includes the token in the headers of HTTP requests, commonly as an **'Authorization' header**. An HTTP interceptor is used to append the token to all requests automatically.

```typescript
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const authToken = this.authService.getAuthToken();
    const authReq = req.clone({
      headers: req.headers.set('Authorization', `Bearer ${authToken}`)
    });
    return next.handle(authReq);
  }
}
```

### Session Management
The server validates the token with each request. A valid token allows the request to proceed; otherwise, an error is sent back.

### User State in Angular
Angular services and RxJS Observables track authentication state, which components can subscribe to.

```typescript
export class AuthService {
  private isLoggedIn = new BehaviorSubject<boolean>(false);

  // ...

  get isLoggedIn$(): Observable<boolean> {
    return this.isLoggedIn.asObservable();
  }

  // ...

  logOut() {
    localStorage.removeItem('token');
    this.isLoggedIn.next(false);
  }
}
```

### Logout
The application removes the token from storage, and the server invalidates the token if necessary.

### Security Considerations
Ensure secure token storage and transmission, such as using HTTPS for communication.

### Refresh Tokens
Implement refresh tokens to obtain new access tokens upon expiration without re-authentication.

## References

- **Angular Documentation**: For comprehensive guides on services, HTTP interceptors, and RxJS Observables in Angular.
  - [Angular Services](https://angular.io/guide/architecture-services)
  - [HTTP Interceptors](https://angular.io/guide/http#intercepting-requests-and-responses)
  - [RxJS Observables in Angular](https://angular.io/guide/observables)

- **JSON Web Tokens (JWT)**: For understanding JWTs for authentication.
  - [Introduction to JSON Web Tokens](https://jwt.io/introduction/)

- **HTTP Security Best Practices**: Guidelines for secure communication over HTTPS.
  - [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)

- **Web Storage API**: For insights into web storage options and security.
  - [Using the Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)

- **Angular Authentication with JWT**: Tutorials on implementing JWT authentication in Angular.
  - [Angular Authentication Using HttpClient and Http Interceptors](https://blog.angular-university.io/angular-jwt-authentication/)

- **RxJS Documentation**: Official RxJS documentation for a deep dive into observables.
  - [RxJS Documentation](https://rxjs.dev/guide/overview)

- **OWASP Security Considerations**: Security practices for token-based authentication.
  - [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- **Refresh Tokens**: Understanding the use of refresh tokens in applications.
  - [The Refresh Token](https://auth0.com/learn/refresh-tokens/)
