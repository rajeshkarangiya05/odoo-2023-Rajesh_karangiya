# -*- coding: utf-8 -*-
from odoo import models, fields, api,_

class DesignationData(models.Model):
	_name = 'designation.data'
	_description = 'Employee Designation'

	name = fields.Char("Employee Designation")
	
