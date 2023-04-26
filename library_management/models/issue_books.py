# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class IssueBooks(models.Model):
	_name="issue.books"
	_description="Issue Book Details"
	_rec_name = "name_id"

	name_id = fields.Many2one("res.partner",string="Name", required=True)
	email = fields.Char(string="Email")
	phone = fields.Char(string="Phone No.")
	address = fields.Text(string="Address",)
	empty = fields.Char(string="Empty")
	issue_date = fields.Date(string="Issue Date")
	books_lines_ids = fields.One2many("register.books","empty_id",string="Books details")
	relation_ids = fields.One2many("register.date","built_relation_id",string="Relatoinal")
	state = fields.Selection(selection=[('draft', 'Draft'),
		('issued', 'Issued'),('return','Return')],
		 string='Status', required=True, readonly=True, copy=False, default='draft')
	book_name = fields.Many2one("book.details",string="Book Name")
	quantity = fields.Integer(string="Quantity")
	user_send_email = fields.Char(string="Send Mail To")
	check_box = fields.Boolean("Manual Entry")
	payable = fields.Integer("Payable",compute="compute_payable_charge")
	
			
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
		for rec in self:
			rec.write({'state': "issued"})
			self.issue_date = datetime.now().date()
			for data in self.books_lines_ids:
				quantity = data.issued_quantity
				register_book_data = self.env["register.books"].search([('id','=',data.id)])
				register_book_data.issue_bookline_ids=self.id
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

	#defining method for getting total charges per user
	def compute_payable_charge(self):
		for data in self:
			data.payable=0
			if data.issue_date:
				payable_data = self.env["register.date"].search([('issue_book_id','=',data.id)])
				for element in payable_data:
					data.payable += element.total_charge


	# defining method for return button
	def return_view(self):
		new_list=[]
		for rec in self.books_lines_ids:
			new_list.append((0,0,{'book_id':rec.book_name_id.id,'quantity':rec.issued_quantity,'return_quantity':rec.issued_quantity}))
		return {
			"type":"ir.actions.act_window",
			"name":"Return Book",
			"res_model":"return.book",
			"view_mode":"form",
			"target":"new",
			"context": {
				"default_books_return_ids": new_list
			}

		}


	# defining method for button "user data" to get details of user from res partner model
	def return_users(self):
		fields = ['name', 'email']
		partner_id = self.env['book.details'].search_count([])



	# defining unlink method for delecting records from registor book model
	def unlink(self):
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
					
					update={
						"issued_quantity":lines.issued_quantity+self.quantity
					}
					self.write({
						"books_lines_ids":[(1,lines.id,update)]
						})
		self.quantity=None
		self.book_name =None
				


	# defining method for button "DeleteDummys" deleting records in register books model
	def Delete_given_data(self):
		pass

	def return_book(self):
		pass

	#method for defining constrain on book lines 
	@api.constrains('books_lines_ids')
	def _check_books_lines_ids(self):
		for rec in self.books_lines_ids:
			count = self.env["register.books"].search_count([('empty_id','=',self.id),
				('book_name_id','=',rec.book_name_id.id)])
			if count > 1:
				raise ValidationError('Same book lines are added')
	

		
	
