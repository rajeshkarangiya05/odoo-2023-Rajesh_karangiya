# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

# Classical Inheritance
# class SaleOrder(models. Model):
# 	_inherit = 'sale.order'

	# partner_id = fields.Many2one(
	#     'res.partner', string='Amit', readonly=True,
	#     states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
	#     required=True, change_default=True, index=True, tracking=1,
	#     domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)

class ResPartner(models.Model):
	_inherit = "res.partner"

	# new field to inherit res_partner and choosing if he/she is author or not
	is_author = fields.Boolean(string="Author")