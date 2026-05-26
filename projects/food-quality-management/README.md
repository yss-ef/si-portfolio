# Food Quality and Safety Management System

This project is a custom Odoo 17 module developed to address the specific needs of the food industry within an ERP environment.

## Overview
Standard ERP systems often treat all inventory items identically. This project bridges the gap between generic logistics and the strict requirements of food safety (perishability, chain of cold, allergens).

## Features
*   Sanitary Control Cycle: Integrated quality checks at the point of reception.
*   Automated Periodic Inspections: Daily scheduler (Cron) that generates inspection tickets based on product-specific intervals.
*   Logistics Security Locks: Prevents shipping of non-compliant or expired lots by overriding validation methods.
*   Allergen Management: Normalized repository for allergens integrated with the eCommerce storefront.
*   Reporting: Custom QWeb PDF templates for Sanitary Certificates.

## Project Structure
*   `odoo-module/`: The `gestion_alimentaire` Odoo 17 addon.
*   `deployment/`: Docker Compose and Odoo configuration files for containerized setup.

## Implementation Details
The module extends several standard Odoo models:
*   `product.template`: Adds fields for perishability, storage temperature, and control intervals.
*   `stock.lot`: Adds tracking for the last control date.
*   `stock.picking`: Implements validation overrides to enforce quality compliance.
