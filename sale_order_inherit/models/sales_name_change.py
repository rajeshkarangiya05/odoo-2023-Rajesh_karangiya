from odoo import fields,models,api,_

class SalesNameChange(models.Model):
	_inherit = 'sale.order'

	partner_id = fields.Many2one(
        'res.partner', string='Grahak', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)

	# sale_order = fields.Char(string='Rajesh')