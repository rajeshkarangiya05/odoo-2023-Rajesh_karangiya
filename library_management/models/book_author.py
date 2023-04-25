# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class BookAuthor(models.Model):
	_name="book.author"
	_description="Book author details"

	name = fields.Char(string="Author name")
	email = fields.Char(string="Email Id")
	contact = fields.Char(string="Contact No.")
	address = fields.Text(string="Address")

	def fun():
		print("x = 10")

	fun()