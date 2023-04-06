# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class RegisterBooks(models.Model):
	_name="register.books"
	_description="Register book detail"

	book_name_id = fields.Many2one("book.details", string="Book Name")
	empty_id = fields.Many2one("issue.books", string="Empty")
	issued_quantity = fields.Integer(string="Quantity")


	
