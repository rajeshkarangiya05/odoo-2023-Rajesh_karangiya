from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	ref = fields.Char("ref")
	other_info = fields.Char("Other Info")

	@api.onchange("product_id")
	def get_internal_reference(self):
		domain = super(SaleOrderLine, self).product_id_change()
		record = self.env["product.product"].search([('id','=',self.product_id.id)])
		print(record)
		if self.product_id:
			self.ref = record.default_code
		return domain

