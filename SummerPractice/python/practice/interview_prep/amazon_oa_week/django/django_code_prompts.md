# Django Code Prompts (Practice in 20-30 min blocks)

## Prompt 1: Optimize N+1 query
You have:
- `Order` model FK to `User`
- `OrderItem` reverse FK from `Order`
Task:
- Return latest 50 orders with user name and item count in one endpoint.
- Avoid N+1.

## Prompt 2: Build filtered movie endpoint
Input query params:
- `year`, `min_year`, `max_year`, `director`, `writer`
Output:
- filtered queryset, case-insensitive contains for names
- sorted by `rating desc`, then `popularity desc`
- return JSON list

## Prompt 3: Add robust pagination + validation
Task:
- `page` and `page_size` with caps
- reject invalid params cleanly
- return deterministic ordering

## Prompt 4: Auth + permissions
Task:
- Authenticated users can create
- Only owner can update/delete
- Everyone can read

## Prompt 5: Caching
Task:
- Cache list endpoint 60s
- Invalidate cache on create/update/delete
