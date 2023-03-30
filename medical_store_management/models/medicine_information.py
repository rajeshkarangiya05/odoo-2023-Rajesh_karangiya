# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from dateutil import relativedelta
from datetime import datetime,date
from odoo.exceptions import ValidationError


class MedicineInformation(models.Model):
    _name="medicine.information"
    _description="medicine"

    batch_no=fields.Char(string="Batch No.",help="", readonly=True)
    name = fields.Char(string="Name of Medicine")
    ref_no = fields.Integer(string="Reference No.")
    company = fields.Char(string="Company name")
    is_major = fields.Boolean(string="Is major?")
    dosage= fields.Selection(selection=[("tablet","tablet"),("capsule","capsule"),("liquid","liquid")], string="Dosage Form")
    mfg_date = fields.Date(String="Manufacturing Date")
    exp_date = fields.Date(string="Expiry Date")
    expiry = fields.Char(string="Expiry month", compute="_compute_expiry_months",store=True)

    @api.model
    def create(self,vals):
        if not vals["exp_date"] or str(vals["exp_date"]) < str(datetime.now().date()):
            raise ValidationError("Enter valid expiry date")
        if not vals.get('batch_no'):
            seq = self.env['ir.sequence'].next_by_code('medicine.information')
            date_three=date.today().strftime("%b")
            vals["batch_no"] = seq[0:4]+date_three+"/"+seq[4:]
        record_exp_data = self.env["medicine.information"].search([("expiry",">","0")])
        print("record_exp_data================>",record_exp_data)
        return super(MedicineInformation,self).create(vals)


    def write(self,vals):
        if not vals["exp_date"] or str(vals["exp_date"]) < str(datetime.now().date()):
            raise ValidationError("Enter valid expiry date")
        res = super(MedicineInformation, self).write(vals)
        return res



    # defining function for header button named "symptoms"
    def action_view_symptoms(self):
        symptoms=self.env['symptoms.data'].search([('medicine_id','=',self.id)])
        action= {
            "type":"ir.actions.act_window",
            "res_model":"symptoms.data",
            "domain":[('medicine_id','=',self.id)],
            "name":("Symptoms"),
            'view_mode':'tree,form'
        }
        if len(symptoms) != 0:
            action.update({
                'views': [[False, "form"]],
                'view_mode': 'form',
                'res_id': symptoms.id,
            })
        return action

    # defining function for smart button named "stock"
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

    # defining compute function
    @api.depends("exp_date")
    def _compute_expiry_months(self):
        for data in self:
            data.expiry=0
            if data.mfg_date:
                month_difference = relativedelta.relativedelta(data.exp_date,data.mfg_date)
                data.expiry=month_difference.months + (month_difference.years*12)
    
    # @api.depends("exp_date")
    # def _set_expiry_date(self):
    #     for rec in self:
    #         if rec.exp_date:
    #             rec.exp_date=True
    #         else:
    #             rec.exp_date=False





