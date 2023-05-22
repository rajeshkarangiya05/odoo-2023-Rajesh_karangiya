# -*- coding: utf-8 -*-

from odoo import fields, models,api,_

class HotelRoomBooking(models.Model):
	_name="user.bus.booking"

	name = fields.Char(string="Name", required=True)
	id_proof = fields.Binary(string="ID Proof")
	date = fields.Date("Departure Date")
	from_destination = fields.Char("From")
	to_destination = fields.Char("To")
	bus_type = fields.Char("Type")
	state = fields.Selection(selection=[('draft', 'Draft'),
		('booked', 'Booked'),('cancel','Cancel')],
		 string='Status', required=True, readonly=True, copy=False, default='draft')
	# method for 'Book Button'
	def approve_booking(self):
		self.write({
				"state":'booked'
			})

	# method for 'Cancel Button'
	def cancel_booking(self):
		self.write({
				"state":'cancel'
			})

