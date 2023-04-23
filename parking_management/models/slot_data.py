from odoo import fields,models

class SlotData(models.Model):
	_name="slot.data"
	_description="Slot Data"


	base_name_id = fields.Many2one("base.name",string="Base")
	section_name = fields.Char(string="Section name")
	section_partition = fields.Char("Total Section Partition")
	vehicel_type_id = fields.Many2one("vehicel.type",string=" Choose Vehicle Type")
	strength = fields.Integer("Available Slot")
	booked = fields.Integer("Booked Slot")
	token_user = fields.Char("Token of User")

	#method name_get for slot to user
	def name_get(self):
		res = []
		for rec in self:
			slots = "Base "+rec.base_name_id.name+" Section "+rec.section_name+" partition "+rec.section_partition
			res.append((rec.id,slots))
		return res


