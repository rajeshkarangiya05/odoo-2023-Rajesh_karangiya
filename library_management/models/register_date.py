# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterDate(models.Model):
	_name="register.date"
	_description="Register Data"

	user_id = fields.Char(string="User ID")
	bookid = fields.Char(string="Book Line ID")
	incoming_date = fields.Date(string="Incoming Date", readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date", readonly=True)
	books_id_name = fields.Integer(string="Book Name ID") 
	

	