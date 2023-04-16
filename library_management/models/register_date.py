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
	charges = fields.Integer(string="Charges", compute="_compute_charges", store=True)
	int_diff = fields.Integer(string="Expected Return Days")

	# defining method for charge field
	@api.depends("incoming_date")
	def _compute_charges(self):
		for element in self:
			element.charges=0
			if not element.incoming_date:
		
				get_defaultcharge = self.env["book.details"].search([('id','=',element.books_id_name)])
				expected_return_date = self.env["register.books"].search([('id','=',element.bookid)])					
		
				# if element.int_diff:					
				in_date = element.outgoing_date
				current_day = datetime.now().date()
				difference_day = (current_day-in_date).days					
				multiple =  difference_day//5
				element.charges=get_defaultcharge.charges+(multiple*get_defaultcharge.charges)


		
	

	