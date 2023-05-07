# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
# from openerp import tools

class HotelManagement(models.Model):
	_name="hotel.management"
	_description="Hotel Management"

	name = fields.Char(string="Hotel name", required=True)
	contact = fields.Char(string="Contact No.")
	email = fields.Char(string="Email Id")	
	address = fields.Text(string="Address", required=True)
	website = fields.Char(string="Website")
	image = fields.Binary(string="Image")


	# @api.model
	# def create(self,vals):
	# 	if "image" in vals:
	# 		resize_image = tools.image_resize_image(vals["image"],size = (250,250),avoid_if_small =True)
	# 		vals["image"] = resize_image
	# 		return super(HotelManagement,self).create(vals)

	# @api.model
	# def write(self,vals):
	# 	if "image" in vals:
	# 		resize_image = tools.image_resize_image(vals["image"],size = (250,250),avoid_if_small =True)
	# 		vals["image"] = resize_image
	# 		return super(HotelManagement,self).create(vals)
