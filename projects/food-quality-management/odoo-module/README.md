# Food quality management for Odoo 17

The `gestion_alimentaire` module manages sanitary safety, traceability, and
quality control for food products within an Odoo-managed warehouse.

## Core features

- Allergen management: Define allergens and associate them with products.
  Features dynamic display on the eCommerce storefront.
- Quality control (QC): Provides a comprehensive inspection ticket system with
  temperature tracking.
- Shipping security: Automatically locks stock transfers if lots lack a valid
  conformity certificate.
- Automated periodic checks: Generates quality control tickets for perishable
  products using a scheduled Cron action.
- Sanitary reports: Generates PDF conformity reports for quality controls.
- Storage temperature: Tracks temperature thresholds by product type and
  provides alerts for deviations.

## Module architecture

The module follows the standard Odoo directory structure:

```text
gestion_alimentaire/
├── data/                       # XML data (Cron and demo data)
├── models/                     # Business logic and model extensions
├── report/                     # QWeb PDF report templates
├── security/                   # Access rights and security groups
├── views/                      # XML user interfaces
└── __manifest__.py             # Module metadata
```

## Usage

### 1. Product configuration

On the Inventory tab of the product form, select "Is Perishable" to enable
automatic controls. Specify the target temperature and control interval in
days.

### 2. Reception and shipping

During stock reception or delivery (`stock.picking`), use the "Create Quality
Control" button to generate tickets for relevant lots. Odoo prevents transfer
validation if a perishable item lacks a "Compliant" control status.

### 3. Control execution

Inspectors complete control tickets by recording the observed temperature. The
system blocks validation if the temperature exceeds the authorized threshold.
Once validated, the lot is marked as safe for movement.

### 4. Automation

A scheduled action runs daily to identify lots requiring re-inspection based on
their defined control intervals.

## Installation

1. Copy the `gestion_alimentaire` directory into your `addons` folder.
2. Update the module list in Odoo while in developer mode.
3. Install the "Food Quality Management" module.

## License

This module is distributed under the LGPL-3 license.
