from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class FoodQualityControl(models.Model):
    """
    Modèle central gérant les inspections sanitaires.
    """
    _name = 'food.quality.control'
    _description = 'Contrôle Qualité Alimentaire'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'inspection_date desc'

    name = fields.Char(string="N° de Ticket", required=True, copy=False, default='Nouveau', tracking=True)
    lot_id = fields.Many2one('stock.lot', string="Lot à contrôler", required=True, tracking=True)
    product_id = fields.Many2one('product.product', related='lot_id.product_id', store=True, string="Produit")
    inspection_date = fields.Date(string="Date d'inspection", default=fields.Date.context_today, tracking=True)
    recorded_temperature = fields.Float(string="Température relevée (°C)", tracking=True)
    target_temperature = fields.Float(related='product_id.product_tmpl_id.storage_temperature', string="Température cible")
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('in_progress', 'En inspection'),
        ('passed', 'Conforme'),
        ('failed', 'Non Conforme')
    ], string="État", default='draft', tracking=True)
    
    notes = fields.Text(string="Observations")
    inspector_id = fields.Many2one('res.users', string="Inspecteur", default=lambda self: self.env.user, tracking=True)

    @api.constrains('recorded_temperature', 'state')
    def _check_temperature_safety(self):
        for record in self:
            if record.state == 'passed':
                if record.recorded_temperature > (record.target_temperature + 10.0):
                    raise ValidationError(_(
                        "SÉCURITÉ ALIMENTAIRE : Température trop élevée (%s°C) pour ce type de produit (Cible: %s°C). "
                        "Validation impossible."
                    ) % (record.recorded_temperature, record.target_temperature))

    def action_validate(self):
        for record in self:
            record.state = 'passed'
            record.lot_id.last_control_date = fields.Date.context_today(self)
            record.message_post(body=_("Inspection validée : Lot conforme."))

    def action_reject(self):
        for record in self:
            record.state = 'failed'
            record.message_post(body=_("Inspection rejetée : Risque sanitaire détecté."))
