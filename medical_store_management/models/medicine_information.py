# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from dateutil import relativedelta
from datetime import datetime,date
from odoo.exceptions import ValidationError


class MedicineInformation(models.Model):
    _name="medicine.information"
    _description="medicine"

    batch_no=fields.Char(string="Batch No.",help="", readonly=True)
    name = fields.Char(string="Name of Medicine", required=True)
    ref_no = fields.Integer(string="Reference No.")
    company = fields.Char(string="Company name")
    is_major = fields.Boolean(string="Is major?")
    dosage= fields.Selection(selection=[("tablet","tablet"),("capsule","capsule"),("liquid","liquid")], string="Dosage Form")
    mfg_date = fields.Date(String="Manufacturing Date")
    exp_date = fields.Date(string="Expiry Date")
    expiry = fields.Integer(string="Expiry month", compute="_compute_expiry_months",store=True)
    
    # create method for expiry date and batch number
    @api.model
    def create(self,vals):
        count = 0
        if not vals["exp_date"] :
            raise ValidationError("Enter valid expiry date")
        if not vals.get('batch_no'):
            seq = self.env['ir.sequence'].next_by_code('medicine.information')
            print("==================>", seq)
            date_three=date.today().strftime("%b")
            number= self.env["ir.sequence.date_range"].search([('id','=','43')])
            print("**************",number.date_to)
            input_dt = datetime.now()
            last_month_date = input_dt + relativedelta.relativedelta(day=31)
            print(last_month_date)
            first_month_date = input_dt + relativedelta.relativedelta(day=1)
            print("first",first_month_date)
            number.date_from = first_month_date
            number.date_to = last_month_date
            # rrr = [{
            #     "date_to":last_month_date
            # }]
            # t = self.env["ir.sequence.date_range"].write(rrr)
            # print("tttttttttttttt",t)

            vals["batch_no"] = seq[0:4]+date_three+"/"+seq[4:]
            print("\n\n\n\n\n",vals)
            # print("seq ======>",number._create_date_range_seq.date_to)
        return super(MedicineInformation,self).create(vals)


    # write method for validating for expiry date
    def write(self,vals):
        if not vals["exp_date"] or str(vals["exp_date"]) < str(datetime.now().date()):
            raise ValidationError("Enter valid expiry date")
        res = super(MedicineInformation, self).write(vals)
        return res

    # write default method to give default comapany name
    @api.model
    def default_get(self,fields):
        res = super(MedicineInformation, self).default_get(fields)
        if 'company' in fields:
            res['company'] = "Zydus Limited"
        return res

    # write name_get method to get name and expiry date in drop down
    def name_get(self):
        result=[]
        for element in self:
            medicine = element.name +" ["+ str(element.exp_date)+"]"
            result.append((element.id,medicine))
        return result

    # write name_search method to search medicine by its name or reference no or expiry date

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=100, name_get_uid=None):
        args=args or []
        if name:
            args = ['|','|',('name',operator,name),('ref_no',operator,name),("exp_date",operator,name)] + args
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)




    # defining function for smart button named "symptoms"
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
                'views': [[False, "tree"], [False, "form"]],
                'view_mode': 'tree, form',
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

    # defining compute function for expiry month
    @api.depends("exp_date")
    def _compute_expiry_months(self):
        for data in self:
            data.expiry=0
            if data.mfg_date:
                month_difference = relativedelta.relativedelta(data.exp_date,data.mfg_date)
                data.expiry=month_difference.months + (month_difference.years*12)





