from odoo import fields,models,api,_

class StockMoveLines(models.Model):
	_inherit = 'stock.move.line'

	price_subtotal = fields.Float("Sub Total")



	def _get_aggregated_product_quantities(self, **kwargs):

		res = super(StockMoveLines,self)._get_aggregated_product_quantities()
		print("\n\npicking_id", self.picking_id)
		data = self.env["sale.order"].search([('picking_ids','=',self.picking_id.id)])
		test = data.order_line
		print("\n data",res)
		for element in test:
			
			print("\ntest",element.price_subtotal)
			res["sub_total"]= element.price_subtotal
		print(res)
		return res
