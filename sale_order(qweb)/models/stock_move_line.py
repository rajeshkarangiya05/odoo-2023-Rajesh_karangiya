# -*- coding: utf-8 -*-

from odoo import fields,models,api,_
import json

class StockMoveLine(models.Model):
	_inherit = 'stock.move.line'


	def _get_aggregated_product_quantities(self, **kwargs):
		res = super(StockMoveLine,self)._get_aggregated_product_quantities()
		for rec in self:
			for element in res.keys():
				print()
				if res[element]['product'] == rec.product_id:
					res[element]["unit_price"] = rec.move_id.unit_price
					res[element]["sub_total"] = rec.move_id.price_subtotal
					res[element]["tax_id"] = rec.move_id.tax_id.name
		return res



