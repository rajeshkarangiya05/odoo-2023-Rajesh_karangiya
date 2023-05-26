# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	other_info = fields.Char("Other Info")

	def _prepare_invoice_line(self, **optional_values):
		values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
		values.update({'other_info':self.other_info})
		return values