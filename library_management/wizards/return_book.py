from odoo import fields,models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError
class ReturnBook(models.TransientModel):
	_name="return.book"
	_description = "Return Book wizard"

	reture_book = fields.Boolean(string="Return Individual Book")
	books_return_ids = fields.One2many("register.data.lines",'relation_id',string="Select Books")

	# defining method for Return All
	def action_confirm(self):
		for rec in self:
			records = self.env["issue.books"].search([('id','=',self._context["active_id"])])
			vals = {
				"state":"return"
			}

			for data in rec.books_return_ids:
				if data.return_quantity > data.quantity:
					raise ValidationError('Return Quantity is more than Book Quantity')
				else:
					loop_variable = data.quantity - data.return_quantity
					print('loop_variable',loop_variable)
					register_incoming_date = self.env['register.date'].search([('issue_book_id','=',self._context['active_id']),
						('incoming_date','=',False),
						('books_id_name','=',data.book_id.id)])
					print("register_incoming_date",register_incoming_date)
					for index in range(loop_variable):
						register_incoming_date[index].incoming_date = datetime.now().date()


			
			returnData = self.env["register.date"].search([('issue_book_id','=',self._context["active_id"])])
			count = self.env["register.date"].search_count([('issue_book_id','=',records.id)])
						
			new_list=[]
			for res in returnData:
				# res.incoming_date = datetime.now().date()
				if res.incoming_date:
					new_list.append(True)
				else:
					new_list.append(False)
			if all(new_list):
				records.write(vals)
			


	# method to fill lines of register_book	model	
	# @api.onchange("reture_book")
	# def add_data(self):
	# 	print("in***********")
	# 	for rec in self:
	# 		print("check *******")
	# 		data = self.env["register.books"].search([('issue_bookline_ids','=',self._context["active_id"])])
	# 		print("\n\n data",data)
	# 		for dat in data:
	# 			vals={
	# 				'book_id':dat.book_name_id.id,
	# 				'quantity':dat.issued_quantity
	# 			}
	# 			self.write({
	# 				"books_return_ids":[(0,0,vals)]
	# 				})





class RegisterDateLines(models.TransientModel):
	_name="register.data.lines"
	_description="Register Date Data"

	relation_id = fields.Many2one("return.book")
	book_id =  fields.Many2one("book.details")
	quantity =  fields.Integer("Book Quantity")
	return_quantity = fields.Integer("Return Quantity")

	# def default_get(self,fields):
	# 	res = super(RegisterDateLines, self).default_get(fields)
	# 	data = self.env["register.books"].search([('issue_bookline_ids','=',self._context["active_id"])])
	# 	print("data ------",data)
	# 	if 'return_quantity' in fields:
	# 		for element in data:
	# 			print("element quantity -----",element.issued_quantity)
	# 			res['return_quantity']=element.issued_quantity
	# 	return res




	






