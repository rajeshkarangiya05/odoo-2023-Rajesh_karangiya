from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = ['sale.order.line']

	p1 = fields.Char("P1")
	p2 = fields.Char("p2")

	@api.onchange("product_id")
	def product_id_change(self):
		domain = super(SaleOrderLine, self).product_id_change()
		record = self.env["product.product"].search([('id','=',self.product_id.id)])
		print(record)
		if self.product_id:
			self.p1 = record.p1
			self.p2 = record.p2
		return domain





	