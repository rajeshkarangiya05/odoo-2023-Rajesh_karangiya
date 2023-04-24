# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProfessorRecord(models.Model):
    _name = "professor.record"

    name = fields.Char(string="Name", required=True, help="")
    subject_id = fields.Many2one('student.subject', string='Subject', copy=False)
    student_id = fields.Many2one('student.information', string='Student')
    
    def unlink(self):
        print("\n\n\n\n this method is deleted:::", self)
        res = super(ProfessorRecord, self).unlink()
        print("\n\n RES::::::::", res)
        return res

    def copy(self, default=None):
        print("\n\n self:::::::::::", self)
        default = {
            'name': 'Kinjal'
        }
        # default['name'] = 'Kinjal'
        res = super(ProfessorRecord, self).copy(default=default)
        print("\n\n\n res:::::::::::", res)
        return res