# Systems information portfolio

This repository centralizes academic and personal work related to Enterprise
Resource Planning (ERP) systems. It focuses on the Odoo 17 framework and
containerized deployments.

## Projects

### Food quality and safety management

This project involves a custom Odoo 17 module designed to manage food safety
requirements, including perishability, storage temperatures, and allergen
tracking.

Key implementations include:
- Automated quality control tickets via Cron jobs.
- Logistics security locks to prevent shipping non-compliant lots.
- Allergen management integrated with eCommerce.
- ORM extensions for stock lots and product templates.

[View project details](./projects/food-quality-management/)

## Labs

### Odoo fundamentals

This section contains exercises focused on the core architecture of Odoo 17,
covering the ORM, views, and security.

Topics include:
- Model definitions and field types (Many2one, One2many, Many2many).
- View inheritance and advanced UI (Kanban, Graph, Search).
- Access rules and security group configuration.
- Data integrity via SQL and Python constraints.

[View lab details](./labs/odoo-fundamentals/)

## Technologies used

- ERP Platform: Odoo 17.0
- Backend: Python, PostgreSQL
- Frontend: XML (Odoo Views), QWeb (Reporting)
- Infrastructure: Docker, Docker Compose
- Methodology: BPMN 2.0, UML

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.

Authored by Youssef Fellah.
Developed for the Engineering Cycle at Mundiapolis University.
