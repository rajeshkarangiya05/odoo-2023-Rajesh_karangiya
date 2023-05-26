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
	partner_email = fields.Char("Email", related='customer_id.email', store=True)
	user_email = fields.Char("OLD Email")
	user_address = fields.Text("Address")
	checkin_date = fields.Datetime("Checkin-Date", required=True)
	checkout_date = fields.Datetime("Checkout-Date", required=True)
	room_lines_ids = fields.One2many("hotel.room.booking.lines","user_id",string="Rooms", ondelete="cascade")
	state = fields.Selection(selection=[('draft', 'Draft'),
		('booked', 'Booked'),('cancel','Cancel')],
		 string='Status', required=True, readonly=True, copy=False, default='draft')
	user_image = fields.Binary("User Image")
	color = fields.Integer(string="Color",compute="_compute_get_color")
	form_state = fields.Char("State")

	# method for giving kannban view line color
	def _compute_get_color(self):
		for rec in self:
			if rec.state == 'draft':
				rec.color = 1
			elif rec.state == 'booked':
				rec.color = 3
			else:
				rec.color = 4

	# method to fill fields like user_email, user_address, user_image 
	@api.onchange("customer_id")
	def _onchange_auto_fill_address_email(self):
		print("\n\n-----------in-------------------------------------------------asideeeeeee")
		for rec in self:
			if rec.customer_id:
				
				record = self.env["res.partner"].search([('id','=',rec.customer_id.id)])
				rec.user_email = record.email
				rec.user_image = record.image_1920
				if not record.street2:
					rec.user_address = record.street+"\n"+(record.zip)+"\n"+(record.city)
				else:
					rec.user_address = (record.street)+"\n"+(record.street2)+"\n"+(record.zip)+"\n"+(record.city)

	@api.onchange("customer_id")
	def _onchange_auto_fill_user_id(self):
		if self.room_lines_ids:
			vals={
				"user_id": self.id
			}
			data = self.env["hotel.room.booking.lines"].create(vals)

	# method on "Approve" button to send mail to user and change state
	def Approve_booking(self):
		for rec in self:
			rec.write({'state': "booked"})
		template = self.env.ref('hotel_management.hotel_user_id').id	
		template_id = self.env['mail.template'].browse(template)
		template_id.send_mail(self.id, force_send=True)

	# wizard on "cancel" button 
	def cancel_booking(self):
		return {
			"type":"ir.actions.act_window",
			"name":"Cancel Booking",
			"res_model":"cancel.booking",
			"view_mode":"form",
			"target":"new",
		}

	# action server to send mail for checkout before 1 hour of checkout date
	def action_send_mail_checkout(self):
		for rec in self:
			template = self.env.ref('hotel_management.checkout_template_id').id	
			template_id = self.env['mail.template'].browse(template)
			template_id.send_mail(rec.id, force_send=True)

	# schedular method to send checkout mail before 1 hour of checkout date
	def cron_checkout_reminder(self):
		room_data = self.env['hotel.room.booking'].search([])
		for rec in room_data:
			print(" ********* in scheduler")
			if rec.checkout_date > datetime.now() and rec.state == "booked" and rec.checkout_date.hour - datetime.now().hour == 1:
				print(" ********* in 2 scheduler")
				template = self.env.ref("hotel_management.checkout_template_id").id
				template_id = self.env["mail.template"].browse(template)
				template_id.send_mail(rec.id, force_send=True)

	# method to through valicationError if checkout date is less than Checkin date
	@api.constrains('checkin_date','checkout_date')
	def _check_checkout(self):
		for rec in self:
			record = self.env["hotel.room.booking"].search([])
			if rec.checkout_date < rec.checkin_date:
				raise ValidationError("Invalid checkout Date.Checkout Date should be greater than checkin date")
	
	# method to check if user already exists and is in draft sate
	@api.onchange("customer_id")
	def _onchange_check_user_form(self):
		for rec in self:
			record = self.env["hotel.room.booking"].search([])
			for data in record:
				print("data.state", data.state)
				print("record.customer_id",data.customer_id.name)
				print("rec.customer_id",rec.customer_id.name)
				if rec.customer_id == data.customer_id and data.state == "draft" :
					raise ValidationError("User %s already exists and is in draft state"% (rec.customer_id.name))


