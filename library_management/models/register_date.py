# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterDate(models.Model):
	_name="register.date"
	_description="Register Data"

	bookid = fields.Char(string="Book ID")
	incoming_date = fields.Date(string="Incoming Date", readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date", readonly=True)
	

	