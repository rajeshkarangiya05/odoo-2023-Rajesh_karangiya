# -*- coding: utf-8 -*-

from odoo import fields,api,models

class SymptomsData(models.Model):
	_name="symptoms.data"
	_description="Symptoms Data"


	medicine_id = fields.Many2one("medicine.information",string="Name of Medicine")
	symptoms_ids= fields.Many2many("health.symptoms","symptoms_oder_id",string="Symptoms")