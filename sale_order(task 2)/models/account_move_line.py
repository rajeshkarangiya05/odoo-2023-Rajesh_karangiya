# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class AccountMoveLine(models.Model):
	_inherit = 'account.move.line'

	other_info = fields.Char("Other Info")