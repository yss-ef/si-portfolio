# Systems Information (SI) Portfolio

This repository centralizes my academic and personal work related to Enterprise Resource Planning (ERP) systems, focusing on the Odoo 17 framework and containerized deployments.

## Projects

### Food Quality and Safety Management
A custom Odoo 17 module designed to manage food safety requirements such as perishability, storage temperatures, and allergen tracking.

Key implementations:
*   Automated periodic quality control tickets via Cron jobs.
*   Logistics security locks to prevent shipping non-compliant lots.
*   Many-to-Many allergen management integrated with eCommerce.
*   ORM extensions for stock lot and product templates.

[View Project Details](./projects/food-quality-management/)

## Labs

### Odoo Fundamentals
This section contains exercises focused on the core architecture of Odoo 17, including ORM, Views, and Security.

Topics covered:
*   Model definitions and field types (Many2one, One2many, Many2many).
*   View inheritance and advanced UI (Kanban, Graph, Search).
*   Access rules and security groups configuration.
*   Data integrity via SQL and Python constraints.

[View Lab Details](./labs/odoo-fundamentals/)

## Technologies Used
*   ERP Platform: Odoo 17.0
*   Backend: Python, PostgreSQL
*   Frontend: XML (Odoo Views), QWeb (Reporting)
*   Infrastructure: Docker, Docker Compose
*   Methodology: BPMN 2.0, UML

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---
Authored by Youssef Fellah.  
Developed for the Engineering Cycle - Mundiapolis University.
