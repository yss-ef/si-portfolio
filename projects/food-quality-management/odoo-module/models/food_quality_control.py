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
    
    recorded_humidity = fields.Float(string="Humidité relevée (%)", tracking=True)
    target_humidity = fields.Float(related='product_id.product_tmpl_id.storage_humidity', string="Humidité cible")

    packaging_state = fields.Selection([
        ('intact', 'Intact'),
        ('damaged', 'Endommagé'),
        ('soiled', 'Souillé'),
        ('swollen', 'Gonflé')
    ], string="État de l'emballage", default='intact', tracking=True)

    visual_aspect = fields.Selection([
        ('normal', 'Normal'),
        ('abnormal', 'Anormal / Suspect')
    ], string="Aspect visuel", default='normal', tracking=True)

    smell_check = fields.Selection([
        ('normal', 'Normal'),
        ('suspicious', 'Suspect / Mauvaise odeur')
    ], string="Odeur", default='normal', tracking=True)

    lot_expiration_date = fields.Date(related='lot_id.expiration_date', string="Date de péremption")
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('in_progress', 'En inspection'),
        ('passed', 'Conforme'),
        ('failed', 'Non Conforme')
    ], string="État", default='draft', tracking=True)
    
    notes = fields.Text(string="Observations")
    inspector_id = fields.Many2one('res.users', string="Inspecteur", default=lambda self: self.env.user, tracking=True)

    @api.constrains('recorded_temperature', 'state', 'packaging_state', 'visual_aspect', 'smell_check')
    def _check_food_safety(self):
        for record in self:
            if record.state == 'passed':
                # 1. Vérification Température
                if record.recorded_temperature > (record.target_temperature + 10.0):
                    raise ValidationError(_(
                        "SÉCURITÉ ALIMENTAIRE : Température trop élevée (%s°C) pour ce type de produit (Cible: %s°C). "
                        "Validation impossible."
                    ) % (record.recorded_temperature, record.target_temperature))
                
                # 2. Vérification Date de Péremption
                if record.lot_expiration_date and record.lot_expiration_date < fields.Date.context_today(self):
                    raise ValidationError(_(
                        "SÉCURITÉ ALIMENTAIRE : Le lot est périmé (DLC: %s). "
                        "Validation impossible."
                    ) % record.lot_expiration_date)

                # 3. Vérification Organoleptique
                if record.packaging_state == 'swollen':
                    raise ValidationError(_("ALERTE : Un emballage gonflé est un signe de risque bactérien majeur. Validation refusée."))
                
                if record.visual_aspect == 'abnormal' or record.smell_check == 'suspicious':
                    raise ValidationError(_("SÉCURITÉ ALIMENTAIRE : L'aspect ou l'odeur du produit est suspect. Validation refusée."))

    def action_validate(self):
        for record in self:
            record.state = 'passed'
            record.lot_id.last_control_date = fields.Date.context_today(self)
            record.message_post(body=_("Inspection validée : Lot conforme."))

    def action_reject(self):
        for record in self:
            record.state = 'failed'
            record.message_post(body=_("Inspection rejetée : Risque sanitaire détecté."))
