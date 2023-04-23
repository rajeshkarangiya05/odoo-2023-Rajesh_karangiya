from odoo import fields,models

class PaymentType(models.Model):
	_name="payment.type"
	_description="Payment Type"

	name = fields.Char(string="Types of Payment")





