# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models,api,fields


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        print("\n\n ----------------------- ")
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        print("\n\n",values)
        print(values['sale_line_id'])
        new_data = self.env["sale.order.line"].search([('id','=',values['sale_line_id'])])
        print(" ************* \n\n ",new_data)
        move_values['other_info'] = new_data.other_info
        print("move_values",move_values)
        return move_values


