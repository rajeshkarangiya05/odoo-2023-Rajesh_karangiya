# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from odoo.osv import expression

class BusData(models.Model):
	_name="bus.data"

	bus_type = fields.Selection(selection=[('sleeper','Sleeper'),('seater','Seater'),('combo','Sleeper-seater')],string="Type of Bus")
	specification_ids = fields.Many2many('bus.specific','specific_ids',string="Facilities")
	company = fields.Char("Manufacturing Company", required=True)

	@api.model
	def _name_search(self,name,args=None,operator='ilike',limit=100,name_get_uid=None):
		if name:
			domain = ['|','|',
				('bus_type',operator,name),
				('specification_ids',operator,name),
				('company',operator,name)]

			return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
		return super()._name_search(name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)

	def name_get(self):
		result=[]
		for data in self:
			name = data.company + '/' + data.bus_type 
			result.append(((data.id),name))
		return result




class BusSpecific(models.Model):
	_name = "bus.specific"
	_rec_name = 'specification'

	specification = fields.Char(string="Bus Facility")


