# -*- coding: utf-8 -*-

from odoo import fields, models,api,_
from datetime import datetime,date

class BookDetails(models.Model):
	_name="book.details"
	_description="Books details"
	_rec_name="book_name"

	name_id = fields.Many2one("book.author",string="Author name")
	book_name = fields.Char(string="Book name")
	price = fields.Integer(string="Price")
	pages = fields.Integer(string="Pages")
	book_id = fields.Char(string="BooK ID", readonly="True")
	quantity = fields.Integer(string="Quantity")
	stock_quantity = fields.Integer(string="Stock Quantity",compute="_compute_stock_quantity")
	book_types_ids = fields.Many2many("book.type", "book_type_id", string="Book Types")
	charges = fields.Integer(string="Return charges")
	

	# defining sequence for book id
	@api.model
	def create(self,vals):
		if not vals.get('book_id'):
			seq = self.env['ir.sequence'].next_by_code('book.details')
			date_three=date.today().strftime("%b")
			vals["book_id"] = seq[0:3]+date_three.upper()+"/"+seq[3:]
		return super(BookAuthor,self).create(vals)

	# write name get method for book name
	def name_get(self):
		result=[]
		for element in self:
			medicine = element.book_name +" ["+ element.book_id + "] " + " [" + element.name_id.name +"] "
			result.append((element.id,medicine))
		return result

	#write name search method for book name
	@api.model
	def _name_search(self, name, args=None, operator="ilike", limit=100, name_get_uid=None):
		args=args or []
		if name:
			args = ['|','|',('book_id',operator,name),('book_name',operator,name),("name_id",operator,name)] + args
		return self._search(args, limit=limit, access_rights_uid=name_get_uid)

	# define function for smart button of "Quantity"
	def action_book_quantity(self):
		pass
		

	#defining method for smart button name quantity
	def _compute_stock_quantity(self):
		t = self.env["register.date"].search_count([('books_id_name','=',self.id), ('incoming_date','=',False)])
		self.stock_quantity = self.quantity - t
		

	

