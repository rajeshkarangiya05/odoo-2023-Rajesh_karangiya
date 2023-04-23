from odoo import fields,models,api,_

class BaseName(models.Model):
	_name="base.name"
	_description="Base name"


	name = fields.Char(string="Base Name", required=True)
	choose_sections = fields.Integer(string="Total Sections")
	choose_partition = fields.Integer(string="Total Rows per Section")
	slot_data_ids = fields.One2many("slot.data","base_name_id",string="Slot Data")
	state = fields.Selection(selection=[('step_1','STEP 1'),
		('step_2','STEP 2')],string='Status',required=True, readonly=True,
		 copy=False, default='step_1')
	confirmation = fields.Boolean(string="Confirm to add the data in Base")

	# method to add lines in slot data model
	@api.onchange("confirmation")
	def adding_row_slot_data(self):
		for element in self:
			if element.choose_sections and element.choose_partition:
				sec_num = 1
				par_num = 1
				for _ in range(element.choose_sections):
					for _ in range(element.choose_partition):
						vals={
							"section_name":"SEC%s"% sec_num,
							"section_partition":f"P-S-SEC{sec_num}-{par_num}"
						}

						self.write({
								"slot_data_ids":[(0,0,vals)]
							})
						par_num+=1
						
					sec_num+=1
					par_num = 1
						
						
	# methos for "NEXT" button
	def action_step_1(self):
		for rec in self:
			rec.write({'state': "step_2"})
		return {
			"type":"ir.actions.act_window",
			"name":"Choose Vehicle and Add slots",
			"res_model":"choose.vehicle",
			"view_mode":"form",
			"target":"new",

		}

	# method to delect lines of base_name and slot_data linked
	def unlink(self):
		for lines in self.slot_data_ids:
			record = self.env["slot.data"].search([('id','=',lines.id)])
			record.unlink()
		return super(BaseName,self).unlink()



	
	
