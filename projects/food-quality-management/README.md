# Food quality and safety management system

This repository contains a custom Odoo 17 module designed to address food
industry requirements within an ERP environment.

Standard ERP systems often treat inventory items identically. This project
addresses the gap between generic logistics and the strict requirements of food
safety, including perishability, cold chain maintenance, and allergen tracking.

## Features

- Sanitary control cycle: Implements quality checks during product reception.
- Automated periodic inspections: Uses a scheduled Cron job to generate
  inspection tickets based on product intervals.
- Logistics security locks: Prevents the shipment of non-compliant or expired
  lots by overriding standard validation methods.
- Allergen management: Provides a normalized repository for allergens
  integrated with the eCommerce storefront.
- Reporting: Includes custom QWeb PDF templates for sanitary certificates.

## Project structure

- `odoo-module/`: The `gestion_alimentaire` Odoo 17 addon.
- `deployment/`: Docker Compose and Odoo configuration files for containerized
  deployment.

## Implementation details

The module extends several standard Odoo models:

- `product.template`: Adds fields for perishability, storage temperature, and
  control intervals.
- `stock.lot`: Adds tracking for the most recent control date.
- `stock.picking`: Implements validation overrides to enforce quality
  compliance.
