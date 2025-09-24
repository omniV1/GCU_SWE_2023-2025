# Express Routing

## Basic Concepts
- Routing determines how an application's endpoints respond to client requests
- Defined using methods of the Express app object (e.g., `app.get()`, `app.post()`)
- Can use `app.all()` for all HTTP methods and `app.use()` for middleware

## Route Methods
- Correspond to HTTP methods (GET, POST, etc.)
- Special method `app.all()` for handling all HTTP methods

## Route Paths
- Can be strings, string patterns, or regular expressions
- Special characters: `?`, `+`, `*`, `()`, `-`, `.`
- Query strings are not part of the route path

## Route Parameters
- Named URL segments that capture values
- Accessed via `req.params` object
- Can include regular expressions for more control

## Route Handlers
- Can be a single function, multiple functions, or arrays of functions
- Use `next()` to pass control to the next handler

## Response Methods
- Various methods available on the `res` object (e.g., `res.send()`, `res.json()`, `res.redirect()`)

## Chaining Route Handlers
- Use `app.route()` to create chainable route handlers for a single path

## Express Router
- Creates modular, mountable route handlers
- Treated as a "mini-app"
- Can have its own middleware and routes
- Mounted in the main app using `app.use()`
