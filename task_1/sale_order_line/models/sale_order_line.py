from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	ref = fields.Char("ref")

	@api.onchange("product_id")
	def get_internal_reference(self):
		domain = super(SaleOrderLine, self).product_id_change()
		if self.product_id:
			self.ref = self.product_id.default_code
		return domain
