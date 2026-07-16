# Django Rapid-Fire (Python Django OA/Interview)

## High-yield questions to answer out loud
1. Difference between `select_related()` and `prefetch_related()`?
2. `filter()` vs `get()` behavior and exceptions?
3. `annotate()` vs `aggregate()`?
4. What is N+1 and how do you detect/fix it?
5. DRF `APIView` vs `ViewSet`?
6. Where should validation live: serializer, model, or view?
7. Difference between authentication and authorization in DRF?
8. How does Django request -> middleware -> view -> response flow work?
9. How would you paginate large API results safely?
10. How would you cache expensive list endpoints?

## Must-know concise answers
- `select_related`: SQL JOIN for FK/OneToOne.
- `prefetch_related`: separate query + Python join for M2M/reverse FK.
- N+1: 1 query for list + N queries for related objects; fix with related loading.
- `annotate`: per-row computed field; `aggregate`: single summary result.
