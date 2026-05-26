from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    quality_check_count = fields.Integer(compute='_compute_quality_check_count', string="Nombre de contrôles")

    def _compute_quality_check_count(self):
        for picking in self:
            lots = picking.move_line_ids.lot_id
            picking.quality_check_count = self.env['food.quality.control'].search_count([
                ('lot_id', 'in', lots.ids)
            ])

    def action_create_quality_check(self):
        """
        Crée un ticket de contrôle pour chaque lot.
        Gère les nouveaux lots (lot_name) en les créant à la volée.
        """
        self.ensure_one()
        lot_ids = self.env['stock.lot']
        
        for line in self.move_line_ids:
            if not line.lot_id and line.lot_name:
                existing_lot = self.env['stock.lot'].search([
                    ('name', '=', line.lot_name),
                    ('product_id', '=', line.product_id.id),
                    ('company_id', '=', self.company_id.id)
                ], limit=1)
                
                if existing_lot:
                    line.lot_id = existing_lot
                else:
                    new_lot = self.env['stock.lot'].create({
                        'name': line.lot_name,
                        'product_id': line.product_id.id,
                        'company_id': self.company_id.id,
                    })
                    line.lot_id = new_lot
            
            if line.lot_id:
                lot_ids |= line.lot_id

        if not lot_ids:
            lot_ids = self.move_ids.mapped('lot_ids')

        if not lot_ids:
            raise UserError(_("Veuillez saisir un numéro de lot dans les 'Opérations détaillées' avant de lancer le contrôle."))

        created_count = 0
        for lot in lot_ids:
            existing = self.env['food.quality.control'].search([
                ('lot_id', '=', lot.id),
                ('state', 'in', ('draft', 'in_progress'))
            ])
            if not existing:
                self.env['food.quality.control'].create({
                    'lot_id': lot.id,
                    'name': f"Contrôle Réception - {self.name} - {lot.name}",
                })
                created_count += 1
        
        if created_count > 0:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Succès'),
                    'message': _('%s ticket(s) de contrôle qualité ont été créés.') % created_count,
                    'sticky': False,
                    'type': 'success',
                }
            }
        else:
            raise UserError(_("Un contrôle qualité existe déjà pour ces lots."))

    def button_validate(self):
        """
        Verrou de sécurité universel : Bloque toute validation (Entrée/Sortie/Interne)
        si un produit alimentaire périssable n'a pas de contrôle conforme.
        """
        for line in self.move_line_ids:
            if line.lot_id and line.product_id.product_tmpl_id.is_perishable:
                # On cherche le dernier contrôle en date pour ce lot
                last_check = self.env['food.quality.control'].search([
                    ('lot_id', '=', line.lot_id.id)
                ], order='inspection_date desc', limit=1)
                
                if not last_check or last_check.state != 'passed':
                    raise UserError(_(
                        "SÉCURITÉ BLOQUANTE : Le lot %s (%s) n'a pas de contrôle qualité validé. "
                        "L'opération est interdite tant que le lot n'est pas déclaré conforme."
                    ) % (line.lot_id.name, line.product_id.name))
        
        return super(StockPicking, self).button_validate()
