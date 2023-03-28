# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class MedicineStock(models.Model):
	_name="medicine.stock"
	_description="Medicine Stock"


	name_id = fields.Many2one("medicine.information",string="Medicine Name")
	quantity = fields.Integer(string="Quantity")
	year = fields.Date(string="Date")


