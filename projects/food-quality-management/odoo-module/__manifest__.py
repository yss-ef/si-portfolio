{
    'name': 'Gestion Qualité Alimentaire',
    'version': '17.0.1.1.0',
    'category': 'Inventory/Inventory',
    'summary': 'Contrôle qualité, allergènes et traçabilité alimentaire',
    'description': """
Module professionnel de gestion alimentaire :
- Suivi des allergènes sur les articles.
- Verrous de sécurité à l'expédition des lots.
- Automatisation des contrôles périodiques.
- Rapports PDF de conformité sanitaire.
    """,
    'author': 'Youssef',
    'depends': ['base', 'product', 'stock', 'mail', 'website_sale'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/cron_quality_control.xml',
        'data/demo_data.xml',
        'report/food_quality_report.xml',
        'views/food_quality_control_views.xml',
        'views/product_template_views.xml',
        'views/stock_lot_views.xml',
        'views/stock_picking_views.xml',
        'views/website_sale_templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
