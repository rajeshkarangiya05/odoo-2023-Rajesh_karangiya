# -*- coding: utf-8 -*-

from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
	_inherit = 'res.partner'

	is_prime_customer = fields.Boolean(string="Is Prime Customer")
	discount = fields.Float(string="Discount")

	@api.constrains("discount")
	def _check_discount(self):
		for rec in self:
			if rec.discount and rec.discount > 100:
				raise ValidationError('Discount Greater then 100')

