# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import datetime

class IssueBooks(models.Model):
	_name="issue.books"
	_description="Issue Book Details"
	_rec_name = "name_id"

	name_id = fields.Many2one("res.partner",string="Name")
	email = fields.Char(string="Email")
	phone = fields.Char(string="Phone No.")
	address = fields.Text(string="Address",)
	empty = fields.Char(string="Empty")
	issue_date = fields.Date(string="Issue Date")
	books_lines_ids = fields.One2many("register.books","empty_id",string="Books details")
	state = fields.Selection(selection=[('draft', 'Draft'),
		('issued', 'Issued'),('return','Return')],
		 string='Status', required=True, readonly=True, copy=False, default='draft')
			

	@api.onchange("name_id")
	def _onchange_default_value(self):
		for data in self:
			data.email = ""
			if data.name_id:
				compare_id = data.name_id.id
				res_data = self.env["res.partner"].search([('id','=',compare_id)])
				data.email = res_data.email
				data.phone = res_data.phone
				if not res_data.street2:
					data.address = str(res_data.street)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)
				else:
					data.address = str(res_data.street)+"\n"+str(res_data.street2)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)

	def issue_view(self):
		for rec in self:
			rec.write({'state': "issued"})
			print(self.books_lines_ids)
			self.issue_date = datetime.now().date()
			for data in self.books_lines_ids:
				print("data",data.id)
				print("quantity =====>", data.issued_quantity)
				quantity = data.issued_quantity
				for _ in range(quantity):					
					register_id = [{"bookid":data.id,
					'outgoing_date':self.issue_date,
					'user_id':self.name_id.id,
					'books_id_name':data.book_name_id}]
					issueData = self.env["register.date"].create(register_id)

	def return_view(self):
		for rec in self:
			rec.write({'state': "return"})
			for data in self.books_lines_ids:
				returnData = self.env["register.date"].search([('bookid','=',data.id)])
				returnData.incoming_date = datetime.now().date()



	def return_users(self):
		fields = ['name', 'email']
		partner_id = self.env['res.partner'].read_group([('id','>',10)], fields=fields, groupby=['email'], lazy=False)
		print("read =============>",partner_id)