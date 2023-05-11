from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class SaleNameChange(models.Model):
	_inherit = ['sale.order']

	partner_id = fields.Many2one(
		'res.partner', string='Grahak', readonly=True,
		states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
		required=True, change_default=True, index=True, tracking=1,
		domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)

	rajesh = fields.Char(string='st')

	def action_merge_quotation(self):
		# data = {}
		
		if all(rec.state == 'draft' for rec in self) and len(self.partner_id.ids) == 1:
			self.action_cancel()	
			new_record = self.create({'partner_id':self.partner_id.id})
			for element in self.order_line:				
				element.copy({'order_id': new_record.id})
			new_record.action_confirm()


		else:
			raise ValidationError('The state of Quotation is not draft or you have choose multiple Gharak')

