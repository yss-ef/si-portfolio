from odoo import models, fields

class FoodAllergen(models.Model):
    """
    Modèle représentant le référentiel des allergènes.
    Ce modèle permet de lister de manière normalisée les allergènes (Gluten, Arachide, etc.)
    pour éviter les erreurs de saisie et faciliter les filtres.
    """
    _name = 'food.allergen'
    _description = 'Référentiel des Allergènes'

    # Nom de l'allergène (ex: Lactose)
    name = fields.Char(string="Nom de l'allergène", required=True)
    
    # Description optionnelle pour plus de détails sur l'allergène
    description = fields.Text(string="Description")

