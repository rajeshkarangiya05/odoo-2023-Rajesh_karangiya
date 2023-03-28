# -*- coding: utf-8 -*-

from odoo import fields, models

class HealthSymptoms(models.Model):
	_name="health.symptoms"
	_description="health detail"
	

	name = fields.Char(string="Name of symptoms")
	
