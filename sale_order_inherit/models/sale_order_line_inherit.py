from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = ['sale.order.line']

	p1 = fields.Char("P1")
	p2 = fields.Char("p2")


class ProductProduct(models.Model):
	_inherit = '[product.product]'

	