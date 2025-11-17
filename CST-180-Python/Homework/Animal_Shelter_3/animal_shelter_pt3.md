# Animal Shelter Simulator – Project 3 Design Document

**Owen Lindsey**  
**Professor David Parker**  
**CST-180: Python Programming 1**  
**Grand Canyon University**  
**November 16, 2025**

---
***[Video Link]()

***[src code]() 

## Summary Statement

This final exercise completes the animal shelter simulator by introducing a full **Shelter** object that manages kennel capacity, animal intake, adoptions, and a waitlist for unavailable animal types. The shelter now controls how many kennels can exist, automatically reuses empty kennels, and prevents over-capacity situations. Adoption requests can free kennels, and unsuccessful requests are recorded on the waitlist so the shelter can follow up when new animals arrive. The updated design demonstrates inheritance, composition, capacity management, and basic workflow tracking in one cohesive system.

---

## Input / Processing / Output Overview

| Stage      | Description |
| ---------- | ----------- |
| **Input**  | Animal details (`name`, `age`, type-specific attribute); shelter capacity; adopter requests specifying an animal type and optional adopter name for the waitlist. |
| **Processing** | Constructors validate data, shelters locate empty kennels, and adoption paths either free kennels or log waitlist entries. Business rules enforce one animal per kennel, automatic kennel creation up to the set capacity, and waitlist tracking for unavailable types. |
| **Output** | String renderings of animals, kennels, and shelter status; Boolean success/failure for intake; adopted animal objects (or `None` when unavailable); waitlist snapshots for each animal type. |

---

## UML Object Model

![[Pasted image 20251117100415.png]]

**Relationships**
- `Dog`, `Cat`, and `Bird` inherit from the base `Animal` class.
- `Kennel` composes exactly one `Animal` (or `None`).
- `Shelter` composes multiple `Kennel` instances (bounded by `capacity`) and maintains a waitlist dictionary keyed by animal type.

---

## Design Pseudocode / Flow

### Shelter.add_animal(animal)
1. FOR each kennel IN kennels:
    - IF kennel is empty, place animal there and RETURN True.
2. IF len(kennels) < capacity:
    - CREATE new kennel with the animal, append to list, RETURN True.
3. RETURN False (shelter is full and no empty kennel exists).

### Shelter.adopt_animal(animal_type, adopter_name=None)
1. NORMALIZE requested type to lowercase for comparisons.
2. FOR each kennel IN kennels:
    - IF kennel holds that type, store the animal, set kennel empty, RETURN the animal.
3. IF adopter_name provided:
    - APPEND adopter_name to waitlist[animal_type].
4. RETURN None (no animal of that type is currently available).

### Shelter.get_waitlist(animal_type)
1. NORMALIZE type.
2. RETURN a copy of waitlist entry (empty list if not present).

---

## Sample Data

| Animal | Type | Name    | Age | Attribute    | Value       |
| ------ | ---- | ------- | --- | ------------ | ----------- |
| dog1   | Dog  | Buddy   | 3   | Breed        | Labrador    |
| cat1   | Cat  | Mittens | 2   | Fur Color    | Tabby       |
| bird1  | Bird | Sky     | 1   | Wingspan (m) | 0.35        |
| adop1  | Request | Rabbit | -- | Adopter Name | Alice       |

Shelter capacity used for the scenario: **3 kennels**.

---

## Sample Output Walkthrough

```
Shelter(capacity=3, kennels=2, animals=2, Kennel Animal: Dog: Name: Buddy, Age: 3, Breed: Labrador, Kennel Animal: Cat: Name: Mittens, Age: 2, Fur Color: Tabby)
Adopted: Cat: Name: Mittens, Age: 2, Fur Color: Tabby
Empty kennel available? True
Shelter(capacity=3, kennels=2, animals=2, Kennel Animal: Dog: Name: Buddy, Age: 3, Breed: Labrador, Kennel Animal: Bird: Name: Sky, Age: 1, Wingspan: 0.35)
Rabbit adoption result: None
Rabbit waitlist: ['Alice']
```

This output shows:
1. Initial shelter status with a dog and cat occupying two kennels.
2. Successful cat adoption freeing a kennel.
3. Bird intake reusing the empty kennel.
4. A failed rabbit adoption request that records "Alice" on the rabbit waitlist.

---

## Test Strategy Snapshot

- **Unit tests** validate constructors, formatting, and behavior of every animal class plus the Kennel.
- New **Shelter tests** cover:
  1. Constructor validation (capacity must be > 0).
  2. Automatic reuse of empty kennels before creating new ones.
  3. Capacity enforcement when intake exceeds the limit.
  4. Adoption workflow removing animals and freeing kennels.
  5. Waitlist tracking for unavailable animal types, ensuring the returned list cannot mutate internal data.

The suite now totals **33 tests** and can be run with `python -m unittest test_animal_shelter.py -v`.
