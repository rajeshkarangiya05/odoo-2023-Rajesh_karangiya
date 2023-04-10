# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class BookType(models.Model):
	_name="book.type"
	_description="Book Type"

	name = fields.Char(string="Enter Book Type")