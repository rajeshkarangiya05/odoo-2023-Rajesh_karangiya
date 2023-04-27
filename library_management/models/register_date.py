# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import timedelta, datetime

class RegisterDate(models.Model):
	_name="register.date"
	_description="Register Data"

	user_id = fields.Char(string="User ID")
	bookid = fields.Char(string="Book Line ID")
	built_relation_id = fields.Many2one("issue.books", string="Relational field")
	incoming_date = fields.Date(string="Incoming Date")
	outgoing_date = fields.Date(string="Outgoing Date", readonly=True)
	books_id_name = fields.Integer(string="Book Name ID")
	charges = fields.Integer(string="To pay", compute="_compute_charges")
	int_diff = fields.Integer(string="Expected Return Days")
	issue_book_id = fields.Integer(string="Issue Book Id")
	total_charge = fields.Integer(string="Total Charges")
	return_quantity=fields.Integer(string="Return")
	# empty_id = fields.Many2one('return.book',string="Empty id")

	# defining method for charge field
	@api.depends("incoming_date")
	def _compute_charges(self):
		count = 0
		for element in self:
			element.charges=0
			if not element.incoming_date:
		
				get_defaultcharge = self.env["book.details"].search([('id','=',element.books_id_name)])
				
				
				expected_return_date = self.env["register.books"].search([('id','=',element.bookid)])					
						
				in_date = element.outgoing_date
				current_day = datetime.now().date()
				if in_date:
					difference_day = (current_day-in_date).days
					if element.int_diff:				
						multiple =  difference_day//element.int_diff
						element.charges=get_defaultcharge.charges+(multiple*get_defaultcharge.charges)

						element.total_charge = element.charges

			issue_data =self.env["issue.books"].read_group([('id','=',element.issue_book_id)],fields=['id'],groupby=['name_id'])
			

	
	def return_book(self):
		print("...Helllllllllllllllllllooooooooo...")

	



		
	

	