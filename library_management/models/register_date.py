# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterDate(models.Model):
	_name="register.date"
	_description="Register Data"


	issue_date_data = fields.Date(string="Issue Date")
	

	