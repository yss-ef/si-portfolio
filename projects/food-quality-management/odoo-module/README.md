# Gestion Qualité Alimentaire - Odoo 17

Ce module Odoo permet de gérer la sécurité sanitaire, la traçabilité et le contrôle qualité des produits alimentaires au sein de l'entrepôt.

## Fonctionnalités Principales

*   **Gestion des Allergènes** : Définition des allergènes et association aux articles. Affichage dynamique sur la boutique en ligne (eCommerce).
*   **Contrôle Qualité (CQ)** : Système complet de tickets d'inspection avec suivi de la température.
*   **Sécurité à l'Expédition** : Verrouillage automatique des transferts de stock si les lots n'ont pas de certificat de conformité valide.
*   **Contrôles Périodiques Automatisés** : Génération automatique de tickets de contrôle pour les produits périssables via une action planifiée (Cron).
*   **Rapports Sanitaires** : Génération de rapports PDF de conformité pour les contrôles qualité.
*   **Température de Stockage** : Suivi des seuils de température par type de produit avec alertes en cas de dépassement.

## Architecture du Module

Le module est structuré de manière standard pour Odoo :

```text
gestion_alimentaire/
├── data/                       # Données XML (Actions planifiées, données de démonstration)
│   ├── cron_quality_control.xml # Automatisation des contrôles
│   └── demo_data.xml           # Jeu de données de test
├── models/                     # Logique métier et extensions de modèles
│   ├── food_allergen.py        # Définition des allergènes
│   ├── food_quality_control.py # Cœur du système de tickets Qualité
│   ├── product_template.py     # Extension des articles (Allergènes, T°, Périodicité)
│   ├── stock_lot.py            # Suivi des contrôles par lot de fabrication
│   └── stock_picking.py        # Verrous de sécurité lors des transferts
├── report/                     # Templates de rapports PDF (QWeb)
│   └── food_quality_report.xml
├── security/                   # Droits d'accès et groupes
│   ├── ir.model.access.csv     # Permissions par modèle
│   └── security_groups.xml     # Groupes "Inspecteur" et "Responsable"
├── views/                      # Interfaces utilisateur (XML)
│   ├── food_quality_control_views.xml
│   ├── product_template_views.xml
│   ├── stock_lot_views.xml
│   ├── stock_picking_views.xml
│   └── website_sale_templates.xml # Intégration eCommerce
└── __manifest__.py             # Métadonnées du module
```

## Utilisation

### 1. Configuration des Articles
Dans la fiche article (onglet Inventaire), cochez **"Est périssable"** pour activer les contrôles automatiques. Renseignez la **température cible** et l'**intervalle de contrôle** (en jours).

### 2. Réception et Expédition
Lors d'une réception ou d'une livraison (`stock.picking`), un bouton **"Créer Contrôle Qualité"** permet de générer des tickets pour les lots concernés. 
> **Note :** Odoo bloquera la validation du transfert si un article périssable n'a pas de contrôle marqué comme "Conforme".

### 3. Exécution du Contrôle
Les inspecteurs remplissent les tickets de contrôle en relevant la température. 
*   Si la température dépasse le seuil autorisé (+10°C par rapport à la cible), le système bloque la validation.
*   Une fois validé, le lot est considéré comme "Sûr" pour le mouvement de stock.

### 4. Automatisation
Une action planifiée ("Génération tickets contrôle qualité") tourne quotidiennement pour vérifier si des lots en stock nécessitent une nouvelle inspection basée sur l'intervalle de contrôle défini.

## Installation

1. Copiez le dossier `gestion_alimentaire` dans votre répertoire `addons`.
2. Mettez à jour la liste des modules dans Odoo (Mode développeur).
3. Installez le module "Gestion Qualité Alimentaire".

## Licence
Ce module est distribué sous licence LGPL-3.
