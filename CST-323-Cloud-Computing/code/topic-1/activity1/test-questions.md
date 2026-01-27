# Topic 1 Activity 1 - Multiple Choice Test

## Spring Boot Order Management Application

---

### Question 1
What annotation is used on the `OrdersDataService` class to mark it as a Spring-managed service component?

A) `@Component`
B) `@Repository`
C) `@Service` = C
D) `@Controller`

---

### Question 2
In the `OrderEntity` class, which annotation maps the Java field `quantity` to the database column `QTY`?

A) `@Id`
B) `@Table`
C) `@Column("QTY")` = C
D) `@Field("QTY")`

---

### Question 3
What does the `Mapper.toEntity()` method do?

A) Converts an `OrderEntity` to an `OrderModel` 
B) Converts an `OrderModel` to an `OrderEntity`= B
C) Saves an entity to the database
D) Deletes an entity from the database

---

### Question 4
In the `OrdersDataService.getById()` method, what is returned if the order is not found in the repository?

A) An empty `OrderModel` object
B) An exception is thrown
C) `null` = C
D) `Optional.empty()`

---

### Question 5
Which Spring Data interface does `OrdersRepository` extend?

A) `JpaRepository`
B) `CrudRepository` = B 
C) `MongoRepository`
D) `PagingAndSortingRepository`

---

### Question 6
What is the purpose of the `@Autowired` annotation on the `ordersRepository` field in `OrdersDataService`?

A) To create a new instance of the repository 
B) To enable dependency injection by Spring = B 
C) To validate the repository configuration
D) To mark the field as read-only

---

### Question 7
Which database table does the `OrderEntity` class map to?

A) `orders`
B) `ORDER_ENTITY`
C) `ORDERS` = C
D) `order_table`

---

### Question 8
What does the `OrdersDataService.getAll()` method return?

A) A single `OrderModel`
B) An `ArrayList<OrderEntity>`
C) An `Iterable<OrderModel>`
D) A `List<OrderEntity>`

---

### Question 9
In the `OrderEntity` class, which annotation marks the `id` field as the primary key?

A) `@PrimaryKey`
B) `@Key`
C) `@Id`
D) `@Column`

---

### Question 10
What design pattern does the `DataAccessInterface<T>` represent?

A) Singleton Pattern
B) Factory Pattern
C) Repository/Data Access Object Pattern
D) Observer Pattern

---

### Question 11
What type of dependency injection is used in the `OrdersDataService` constructor?

A) Field injection
B) Setter injection
C) Constructor injection
D) Interface injection

---

### Question 12
Which method in `OrdersDataService` would you call to add a new order to the database?

A) `getById()`
B) `update()`
C) `create()`
D) `getAll()`

---

### Question 13
What does the `ordersRepository.save()` method return in the `create()` and `update()` methods?

A) `void`
B) `boolean`
C) The saved `OrderEntity`
D) The ID of the saved entity

---

### Question 14
What is the return type of the `deleteById()` method in `OrdersDataService`?

A) `void`
B) `boolean`
C) `OrderModel`
D) `int`

---

### Question 15
Why does the application use both `OrderModel` and `OrderEntity` classes?

A) To improve performance
B) To separate the presentation layer from the data layer
C) Because Spring requires both
D) To reduce code duplication

---

## Answer Key

1. C
2. C
3. B
4. C
5. B
6. B
7. C
8. C
9. C
10. C
11. C
12. C
13. C
14. B
15. B

---

## Scoring Guide
- 15 correct: Excellent understanding
- 12-14 correct: Good understanding
- 9-11 correct: Satisfactory understanding
- Below 9: Review the material
