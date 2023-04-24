from odoo import models, fields



class LeaveSchool(models.TransientModel):
    _name = "leave.school"

    reason = fields.Char('Reason For leaving School')
    # student_id = fields.Many2one('student.information', 'Student')

    def action_confirm(self):
        print("\n\n\n action_confirm called", self, self._context)
        if self._context.get('active_id', False):
            student = self.env['student.information'].browse(self._context.get('active_id'))
            if student:
                student.reason = self.reason