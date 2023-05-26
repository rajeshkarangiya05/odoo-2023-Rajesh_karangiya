# -*- coding: utf-8 -*-

from odoo import fields,models,api,_


class stockMove(models.Model):
	_inherit = 'stock.move'
	
	other_info = fields.Char(string="Other info")