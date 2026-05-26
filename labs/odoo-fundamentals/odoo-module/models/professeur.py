from odoo import models, fields

class Professeur(models.Model):
    _name = 'gestion.professeur'
    _description = 'Modèle Professeur'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    email = fields.Char(string='Email')
    specialite = fields.Char(string='Spécialité')
    
    # Relation inverse vers le modèle cours
    cours_ids = fields.One2many('gestion.cours', 'professeur_id', string='Cours enseignés')

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'L\'email du professeur doit être unique!'),
        ('email_format', "CHECK(email LIKE '%@%.%')", 'Le format de l\'email du professeur semble incorrect.')
    ]
