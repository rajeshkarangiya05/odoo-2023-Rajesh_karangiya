from odoo import models, fields
from datetime import datetime,timedelta

class ExpectedReturnDate(models.TransientModel):
    _name = "return.date"

    expiry = fields.Selection(selection=[('5','5'),('10','10'),('15','15')],string='Expected Return Days', required=True)

    def action_confirm(self):
        t = self.env["issue.books"].search([('id','=',self._context["active_id"])])
        u = self.env["register.date"].search([('bookid','=',t.books_lines_ids.ids)])
        print("u",u)
        for res in u:
            res.int_diff = self.expiry
            print("res.int_diff",res.int_diff)
        t.books_lines_ids.return_date = out = datetime.now() + timedelta(days=int(self.expiry))

