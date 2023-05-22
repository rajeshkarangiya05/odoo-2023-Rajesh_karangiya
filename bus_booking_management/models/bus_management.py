# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from odoo.exceptions import ValidationError

class BusManagement(models.Model):
	_name="bus.management"
	_rec_name = 'owner'

	country_id = fields.Many2one('res.country',string="Country")
	state_id = fields.Many2one('res.country.state', string="State",domain="[('country_id', '=', country_id)]")
	from_id = fields.Many2one('res.city', string="From", domain="[('state_id', '=', state_id)]")
	to_id = fields.Many2one('res.city', string="To", domain="[('state_id', '=', state_id)]")
	owner = fields.Char("Owner", required=True)
	bus_ids = fields.Many2many("bus.data","bus_ids",string="Bus Type")
	journey_start_time = fields.Float(string="Journey Start Time")
	journey_end_time = fields.Float(string="Journey End Time")
	

	@api.constrains('from_id','to_id')
	def _check_to_id(self):
		for rec in self:
			if not rec.from_id:
				raise ValidationError("From field is empty")
			elif rec.to_id and rec.from_id:
				if rec.to_id == rec.from_id:
					raise ValidationError("From and To destination are same")

	# method to duplicate the record
	# def action_duplicate(self):
		




			

