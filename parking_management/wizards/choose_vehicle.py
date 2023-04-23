from odoo import models, fields

class ChooseVehicle(models.TransientModel):
    _name = "choose.vehicle"
    _rec_name="choose_vehicle"

    choose_vehicle = fields.Many2one("vehicel.type",string="Choose Vehicle Type")
    Alot_slot = fields.Integer("Alot Slot Quantity")

    def action_alot(self):
        records = self.env["base.name"].search([('id','=',self._context["active_id"])])
        add_data = self.env["slot.data"].search([('base_name_id','=',records.ids)])
        for res in add_data:
            res.vehicel_type_id = self.choose_vehicle
            res.strength = self.Alot_slot
