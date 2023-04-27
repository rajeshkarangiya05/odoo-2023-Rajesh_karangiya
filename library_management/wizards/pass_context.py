from odoo import fields,models,api,_

class PassContext(models.TransientModel):
	_name="pass.context"
	_description="Pass context"

	nationality_id = fields.Many2one("issue.books",string="Nationality")
	first_name = fields.Char("First Name")
	middle_name = fields.Char("Middle Name")
	last_name= fields.Char("Last Name")


