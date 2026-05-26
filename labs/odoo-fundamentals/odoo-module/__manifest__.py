# -*- coding: utf-8 -*-
{
    'name': 'Gestion des étudiants',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Module de gestion des étudiants',
    'author': 'Youssef',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'license': 'LGPL-3',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/etudiant_view.xml',
        'views/professeur_view.xml',
        'views/cours_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}