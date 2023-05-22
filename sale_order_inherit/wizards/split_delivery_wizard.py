from odoo import models, fields, api
from itertools import groupby
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class SplitDeliveryWizard(models.TransientModel):
	_name = "split.delivery.wizard"


	split_product_ids = fields.One2many("intermediate.data","split_delivery_id",string="Products")


	def action_alot(self):
		for rec in self:
			new_list = []
			sale_order_rec = self.env['sale.order'].browse(self._context.get('sale_order_id'))
			old_pickings = sale_order_rec.picking_ids
			checked_picking_rec = sale_order_rec.picking_ids[0].copy({'move_ids_without_package':False})
			unchecked_picking_rec = sale_order_rec.picking_ids[0].copy({'move_ids_without_package':False})
			for split_line_rec in rec.split_product_ids.filtered(lambda a: a.select_data):
				new_move_id = split_line_rec.move_id.copy()
				new_move_id.picking_id = checked_picking_rec.id
			for split_line_rec in rec.split_product_ids.filtered(lambda a: not a.select_data):
				new_move_id = split_line_rec.move_id.copy()
				new_move_id.picking_id = unchecked_picking_rec.id
			checked_picking_rec.action_confirm()
			unchecked_picking_rec.action_confirm()
			old_pickings.action_cancel()



class IntermediateData(models.TransientModel):
	_name = 'intermediate.data'

	split_delivery_id = fields.Many2one("split.delivery.wizard")
	product_data_id = fields.Many2one("product.product",string="Products")
	move_id = fields.Many2one("stock.move",string="Move")
	select_data = fields.Boolean(string="Select")
