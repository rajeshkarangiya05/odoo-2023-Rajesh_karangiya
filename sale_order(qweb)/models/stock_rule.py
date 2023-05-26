# -*- coding: utf-8 -*-


from odoo import models,api,fields


class StockRule(models.Model):
	_inherit = 'stock.rule'

	def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
		move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
		new_data = self.env["sale.order.line"].search([('id','=',values['sale_line_id'])])
		move_values.update({'unit_price':new_data.price_unit})
		move_values.update({'price_subtotal':new_data.price_subtotal})
		move_values.update({'tax_id':new_data.tax_id})
		return move_values