# Single Responsibility Principle (SRP)

> **A class should have only one reason to change.**

The **S** in SOLID. Each class/module should own exactly **one responsibility** — one axis of change.

---

## Why It Matters

- **Maintainability** — changes stay localized; one concern, one place to edit.
- **Testability** — small, focused classes are easier to unit test.
- **Readability** — intent is obvious from the class name.
- **Low coupling** — unrelated concerns don't drag each other along.

---

## How to Spot a Violation

- Class name contains **"and"** or **"Manager"/"Helper"/"Utils"**.
- Methods touch unrelated concerns (e.g., business logic + persistence + logging + email).
- Changing one feature forces edits across multiple unrelated methods.
- Unit tests need to mock many unrelated dependencies.

---

## Example

### Bad — one class, many responsibilities

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):          # business logic
        return self.salary * 0.8

    def save_to_db(self):             # persistence
        db.save(self)

    def generate_report(self):        # reporting
        return f"Report for {self.name}"
```

Three reasons to change: pay rules, DB schema, report format.

### Good — one responsibility per class

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class PayCalculator:
    def calculate(self, employee: Employee) -> float:
        return employee.salary * 0.8


class EmployeeRepository:
    def save(self, employee: Employee) -> None:
        db.save(employee)


class EmployeeReport:
    def generate(self, employee: Employee) -> str:
        return f"Report for {employee.name}"
```

Each class has **one reason to change**.

---

## Rule of Thumb

> If you can describe a class using **"and"**, it probably violates SRP.

- `UserAuthenticator` — ok
- `UserAuthenticatorAndEmailSender` — split it.
