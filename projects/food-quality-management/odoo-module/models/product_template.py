from odoo import models, fields

class ProductTemplate(models.Model):
    """
    Extension du modèle standard Product Template d'Odoo.
    On ajoute ici les caractéristiques "théoriques" ou "catalogue" liées à l'alimentaire.
    """
    _inherit = 'product.template'

    # Définit si le produit nécessite un suivi sanitaire particulier
    is_perishable = fields.Boolean(string="Est périssable", default=False)
    
    # Température optimale pour la conservation (ex: 4°C pour le frais)
    storage_temperature = fields.Float(string="Température de conservation (°C)")
    
    # Humidité optimale pour la conservation (ex: 80% pour les légumes)
    storage_humidity = fields.Float(string="Humidité de conservation (%)")
    
    # Délai entre deux contrôles qualité automatiques
    control_interval_days = fields.Integer(string="Intervalle de contrôle (jours)", default=30)
    
    # Relation vers le référentiel des allergènes
    allergen_ids = fields.Many2many('food.allergen', string="Allergènes")

    quality_check_count = fields.Integer(compute='_compute_quality_check_count')

    def _compute_quality_check_count(self):
        for template in self:
            template.quality_check_count = self.env['food.quality.control'].search_count([
                ('product_id.product_tmpl_id', '=', template.id)
            ])

    def action_view_quality_checks(self):
        return {
            'name': 'Quality Checks',
            'type': 'ir.actions.act_window',
            'res_model': 'food.quality.control',
            'view_mode': 'tree,form',
            'domain': [('product_id.product_tmpl_id', '=', self.id)],
            'context': {'default_product_id': self.id}
        }

