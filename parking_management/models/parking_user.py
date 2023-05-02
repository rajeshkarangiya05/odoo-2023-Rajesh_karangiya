from odoo import fields,models,api,_

class ParkingUser(models.Model):
	_name="parking.user"
	_description="Menu"


	name_id=fields.Many2one("res.partner",string="Name", required=True)
	vehicle_number=fields.Char(string="Vehicle Number")
	phone=fields.Char(string="Phone No.")
	Vehicle_type_id = fields.Many2one("vehicel.type",string="Choose vehicle Type")
	two_wheel_slot = fields.Integer("Two wheel slots")
	token=fields.Char(string="Entry ticket Number", readonly=True, store=True)
	state = fields.Selection(selection=[('draft','Draft'),
		('token','Token'),('payment','Payment')],string='Status',required=True, readonly=True,
		 copy=False, default='draft')
	payment = fields.Many2one("payment.type", string="Payment Type")
	slots = fields.Many2one("slot.data", string="Choose Slot")
	user_image = fields.Binary("User Image")

	# mehtod for "Avaialable Slotes" smart button
	@api.onchange("Vehicle_type_id")
	def action_two_wheel_slots(self):
		num = 0
		slot = self.env["slot.data"].search([("vehicel_type_id",'=',self.Vehicle_type_id.id)])
		for rec in slot:
			num+=rec.strength
		self.two_wheel_slot = num		

	# method for "Generate Token" button
	def action_Generate_token(self):
		for rec in self:
			rec.write({'state': "token"})
			if not rec.token:     
				rec.token = self.env["ir.sequence"].next_by_code("parking.user")

	# method for "Payment" button
	def action_payment(self):
		for rec in self:
			rec.write({'state': "payment"})

	#method to given ticket number to slot_data model
	@api.onchange("token")
	def token_update(self):
		for rec in self:
			print("\n\n in............")
			# if rec.token:
			print("\n\n in............",rec.slots.ids)
			token_data = self.env["slot.data"].search([("id",'=',rec.slots.id)])
			print("\n\n\n token_data",token_data)
			token_data.token_user = rec.token
			print("token_data.token_user",token_data.token_user)

	@api.onchange("name_id")
	def _onchange_default_image(self):
		for rec in self:
			record = self.env["res.partner"].search([('id','=',rec.name_id.id)])
			rec.user_image = record.image_1920









