# Lab 5 responses: security and access management

This report describes the implementation of security groups and access rights
within the Odoo 17 student management module.

## Security group creation

### Groups and hierarchy

We defined two primary security groups in `security/security.xml` under the
"Education / Student Management" category:

- Teacher (`group_enseignant`): The base group for instructors.
- Education Admin (`group_admin_education`): An administrative group that
  inherits permissions from the Teacher group using `implied_ids`.

```xml
<record id="group_admin_education" model="res.groups">
    <field name="name">Education Admin</field>
    <field name="implied_ids" eval="[(4, ref('group_enseignant'))]"/>
</record>
```

## Access rights configuration

The `security/ir.model.access.csv` file defines specific access levels for the
Professor model:

- Teachers: Granted read and write permissions (`perm_read=1`, `perm_write=1`)
  but restricted from creating or deleting records (`perm_create=0`,
  `perm_unlink=0`).
- Education Admins: Granted full CRUD (Create, Read, Update, Delete) access.
- All users (`base.group_user`): Retain full access to the Student and Course
  models to facilitate testing.

The `security/security.xml` file is loaded in the `__manifest__.py` file before
 the CSV file to ensure groups exist before access rights are applied.

## Permission testing results

| User | Group | Professor Access | Student/Course Access |
| :--- | :--- | :--- | :--- |
| **Test Teacher** | Teacher | Read and Edit. Create and Delete buttons are hidden. | Full Access. |
| **Test Admin** | Education Admin | Full Access. Create and Delete buttons are visible. | Full Access. |

### Observed interface differences

1. Action buttons: The Odoo interface adapts dynamically. For Teachers, the
   "Create" button is removed from the list and form views for professors.
2. Action menu: The "Delete" option is unavailable for users with only Teacher
   permissions on the Professor model.
3. Inheritance: Test Admins possess all Teacher permissions plus creation and
   deletion rights, confirming that `implied_ids` functions correctly.

## Reflection questions

### 1. What is the utility of group categories?

Categories organize groups within the user management interface (Settings >
Users). This allows for grouping rights by role or module, which improves
configuration readability.

### 2. Why is the file order in the manifest important?

Odoo processes files in the order listed in the `data` key. If a CSV file
references a group defined in an XML file, that XML file must load first to
avoid identifier errors.
