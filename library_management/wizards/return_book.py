from odoo import fields,models,api,_
from datetime import datetime

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
	@api.onchange("books_return_ids"):
	def _onchange_books_return_ids(self):
		for data in self.books_lines_ids:
			


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
	book_id =  fields.Many2one("book.details",readonly=True)
	quantity =  fields.Integer("Book Quantity",readonly=True)
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




	






