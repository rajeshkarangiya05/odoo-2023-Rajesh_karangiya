# -*- coding: utf-8 -*-

from odoo import fields, api, models
from datetime import datetime

class PricingData(models.Model):
	_name="pricing.data"
	_description="Pricing Data"


	name_id =fields.Many2one("medicine.information" ,domain="[('exp_date','>','str(datetime.today().date())')]")
	date=fields.Date(string="Date")
	symptoms = fields.Many2many("health.symptoms",string="Symptoms")
	price=fields.Integer(string="Price")
	quantity=fields.Integer(string="Quantity")


	@api.onchange("name_id")
	def _onchange_name_id(self):
		if not self.name_id:
			return
		self.date = datetime.now().date()