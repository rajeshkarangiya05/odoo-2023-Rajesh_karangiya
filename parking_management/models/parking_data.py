from odoo import fields,models,api

class ParkingData(models.Model):
	_name="parking.data"
	_description="Data"


	
	entry=fields.Char(string="Entry ticket Number", readonly=True)
	epmty2_id=fields.Many2one("token.data", string="Empty")

	@api.model
	def create(self,vals):
		if not vals.get("entry"):
			vals["entry"] = self.env["ir.sequence"].next_by_code("parking.data")
		result = super(ParkingData, self).create(vals)
		return result


