from odoo import fields,models,api,_


class ProductProduct(models.Model):
	_inherit = ['product.template']

	p1 = fields.Char("P1")
	p2 = fields.Char("P2")

