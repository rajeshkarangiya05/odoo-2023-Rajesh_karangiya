# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProfessorRecord(models.Model):
    _name = "professor.record"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, help="")
    subject_id = fields.Many2one('student.subject', string='Subject', copy=False)
    student_id = fields.Many2one('student.information', string='Student')
    
    partnerdata = fields.Char("PARTNER DATA")


    def write(self,value):
        print ("www",self._context)
        self.with_context(from_write=True).call_method()
        res = super().write(value)
        return res


    def call_method(self):
        print("Dddddddddddddddddddd",self._context)

    def aaaaaaaaaaaaaa(self):
        print ("Ddssssss",self._context)
        if 'AAAA' in self._context:
            context = dict(self.env.context or {})
            context['aaaaa'] = 'aa'
            return {
                'type': 'ir.actions.act_window',
                'name': _('pp'),
                'res_model': 'res.partner',
                'view_type': 'list',
                'view_mode': 'list',
                'context':context,
                'views': [[False, 'list'], [False, 'form']],
            }

# Classical Inheritance
class SaleOrder(models. Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one(
        'res.partner', string='Partner', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]",)
    # partner_id = fields.Many2one(string="XYZ")
    sale_order = fields.Char(string="Sale Order")

# Extension Inheritance
# class SaleOrder(models. Model):
#     _name = "sale.order"
#     _inherit = ['mail.thread', 'mail.activity.mixin']

# # Deligation Inheritance
# class ProductProduct(models.Model):
#     _name = "product.product"
#     _description = "Product"
#     _inherits = {'product.template': 'product_tmpl_id'}
