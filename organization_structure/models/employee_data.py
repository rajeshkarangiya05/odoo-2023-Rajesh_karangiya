# -*- coding: utf-8 -*-
from odoo import models, fields, api,_

class EmployeeData(models.Model):
	_name = 'employee.data'
	_description = 'Employee data'

	name = fields.Char("Employee name")
	designation_id = fields.Many2one("designation.data",string="Designation")
