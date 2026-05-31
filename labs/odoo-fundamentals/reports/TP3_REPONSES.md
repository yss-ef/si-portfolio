# Lab 3 responses: constraints and validations

This report details the implementation of SQL constraints and Python
validations within the Odoo 17 student management module.

## SQL constraints

SQL constraints ensure data integrity at the PostgreSQL database level.

### Course code uniqueness

In `models/cours.py`:
```python
_sql_constraints = [
    ('code_unique', 'unique(code)', 'The course code must be unique.'),
    ...
]
```

### Positive credits

In `models/cours.py`:
```python
_sql_constraints = [
    ...
    ('credits_positif', 'CHECK(credits >= 0)', 'The number of credits must be positive.')
]
```

### Professor email uniqueness and format

In `models/professeur.py`:
```python
_sql_constraints = [
    ('email_unique', 'unique(email)', 'The professor email must be unique.'),
    ('email_format', "CHECK(email LIKE '%@%.%')", 'The email format is incorrect.')
]
```

## Python validations

### Student enrollment limit

The `@api.constrains` decorator in `models/cours.py` limits each course to a
maximum of three students.

```python
@api.constrains('etudiant_ids')
def _check_max_etudiants(self):
    for record in self:
        if len(record.etudiant_ids) > 3:
            raise ValidationError("A course cannot have more than 3 students.")
```

## Reflection questions

### 1. What is the difference between a SQL constraint and a Python validation?

- SQL constraint: Defined at the database level (PostgreSQL). It is fast and
  ensures integrity even if data is modified outside of Odoo. It is limited to
  simple checks within the same table.
- Python validation (@api.constrains): Executed by the Odoo server. It offers
  flexibility for complex checks, such as counting related records or comparing
  data across different models. It only applies when data passes through the
  Odoo ORM.

### 2. When should you use one over the other?

- Use SQL constraints for uniqueness, simple format checks, or value ranges to
  ensure performance and robustness.
- Use Python validations for logic involving relationships between models or
  complex business calculations.

### 3. What happens when creating a course with an existing code?

The Odoo server intercepts the PostgreSQL error and displays an alert message
to the user: "The course code must be unique." The transaction is rolled back,
and the record is not saved.
