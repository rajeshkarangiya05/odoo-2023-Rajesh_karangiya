# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterBooks(models.Model):
	_name="register.books"
	_description="Register book detail"


	book_name_id = fields.Many2one("book.details", string="Book Name")
	empty_id = fields.Many2one("issue.books", string="Empty")
	issued_quantity = fields.Integer(string="Quantity")
	book_data_ids = fields.Many2many("book.type","book_data_ids", string="Book Types")

	
	@api.onchange("book_name_id")
	def onchange_book_type(self):
		if not self.book_name_id:
			return
		else:
			record = self.env["book.details"].search([('id','=',self.book_name_id.id)])
			self.update({
				"book_data_ids":[(6,0,record.book_types_ids.ids)]
				})






