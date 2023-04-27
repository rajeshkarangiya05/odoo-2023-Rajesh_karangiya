# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterBooks(models.Model):
	_name="register.books"
	_description="Register book detail"


	book_name_id = fields.Many2one("book.details", string="Book Name")
	issue_bookline_ids = fields.Integer(string="Issue Book ID")
	empty_id = fields.Many2one("issue.books", string="Empty")
	issued_quantity = fields.Integer(string="Quantity")
	intermediate_quantity = fields.Integer("Pending Quantity", compute="compute_pending_quantity")
	book_data_ids = fields.Many2many("book.type","book_data_ids", string="Book Types")
	return_date = fields.Date(string="Expected Return Date")
	charges = fields.Integer(string="Charges")
	
	# method for updating book type
	@api.onchange("book_name_id")
	def onchange_book_type(self):
		if not self.book_name_id:
			return
		else:
			record = self.env["book.details"].search([('book_name','=',self.book_name_id.book_name)])
			self.update({
				"book_data_ids":[(6,0,record.book_types_ids.ids)]
				})
	# method for adding pending quantity field
	@api.depends('book_name_id')
	def compute_pending_quantity(self):
		for rec in self:
			rec.intermediate_quantity = 0
			if rec.issued_quantity:
				data = self.env["register.date"].search_count([('books_id_name','=',rec.book_name_id.id),
					('incoming_date','=',False),
					('issue_book_id','=',rec.issue_bookline_ids)])

				rec.intermediate_quantity = data



	






