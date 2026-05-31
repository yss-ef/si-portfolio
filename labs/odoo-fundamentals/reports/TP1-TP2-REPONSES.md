# Odoo 17 development responses

This document provides responses to development questions regarding the
`gestion_etudiants_manuel` module.

## Odoo 17 installation and configuration

### 1. What is the role of the odoo.conf file?

The `odoo.conf` file is the primary configuration file for the Odoo server. It
defines operational parameters, such as database connection details (host, port,
user, password), the default listening port (8069), and paths to various
modules.

### 2. What is the purpose of the addons_path key?

The `addons_path` key specifies the directories where Odoo searches for modules
to load. Correct configuration is essential to include both official Odoo
modules and custom project folders. Incorrect settings prevent modules from
appearing in the interface.

### 3. Why are custom modules separated into a specific folder?

Separating custom modules (for example, in `/mnt/extra-addons` for Docker) is
recommended for several reasons:

- Maintenance: It keeps custom code separate from the Odoo source, facilitating
  core updates.
- Deployment: It simplifies Docker volume management and code transfers between
  environments.
- Clarity: It allows for quick identification of project-specific developments.

## Developer mode and debugging tools

### 4. How do you activate developer mode?

You can activate developer mode using two methods:
1. Through the interface: Navigate to Settings and select "Activate the
   developer mode" at the bottom of the page.
2. Through the URL: Append `?debug=1` to the URL (for example,
   `http://localhost:8069/web?debug=1`).

### 5. Which tools become available in developer mode?

- Technical view: Provides access to record metadata, such as IDs and creation
  dates.
- View manager: Allows for direct editing of XML views within the browser.
- Model inspection: Provides technical details on tables and fields.
- Technical menu: Adds a comprehensive menu in Settings for managing sequences,
  emails, and servers.

### 6. What is the purpose of the model inspection tool?

The model inspection tool displays the technical structure of a model,
including its fields, types, relationships, constraints, and associated access
rules.

## Odoo module structure

### 7. Describe the standard structure of an Odoo module.

- `models/`: Contains Python files defining database tables.
- `views/`: Contains XML files defining the user interface (forms, lists,
  menus).
- `security/`: Contains access rules (`ir.model.access.csv`) and groups.
- `data/`: Contains base XML data for configuration or demonstration.
- `__init__.py`: Initializes the module and Python packages.
- `__manifest__.py`: Contains module metadata.

### 8. What is the purpose of the static folder?

The `static/` folder contains immutable resources, such as CSS files, images,
JavaScript files, and XML files for the frontend (QWeb).

### 9. What is the role of the demo folder?

The `demo/` folder contains XML or CSV files that load only when you select the
"Demo data" option during database creation. It provides examples to test
module functionality.

## Module creation with scaffold

### 10. Which command generates a module structure?

Use the command: `odoo-bin scaffold gestion_etudiants ./addons`

### 11. Which customizations are necessary after scaffolding?

Necessary customizations typically include:
- Updating the `__manifest__.py` file (name, description, author, dependencies).
- Defining models in the `models/` directory.
- Removing unnecessary example files.

## Base components: manifest and init

### 12. What is the __manifest__.py file?

The `__manifest__.py` file serves as the module declaration. Odoo uses it to
manage installation, load dependencies, and identify XML files for processing.

### 13. Explain the keys in the __manifest__.py file.

- `name`: The display name of the module.
- `depends`: A list of required modules (for example, `['base']`).
- `data`: A list of XML or CSV files to load into the database.
- `installable`: Indicates if the module can be installed.
- `application`: If set to True, the module appears in the main applications
  list.

### 14. What happens if installable is set to False?

The module appears in the module list, but the "Install" button is disabled or
hidden.

### 15. What is the role of the __init__.py file?

The `__init__.py` file is a standard Python file that treats the directory as a
package. In Odoo, it imports sub-folders, such as `models`, so the server can
process the contained Python code.

## Model creation and field types

### 16. What is a model in Odoo?

A model is a Python class that inherits from `models.Model`. It defines a table
in the PostgreSQL database where each attribute represents a column.

### 17. What is the purpose of the _name and _description keys?

- `_name`: The unique technical identifier for the model (for example,
  `gestion.etudiant`).
- `_description`: A human-readable name describing the model.

### 18. List five available field types.

1. `Char`: Short character string.
2. `Integer`: Integer number.
3. `Float`: Decimal number.
4. `Date`: Date without a time component.
5. `Selection`: Dropdown list with predefined options.

### 19. Explain the required, default, and index attributes.

- `required=True`: The field must be filled to save the record.
- `default=...`: Automatically assigns a value to the field during record
  creation.
- `index=True`: Instructs PostgreSQL to create an index for faster searches.

### 20. Explain the differences between Many2one, One2many, and Many2many.

- Many2one: Links to a single record in another model (for example, a course
  linked to one professor).
- One2many: The inverse relation where one record links to many (for example, a
  professor viewing all their courses).
- Many2many: Links multiple records to multiple records (for example, students
  enrolled in multiple courses).

## Views and user interfaces

### 21. What is a view and where is it defined?

A view defines the visual representation of data. It is defined in XML files
within the `views/` directory.

### 22. Explain the differences between form, tree, and kanban views.

- Form: A detailed view of a single record for editing.
- Tree (List): A table displaying multiple records.
- Kanban: A card-based display ideal for tracking process stages.

### 23. What is the purpose of the notebook element?

The `<notebook>` element creates tabs within a form to organize information
efficiently.

### 24. How does a search view function?

A search view filters and groups data in the list view. It can include specific
fields for searching, predefined filters, and grouping options.

## Access rules

### 25. Where are access rules defined?

Access rules are defined in the `security/ir.model.access.csv` file.

### 26. Explain the perm_read and perm_write columns.

- `perm_read`: Grants permission to read data.
- `perm_write`: Grants permission to modify data.
- `perm_create`: Grants permission to create records.
- `perm_unlink`: Grants permission to delete records.

### 27. How are groups linked to access rules?

The CSV file specifies a group ID (for example, `base.group_user`). Only users
belonging to that group receive the permissions defined for that model.
