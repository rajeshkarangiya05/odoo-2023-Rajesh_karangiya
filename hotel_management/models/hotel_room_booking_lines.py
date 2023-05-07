# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import datetime,date
from odoo.exceptions import ValidationError

class HotelRoomBookinglines(models.Model):
	_name="hotel.room.booking.lines"
	_description="Intermediate Hotel Data "

	hotel_room_id = fields.Many2one("hotel.room",string="Hotel Rooms")
	count_adults = fields.Integer("Number of Adults")
	count_children = fields.Integer("Number of Children")
	default_price = fields.Integer("Price of Room")
	user_id = fields.Char(string="User ID")



	# method to check if discount to be applied or not
	@api.onchange("hotel_room_id")
	def discount_price(self):
		todays_date = datetime.now().date()
		for rec in self:
			rec.default_price=0
			record = self.env["hotel.room"].search([('id','=',rec.hotel_room_id.id)])
			if rec.hotel_room_id:
				if todays_date >= record.discount_valid_from and todays_date <= record.discount_valid_to :
					if record.discount > 0:
						reduced_price = record.room_price - record.room_price*(record.discount/100)
						rec.default_price = reduced_price
					else:
						rec.default_price = record.room_price
				else:
					rec.default_price = record.room_price

	# method for defining number of childern and adults
	@api.constrains('hotel_room_id')
	def _check_child_adult_quantity(self):
		for rec in self:
			if rec.count_adults > 8:
				raise ValidationError("Invalid input for field Number of Adults.Number of Adults should be greater than zero but less than 8")
			elif rec.count_children > 6:
				raise ValidationError("Invalid input for field Number of Childrens.Number of Childrens should be greater than zero but less than 6")
			elif rec.count_adults <= 0 or rec.count_children <=0:
				raise ValidationError("Invalid input for field Number of Childrens or Number of Adults .Number of Childrens or  Number of Adults should be greater than zero")
	
	# method to get rooms in dropdown for particular hotel
	# @api.onchange("hotel_room_id")
	# def name_get(self):
	# 	print("self----------------",self._context)
	# 	for rec in self:
	# 		print("self._context.get('my_hotel')",self._context.get('my_hotel'))
	# 		rec.hotel_room_id = self._context.get('my_hotel')
	# 		print("rec.hotel_room_id.hotel_name_id",rec.hotel_room_id.hotel_name_id)
