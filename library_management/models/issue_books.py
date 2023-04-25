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
	book_name = fields.Many2one("book.details",string="Book Name")
	quantity = fields.Integer(string="Quantity")
	user_send_email = fields.Char(string="Send Mail To")
	check_box = fields.Boolean("Manual Entry")
	payable = fields.Integer("Payable")
	
			
	# defining method for automatic filling the fields 
	#email, phone, adress by choosing name_id field
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
					data.address = res_data.street+"\n"+(res_data.zip)+"\n"+(res_data.city)
				else:
					data.address = (res_data.street)+"\n"+(res_data.street2)+"\n"+(res_data.zip)+"\n"+(res_data.city)

	# defining method for issue button
	def issue_view(self):
		print(" ******************self.browse ",self.browse())
		for rec in self:
			rec.write({'state': "issued"})
			self.issue_date = datetime.now().date()
			for data in self.books_lines_ids:
				quantity = data.issued_quantity
				for _ in range(quantity):					
					register_id = [{"bookid":data.id,
					'issue_book_id':self.id,
					'outgoing_date':self.issue_date,
					'user_id':self.name_id.id,
					'books_id_name':data.book_name_id}]
					issueData = self.env["register.date"].create(register_id)
		template = self.env.ref('library_management.user_mail_id').id	
		template_id = self.env['mail.template'].browse(template)
		template_id.send_mail(self.id, force_send=True)
		return {
			"type":"ir.actions.act_window",
			"name":"_(Return Date)",
			"res_model":"return.date",
			"view_mode":"form",
			"target":"new",
		}
		

	# defining method for return button
	def return_view(self):
		for rec in self:
			rec.write({'state': "return"})
			for data in self.books_lines_ids:
				returnData = self.env["register.date"].search([('bookid','=',data.id)])
				returnData.incoming_date = datetime.now().date()


	# defining method for button "user data" to get details of user from res partner model
	def return_users(self):
		fields = ['name', 'email']
		partner_id = self.env['book.details'].search_count([])
		
		print('\n\npartner_id',type(partner_id))	



	# defining unlink method for delecting records from registor book model
	def unlink(self):
		print("calling unlink method::::::::::",self)
		# print(self.books_lines_ids.id)
		for lines in self.books_lines_ids:
			record = self.env["register.books"].search([('id','=',lines.id)])
			record.unlink()
		return super(IssueBooks,self).unlink()

	# defining method for button "CreateDummyBook" adding new book in register books model
	def add_new_data(self):
		for element in self.books_lines_ids:
				register_book_data = self.env["register.books"].search([("id","=",element.id)])
				register_book_data.issue_bookline_ids = element.id

		record_book = self.env["book.details"].search([('id','=',self.book_name.id)])
		vals= {
			"book_name_id": self.book_name.id,
			"issued_quantity":self.quantity,
			"book_data_ids":[(6,0, record_book.book_types_ids.ids)]
		}
		
		if not self.books_lines_ids  or self.book_name.id not  in self.books_lines_ids.book_name_id.ids:
			self.write({
							"books_lines_ids":[(0,0, vals)]
						})
		else:
			for lines in self.books_lines_ids:
				record_register_book = self.env["register.books"].search([('id','=',lines.id)])
				if record_book.id == lines.book_name_id.id and lines.id == record_register_book.issue_bookline_ids:
					print("\n *same record")
					update={
						"issued_quantity":lines.issued_quantity+self.quantity
					}
					self.write({
						"books_lines_ids":[(1,lines.id,update)]
						})
				


	# defining method for button "DeleteDummys" deleting records in register books model
	def Delete_given_data(self):
		pass
		





