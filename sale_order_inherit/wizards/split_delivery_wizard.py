from odoo import models, fields

class SplitDeliveryWizard(models.TransientModel):
	_name = "split.delivery.wizard"

	name=fields.Char("Name")
	split_product_ids = fields.One2many("intermediate.data","split_delivery_id",string="Products")

	def action_alot(self):
		pass

class IntermediateData(models.TransientModel):
	_name = 'intermediate.data'

	split_delivery_id = fields.Many2one("split.delivery.wizard")
	product_data_id = fields.Many2one("product.product",string="Products")
	

