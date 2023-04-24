# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentStandard(models.Model):
    _name = "student.standard"

    name = fields.Char(string="Name", required=True, help="")
    student_ids =fields.One2many('student.information','standard_id', string="Student")
    number = fields.Integer('Number')

    def name_get(self):
        result = []
        for standard in self:
            name = standard.name + '  [ ' + str(standard.number) + ' ]'
            result.append((standard.id, name))
        return result

    # def read(self, fields=None, load='_classic_read'):
    #     print("\n\n\n self::::::::::::::", self, fields)
    #     return super(StudentStandard, self).read(fields=fields, load=load)

    @api.model
    def create(self, vals):
        print("\n\n\n vals.get('number')", vals.get('number'))
        if vals.get('number') and vals.get('number') < 2:
            raise ValidationError("Please number that is greater than 2!!!")

        res = super(StudentStandard, self).create(vals)
        # student_ls = [{'name': 'Amit', 'roll_no': 7}, {'name': 'Viren', 'roll_no': 1}, {'name': 'Mukund', 'roll_no': 2}]
        vals = {'name': 'Amit', 'roll_no': 7}

        student = self.env['student.information'].create(vals)
        print("\n\n\n\n student", student, res)
        student.standard_id = res.id
        return res

    def read_partner(self):
        print("\n\n call:::::::")
        # professer_id = self.env['professor.record'].browse(3)
        vals = {
            'name' : 'Tiya',
            'roll_no' : 28,
            'phone': 78713484654,
            # 'standard_id': self.id
        }
        self.write({
                'student_ids': [(6, 0, [5, 7, 17])]

            })

        # fields = ['name', 'city']
        # partner_id = self.env['res.partner'].read_group([
        #     ('city', '=', 'Fremont')], fields=['name'], groupby=['city', 'name'], limit=1, lazy=False,)
        # print("\n\n\n partner_id:::::::::::::", partner_id)

    def unlink(self):
        print("\n\n\n\n this method is deleted:::", self)
        res = super(StudentStandard, self).unlink()
        print("\n\n RES::::::::", res)
        return res

    # def write(self, vals):
    #
    #     records = self.env['professor.record'].search([('name', '=', 'Amit'), (), ()])
    #     records_count = self.env['professor.record'].search_count([])
    #     print("\n\n\n records ::::::::::", records)
    #     if 'address' in vals:
    #         raise ValidationError("You cannot change address for this student!")
    #     res = super(StudentInformation, self).write(vals)
    #     return res
    
    # def read_partner(self):
    #     fields = ['name', 'city']
    #     partner_id = self.env['res.partner'].read_group([
    #         ('city', '=', 'Fremont')], fields=['name'], groupby=['city', 'name'], limit=1, lazy=False,)
    #     print("\n\n\n partner_id:::::::::::::", partner_id)