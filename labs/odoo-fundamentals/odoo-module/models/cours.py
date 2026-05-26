from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Cours(models.Model):
    _name = 'gestion.cours'
    _description = 'Modèle Cours'

    name = fields.Char(string='Nom du cours', required=True)
    description = fields.Text(string='Description')
    
    # Relation Many2many car un étudiant peut suivre plusieurs cours 
    # et un cours peut être suivi par plusieurs étudiants
    etudiant_ids = fields.Many2many('gestion.etudiant', string='Étudiants')
    
    code = fields.Char(string='Code du cours', required=True)
    credits = fields.Integer(string='Crédits')
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    
    professeur_id = fields.Many2one('gestion.professeur', string='Professeur')
    
    niveau = fields.Selection([
        ('debutant', 'Débutant'),
        ('intermediaire', 'Intermédiaire'),
        ('avance', 'Avancé')
    ], string='Niveau', default='debutant')
    
    actif = fields.Boolean(string='Actif', default=True)
    
    duree_totale = fields.Integer(string='Durée totale (jours)', compute='_compute_duree_totale', store=True)

    @api.depends('date_debut', 'date_fin')
    def _compute_duree_totale(self):
        for record in self:
            if record.date_debut and record.date_fin:
                delta = record.date_fin - record.date_debut
                record.duree_totale = delta.days
            else:
                record.duree_totale = 0

    @api.constrains('etudiant_ids')
    def _check_max_etudiants(self):
        for record in self:
            if len(record.etudiant_ids) > 3:
                raise ValidationError("Un cours ne peut pas avoir plus de 3 étudiants inscrits!")

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Le code du cours doit être unique!'),
        ('credits_positif', 'CHECK(credits >= 0)', 'Le nombre de crédits doit être positif.')
    ]
