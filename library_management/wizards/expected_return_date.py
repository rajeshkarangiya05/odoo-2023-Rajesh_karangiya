from odoo import models, fields
from datetime import datetime,timedelta

class ExpectedReturnDate(models.TransientModel):
	_name = "return.date"

	expiry = fields.Selection(selection=[('5','5'),('10','10'),('15','15')],string='Expected Return Days', required=True)

	def action_confirm(self):
		records = self.env["issue.books"].search([('id','=',self._context["active_id"])])
		intDiff = self.env["register.date"].search([('bookid','=',records.books_lines_ids.ids)])
		for res in intDiff:
			res.int_diff = self.expiry
		records.books_lines_ids.return_date = datetime.now() + timedelta(days=int(self.expiry))
		records.write({'state': "issued"})

