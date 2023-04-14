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
		res = super(RegisterDate,self)
		for element in self:
			element.charges=0
			print("int_diff",element.int_diff)
			if element.outgoing_date:
				get_defaultcharge = self.env["book.details"].search([('id','=',element.books_id_name)])
				print("get_defaultcharge.charges",get_defaultcharge.charges)
				expected_return_date = self.env["register.books"].search([('id','=',element.bookid)])
				print("expected_return_date",expected_return_date)
				if not element.incoming_date:
					if expected_return_date:						
						in_date = element.outgoing_date
						current_day = datetime.now().date()
						difference_day = (current_day-in_date).days
						if element.int_diff:
							multiple =  difference_day//element.int_diff
							# if multiple <=0:
							# 	element.charges=get_defaultcharge.charges
							# else:
							print("get_defaultcharge.charges",get_defaultcharge.charges)
							element.charges=get_defaultcharge.charges+(multiple*get_defaultcharge.charges)


		
	

	