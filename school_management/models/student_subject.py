# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class StudentSubject(models.Model):
    _name = "student.subject"

    name = fields.Char(string="Name", required=True, help="")

    
    _sql_constraints = [
        ('uniqe_sub_nme', 'unique (name)', """Only one value can be defined for each given usage!"""),
    ]
    def action_view_professor(self):
        print("\n\n\n self", self, self.id,self.name)
        professer = self.env['professor.record'].search(
            [('subject_id', '=', self.id)])
        action =  {
            "type": "ir.actions.act_window",
            "res_model": "professor.record",
            "domain": [('subject_id', '=', self.id)],
            "name": _("Professor"),
            'view_mode': 'tree,form'
        }
        if len(professer) == 1:
            action.update({
                'views': [[False, "form"]],
                'view_mode': 'form',
                'res_id': professer[0].id,
            })
        else:
            action.update({
                'views': [[False, "tree"], [False, "form"]],
                'view_mode': 'tree, form',
            })
        return action