from odoo import models, fields



class ExpectedReturnDate(models.TransientModel):
    _name = "return.date"

    expiry = fields.Date('Expected Return Date', required=True)

    def action_confirm(self):
        print("\n\n\n", self._context["active_id"])
        t = self.env["issue.books"].search([('id','=',self._context["active_id"])])
        t.books_lines_ids.return_date = self.expiry

