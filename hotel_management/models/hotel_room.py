# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class HotelRoom(models.Model):
	_name="hotel.room"
	_description="Hotel Rooms"

	roomId = fields.Char("Room ID", readonly=True)
	number_of_rooms = fields.Integer("Number of Rooms")
	room_description = fields.Text("Description")
	hotel_name_id = fields.Many2one("hotel.management",string="Hotel Name", required=True)
	room_type = fields.Selection(selection=[('ac','AC'),('nonac','Non-AC')],
		string="Room TYpe", default="ac")
	discount = fields.Integer("Discount")
	discount_valid_from = fields.Date("Discount valid From")
	discount_valid_to = fields.Date("Discount valid To")
	room_price = fields.Integer("Room Price")

	# method for defining room id sequence
	@api.model
	def create(self,vals):
		if not vals.get('roomId'):
			room_sequence = self.env['ir.sequence'].next_by_code('hotel.room')
			vals["roomId"] = room_sequence
		return super(HotelRoom,self).create(vals)

	# name search method for searching room name as HotelName/Roomcode formate
	def name_get(self):
		result=[]
		for element in self:
			hotel = element.hotel_name_id.name +"/"+ element.roomId
			result.append((element.id,hotel))
		return result
