from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class SaleDescription(models.Model):
	_inherit = ['product.template']

	description_new = fields.Boolean("Description")
