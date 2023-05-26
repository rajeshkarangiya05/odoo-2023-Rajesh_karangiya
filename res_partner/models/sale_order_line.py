# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	@api.onchange('product_id')
	def product_id_change(self):
		res = super(SaleOrderLine,self).product_id_change()
		if not self.discount:
			if self.order_id.partner_id.is_prime_customer:
				self.update({'discount':self.order_id.partner_id.discount})
		return res