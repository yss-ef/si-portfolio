# Lab 4 responses: advanced views

This report describes the implementation of advanced views in Odoo 17,
including Kanban, graphical, and advanced search interfaces.

## Kanban view for students

The Kanban view provides a visual representation of student records, including
photographs and key identifiers.

- Model: Added a `photo = fields.Binary(string='Photo')` field in
  `models/etudiant.py`.
- Form view: Implemented the `image` widget for the photo field.
- Kanban view: Created the `<kanban>` view to display the photo, name, student
  number, and gender.
- Action: Updated `etudiant_action` to set `kanban` as the default view mode.

## Graphical view for courses

The graphical view enables statistical analysis of course data.

- Graphical view: Created the `<graph>` view in `views/cours_view.xml` to
  visualize credits by level.
- Action: Added the `graph` view to `cours_action`.

## Advanced search view for professors

The advanced search view facilitates efficient data retrieval for professor
records.

- Search view: Implemented filters for email and course enrollment status, along
  with grouping options for specialty and name.

## Reflection questions

### 1. What are the advantages of the Kanban view over the list view?

The Kanban view is more visual and intuitive. It allows users to identify
records quickly using images or color codes. It is ideal for moderate data
volumes and provides a modern user experience.

### 2. In which contexts should you use a graphical view?

Graphical views are used for data analysis and reporting. They allow for the
instant visualization of data distributions or totals, which assists in
informed decision-making.

### 3. How do search filters improve the user experience?

Filters allow users to find relevant information quickly by reducing visual
noise. Predefined filters eliminate the need for manual complex queries, while
grouping structures information logically.
