# -*- coding: utf-8 -*-

from odoo import fields,models,api,_


class stockMove(models.Model):
	_inherit = 'stock.move'

	unit_price = fields.Float("Unit Price" )
	price_subtotal = fields.Float("Sub Total")
	tax_id = fields.Many2many('account.tax','product_tax_id', string = 'Taxes')
	