from odoo import fields, models,api,_

class BillingUser(models.Model):
	# _name = 'billing.user'
	# _description = 'Billing user'
	_inherit = 'sale.order'

	partner_id = fields.Many2one(
		'res.partner', string='User', readonly=True,
		states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
		required=True, change_default=True, index=True, tracking=1,
		domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)

	# date_order = fields.Datetime(string='Order Date', required=True, readonly=True,
	# 		index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
	# 		copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")
	# payment_term_id = fields.Many2one(
	# 	'account.payment.term', string='Payment Terms', check_company=True,  # Unrequired company
	# 	domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
	# pricelist_id = fields.Many2one(
	# 	'product.pricelist', string='Pricelist', check_company=True,  # Unrequired company
	# 	required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
	# 	domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
	# 	help="If you change the pricelist, only newly added lines will be affected.")
	# validity_date = fields.Date(string='Expiration', readonly=True, copy=False, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
	# 	default=_default_validity_date)
	# state = fields.Selection([
	#     ('draft', 'Quotation'),
	#     ('sent', 'Quotation Sent'),
	#     ('sale', 'Sales Order'),
	#     ('done', 'Locked'),
	#     ('cancel', 'Cancelled'),
	#     ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

			
						