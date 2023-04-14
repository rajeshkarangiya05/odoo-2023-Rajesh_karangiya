from odoo import models, fields
from datetime import datetime,timedelta

class ExpectedReturnDate(models.TransientModel):
    _name = "return.date"

    expiry = fields.Selection(selection=[('5','5'),('10','10'),('15','15')],string='Expected Return Days', required=True)

    def action_confirm(self):
        print("\n\n\n", self._context["active_id"])
        t = self.env["issue.books"].search([('id','=',self._context["active_id"])])
        u = self.env["register.date"].search([('user_id','=',t.name_id.id)])
        for res in u:
            res.int_diff = self.expiry
        t.books_lines_ids.return_date = out = datetime.now() + timedelta(days=int(self.expiry))

