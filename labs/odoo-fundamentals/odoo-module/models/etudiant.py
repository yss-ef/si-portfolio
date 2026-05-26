from odoo import models, fields

class Etudiant(models.Model):
    _name = 'gestion.etudiant'
    _description = 'Modèle étudiant'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
    photo = fields.Binary(string='Photo')
    
    # === EXERCICE 1 ===
    # Ajoutez un champ "Num_étudiant" de type Char, obligatoire et unique.
    num_etudiant = fields.Char(string='Numéro étudiant', required=True, copy=False)
    
    # === EXERCICE 3 ===
    # Ajoutez un champ "Sexe" de type Sélection (Masculin, Féminin, Autre) avec valeur par défaut.
    sexe = fields.Selection([
        ('m', 'Masculin'),
        ('f', 'Féminin'),
        ('o', 'Autre')
    ], string='Sexe', default='m')

    # === TP2: Relation avec les cours ===
    cours_ids = fields.Many2many('gestion.cours', string='Cours suivis')

    _sql_constraints = [
        # Partie de l'EXERCICE 1: Assurer l'unicité du numéro étudiant
        ('num_etudiant_unique', 'unique(num_etudiant)', 'Le numéro étudiant doit être unique !')
    ]
