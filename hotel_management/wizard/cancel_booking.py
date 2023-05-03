from odoo import fields,models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class CancelBooking(models.TransientModel):
	_name="cancel.booking"
	_description = "Cancel Booking"

	choice = fields.Selection(selection=[('cancelmail','Cancel Booking and send mail'),
		('cancel','Cancel Booking')], string="Choice")
	def action_confirm(self):
		state = self.env["hotel.room.booking"].search([('id','=',self._context["active_id"])])
		for rec in self:
			if rec.choice == "cancelmail":
				template = self.env.ref('hotel_management.cancel_booking_id').id	
				template_id = self.env['mail.template'].browse(template)
				template_id.send_mail(self.id, force_send=True)
				state.write({'state': "cancel"})
			elif rec.choice == 'cancel':				
				state.write({'state': "cancel"})


