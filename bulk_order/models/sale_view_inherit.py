# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class SaleViewInherit(models.Model):
	_name="sale.view.inherit"
	_description="Sale View Inherit"

	name = fields.Char("Name")
	bulk_product_ids = fields.Many2many("product.product", "bulk_product_id",string="Products")

class SaleBulk(models.Model):
	_inherit = ['sale.order']

	bulk_product_id = fields.Many2one("sale.view.inherit",string="Bulk Product")

	@api.onchange("bulk_product_id")
	def _onchange_add_sale_order_lines(self):
		for rec in self:
			if rec.bulk_product_id:
				line_list = []
				print("\n\n\n",rec.bulk_product_id.bulk_product_ids)
				
				rec.order_line = False
				for data in rec.bulk_product_id.bulk_product_ids:
					sale_line = self.env["sale.order.line"]
					vals={
						'order_id':self.id,
						'product_id':data.id,
					}
					new_usecase = sale_line.new(vals)
					new_usecase.product_id_change()
					# new_usecase.write({
					# 	'price_unit':50
					# 	})	
					# sale_line_vals = sale_line._convert_to_write(new_usecase._cache)
					
					# sale_line_vals.update({
					# 	'price_unit':50
					# 	})
					# line_list.append((0, 0, sale_line_vals))
					# print('sale_line_vals-----',sale_line_vals)
				# print('line_list---------',line_list)
				# self.order_line = line_list

					# print("new_usecase",new_usecase.name)

					


