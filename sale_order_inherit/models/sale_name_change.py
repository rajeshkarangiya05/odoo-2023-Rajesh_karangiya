from odoo import fields,models,api,_

class SaleNameChange(models.Model):
	_inherit = ['sale.order']

	partner_id = fields.Many2one(
		'res.partner', string='Rajesh', readonly=True,
		states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
		required=True, change_default=True, index=True, tracking=1,
		domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)

	rajesh = fields.Char(string='st')

# class ResPartnerCompany(models.Model):
# 	_inherit = ['res.partner']
	
# 	company_type = fields.Selection(string='Company Type',
# 		selection=[('person', 'Individual'), ('company', 'Company'),('tools','Tools')],
# 		compute='_compute_company_type', inverse='_write_company_type')