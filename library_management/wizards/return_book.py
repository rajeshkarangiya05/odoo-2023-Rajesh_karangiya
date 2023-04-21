from odoo import fields,models,api,_
from datetime import datetime

class ReturnBook(models.TransientModel):
	_name="return.book"
	_description = "Return Book wizard"

	reture_book = fields.Boolean(string="Return Individual Book")
	books_return_ids = fields.Many2many("register.date","book_return",string="Select Books", readonly=True)

	# defining method for Return All
	def action_confirm(self):
		for rec in self:
			records = self.env["issue.books"].search([('id','=',self._context["active_id"])])
			vals = {
				"state":"return"
			}
			records.write(vals)
			returnData = self.env["register.date"].search([('issue_book_id','=',records.id)])
			for res in returnData:
				res.incoming_date = datetime.now().date()



