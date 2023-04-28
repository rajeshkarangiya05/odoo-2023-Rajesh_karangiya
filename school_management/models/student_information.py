from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError



class StudentInformation(models.Model):
    _name = "student.information"

    name = fields.Char(string="Name", help="", readonly=True, copy=False)
    roll_no = fields.Integer(string="Roll No.")
    birth_date = fields.Date(string="Birth Date")
    height = fields.Float(string="Height")
    standard_id = fields.Many2one('student.standard', string="Standard")
    is_use_transportation = fields.Boolean(string="Is use transportation?")
    image = fields.Binary(string="Image")
    address = fields.Text(string="Address")
    student_subject_ids = fields.Many2many('student.subject',
                                            'student_subject_id', string="Subject")
    # student_subject_ids = fields.Many2many(
    #     'student.subject', 'student_subject_id', string="Subject", required=True,
    #     default=lambda self: self.env['student.subject'].search([('name', '=', 'Python')]).ids)
    age = fields.Integer(string="Age", compute="_compute_age_calculation")
    birth_date_day = fields.Char(string="Birth Day", compute="_compute_age_calculation")
    numbers = fields.Integer()
    phone = fields.Char('Phone Number')
    is_visible = fields.Boolean(string="Is visible")
    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], string="Gender")
    reason = fields.Char('Reason FOr leaving School')
    stu_email = fields.Char('Email')

    
    _sql_constraints = [
        ('uniqe_roll_no', 'unique (roll_no)', """Only one value can be defined for each given usage!"""),
    ]
    # _sql_constraints =[('uniqe_roll_no','unique (phone)',"""Roll Numbers is already exists""")]
    
    @api.model
    def create(self, vals):
        vals['numbers'] = 5
        vals['height'] = 15.5
        subjects= self.env['student.subject'].search([],limit=2).ids
        # [(4, group.id, False) for group in all_groups]})
        vals.update({
            # 'student_subject_ids': [(4, subject) for subject in subjects]
            # 'student_subject_ids': [(5, 0, 0)]
            'student_subject_ids': [(6,0, subjects)]
        })
        print('\nvals--------------------',vals)
        return super(StudentInformation, self).create(vals)

    @api.model
    def default_get(self, fields):
        print("\n\n\n default_get", fields)
        res = super(StudentInformation, self).default_get(fields)
        print("\n\n")
        print("res----------------",res)
        if 'height' in fields:
            res['height'] = 10
        print("\n\n")
        print("res ,, --------------------", res)    
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


    @api.onchange('student_subject_ids')
    def onchange_student_subject_ids(self):
        if not self.student_subject_ids:
            return
        self.roll_no = self.numbers
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    @api.depends("birth_date")
    def _compute_age_calculation(self):
        for rec in self:
            rec.age = 0
            if rec.birth_date:
                today_date = date.today()
                if rec.birth_date.month <= today_date.month and rec.birth_date.day <= today_date.day:
                    rec.age = today_date.year - rec.birth_date.year
                else:
                    rec.age = (today_date.year - rec.birth_date.year) - 1

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        print("\n\n\n name", name, args, operator, limit, name_get_uid)
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            args = ['|', ('name', operator, name), ('phone', operator, name)] + args
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    @api.constrains('roll_no')
    def check_roll_no(self):
        for record in self:
            if record.roll_no <= 0 :
                raise ValidationError('Invalid Roll Numbers')    



    def action_leave_school(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "leave.school",
            "name": _("Leave"),
            'view_mode': 'form',
            'target': 'new',
            # 'context': {
            #     'default_student_id': self.id,
            #     # 'default_reason': 'abc'
            # }
        }

    def email_send(self):
        template = self.env.ref('school_management.student_mail_id').id
        template_id = self.env['mail.template'].browse(template)
        template_id.send_mail(self.id, force_send=True)

