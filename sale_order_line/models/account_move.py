from odoo import fields,models,api,_

class AccountMove(models.Model):
	_inherit = 'account.move.line'

	other_info = fields.Char("Other Info")
