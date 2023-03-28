# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from dateutil import relativedelta
from datetime import datetime

class MedicineInformation(models.Model):
    _name="medicine.information"
    _description="medicine"

    name = fields.Char(string="Name of Medicine", required=True)
    ref_no = fields.Integer(string="Reference No.")
    company = fields.Char(string="Company name")
    is_major = fields.Boolean(string="Is major?")
    dosage= fields.Selection(selection=[("tablet","tablet"),("capsule","capsule"),("liquid","liquid")], string="Dosage Form")
    mfg_date = fields.Date(String="Manufacturing Date")
    exp_date = fields.Date(string="Expiry Date")
    expiry = fields.Char(string="Expiry month", compute="_compute_expiry_months")

    def action_view_symptoms(self):
        symptoms=self.env['symptoms.data'].search([('medicine_id','=',self.id)])
        action={
            "type":"ir.actions.act_window",
            "res_model":"symptoms.data",
            "domain":[('medicine_id','=',self.id)],
            "name":("Symptoms"),
            'view_mode':'tree,form'
        }
        if len(symptoms) == 1:
            action.update({
                'views': [[False, "tree"]],
                'view_mode': 'tree',
                'res_id': symptoms[0].id,
            })
        else:
            action.update({
                'views': [[False, "tree"], [False, "form"]],
                'view_mode': 'tree, form',
            })
        return action

    def action_view_stock(self):
        stock=self.env['medicine.stock'].search([('name_id','=',self.id)])
        action={
            "type":"ir.actions.act_window",
            "res_model":"medicine.stock",
            "domain":[('name_id','=',self.id)],
            "name":("Stocks"),
            'view_mode':'tree,form'
        }
        if len(stock) == 1:
            action.update({
                'views': [[False, "form"]],
                'view_mode': 'form',
                'res_id': stock[0].id,
            })
        else:
            action.update({
                'views': [[False, "tree"], [False, "form"]],
                'view_mode': 'tree, form',
            })
        return action

    @api.depends("exp_date")

    def _compute_expiry_months(self):
        print(self)
        for data in self:
            data.expiry=0
            if data.mfg_date:
                print("-...................................................................")
                print(data.mfg_date)
                print(data.exp_date)
                month_difference = relativedelta.relativedelta(data.exp_date,data.mfg_date)
                data.expiry=month_difference.months




