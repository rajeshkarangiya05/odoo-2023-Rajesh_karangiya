# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class HotelRoomBooking(models.Model):
	_name="hotel.room.booking"
	_description="Hotel Rooms booking User"
	_rec_name = "customer_id"

	hotel_id = fields.Many2one("hotel.management",string="Hotel name")
	customer_id = fields.Many2one("res.partner",string="Customer Name", required=True)
	user_email = fields.Char("Email")
	user_address = fields.Text("Address")
	checkin_date = fields.Datetime("Checkin-Date")
	checkout_date = fields.Datetime("Checkout-Date")
	room_lines_ids = fields.One2many("hotel.room.booking.lines","user_id",string="Rooms")
	state = fields.Selection(selection=[('draft', 'Draft'),
		('booked', 'Booked'),('cancel','Cancel')],
		 string='Status', required=True, readonly=True, copy=False, default='draft')



	@api.onchange("customer_id")
	def _onchange_auto_fill_address_email(self):
		for rec in self:
			if rec.customer_id:
				vals={
					"user_id": rec.customer_id.name
				}
				data = self.env["hotel.room.booking.lines"].create(vals)
				
				record = self.env["res.partner"].search([('id','=',rec.customer_id.id)])
				rec.user_email = record.email
				if not record.street2:
					rec.user_address = record.street+"\n"+(record.zip)+"\n"+(record.city)
				else:
					rec.user_address = (record.street)+"\n"+(record.street2)+"\n"+(record.zip)+"\n"+(record.city)


	# @api.onchange("hotel_id")
	# def _onchange_hotel_rooms(self):
	# 	for rec in self:
	# 		context = dict(self._context)
	# 		context["hotel_id"] = rec.hotel_id.id
	# 		print("context ----------- ",context)

	def Approve_booking(self):
		for rec in self:
			rec.write({'state': "booked"})


		template = self.env.ref('hotel_management.hotel_user_id').id	
		template_id = self.env['mail.template'].browse(template)
		template_id.send_mail(self.id, force_send=True)

	def cancel_booking(self):
		return {
			"type":"ir.actions.act_window",
			"name":"Cancel Booking",
			"res_model":"cancel.booking",
			"view_mode":"form",
			"target":"new",

		}

	def action_send_mail_checkout(self):
		for rec in self:
			template = self.env.ref('hotel_management.checkout_template_id').id	
			template_id = self.env['mail.template'].browse(template)
			template_id.send_mail(rec.id, force_send=True)

	
	def cron_checkout_reminder(self):
		room_data = self.env['hotel.room.booking'].search([])
		for rec in room_data:
			print(" ********* in scheduler")
			if rec.checkout_date > datetime.now() and rec.state == "booked" and rec.checkout_date.hour - datetime.now().hour == 1:
				print(" ********* in 2 scheduler")
				template = self.env.ref("hotel_management.checkout_template_id").id
				template_id = self.env["mail.template"].browse(template)
				template_id.send_mail(rec.id, force_send=True)

	@api.constrains('customer_id')
	def _check_chechout(self):
		for rec in self:
			if rec.checkin_date:
				if rec.checkout_date < rec.checkin_date:
					raise ValidationError("Invalid checkout Date.Checkout Date should be greater than checkin date")
			

			# if rec.checkin_date < datetime.now():
			# 	raise ValidationError("Invalid checkout Date")