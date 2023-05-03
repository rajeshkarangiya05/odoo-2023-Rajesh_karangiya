# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class HotelManagement(models.Model):
	_name="hotel.management"
	_description="Hotel Management"

	name = fields.Char(string="Hotel name", required=True)
	contact = fields.Char(string="Contact No.")
	email = fields.Char(string="Email Id")	
	address = fields.Text(string="Address", required=True)
	website = fields.Char(string="Website")
