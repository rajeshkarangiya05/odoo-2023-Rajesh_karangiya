from odoo import fields,models

class VehicleType(models.Model):
	_name="vehicel.type"
	_description="Vehicle Type"


	name=fields.Char(string="Type of Vehicle")
