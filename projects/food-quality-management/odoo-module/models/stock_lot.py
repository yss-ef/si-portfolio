from odoo import models, fields

class StockLot(models.Model):
    """
    Extension du modèle Stock Lot (numéros de série/lot).
    Gère les données "physiques" liées à une instance spécifique de produit en stock.
    """
    _inherit = 'stock.lot'

    # Stocke la date du dernier passage d'un inspecteur sur ce lot précis
    last_control_date = fields.Date(string="Date du dernier contrôle")
    quality_check_count = fields.Integer(compute='_compute_quality_check_count')

    def _compute_quality_check_count(self):
        for lot in self:
            lot.quality_check_count = self.env['food.quality.control'].search_count([
                ('lot_id', '=', lot.id)
            ])

    def action_view_quality_checks(self):
        return {
            'name': 'Quality Checks',
            'type': 'ir.actions.act_window',
            'res_model': 'food.quality.control',
            'view_mode': 'tree,form',
            'domain': [('lot_id', '=', self.id)],
            'context': {'default_lot_id': self.id}
        }

    def _cron_check_quality_controls(self):
        """
        Méthode déclenchée par l'action planifiée (Cron).
        Parcourt les lots périssables et génère un contrôle s'ils n'ont pas été vérifiés
        depuis un certain temps (défini sur le produit).
        """
        today = fields.Date.context_today(self)
        # On ne cherche que les produits marqués comme périssables
        lots = self.search([
            ('product_id.product_tmpl_id.is_perishable', '=', True),
        ])
        
        for lot in lots:
            should_control = False
            
            # Cas 1 : Jamais contrôlé
            if not lot.last_control_date:
                should_control = True
            else:
                # Cas 2 : L'intervalle théorique est dépassé
                interval = lot.product_id.product_tmpl_id.control_interval_days
                delta = (today - lot.last_control_date).days
                if delta >= interval:
                    should_control = True
            
            if should_control:
                # Éviter de créer 10 fois le même ticket si le cron tourne plusieurs fois
                # On vérifie s'il existe déjà un contrôle en brouillon pour ce lot
                existing = self.env['food.quality.control'].search([
                    ('lot_id', '=', lot.id),
                    ('state', '=', 'draft')
                ])
                
                if not existing:
                    # Création automatique du ticket de contrôle
                    self.env['food.quality.control'].create({
                        'lot_id': lot.id,
                        'name': f"Contrôle périodique - {lot.name}",
                        'inspection_date': today,
                    })

