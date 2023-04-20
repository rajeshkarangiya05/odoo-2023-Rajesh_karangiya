# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import timedelta, datetime

class RegisterDate(models.Model):
	_name="register.date"
	_description="Register Data"

	user_id = fields.Char(string="User ID")
	bookid = fields.Char(string="Book Line ID")
	incoming_date = fields.Date(string="Incoming Date", readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date", readonly=True)
	books_id_name = fields.Integer(string="Book Name ID")
	charges = fields.Integer(string="Charges", compute="_compute_charges")

	#defining method for charge field
	@api.depends("incoming_date")
	def _compute_charges(self):
		for element in self:
			get_defaultcharge = self.env["book.details"].search([('id','=',element.books_id_name)])
			five_day_diff = element.outgoing_date + timedelta(days=5)
			if not element.incoming_date:				
				if datetime.now().date() <= five_day_diff:
					element.charges=get_defaultcharge.charges
				else:
					element.charges=get_defaultcharge.charges*2


		
	

	