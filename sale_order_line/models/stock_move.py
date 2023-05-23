from odoo import fields,models,api,_

class StockMove(models.Model):
	_inherit = 'stock.move'

	other_info = fields.Char("Other Info")
