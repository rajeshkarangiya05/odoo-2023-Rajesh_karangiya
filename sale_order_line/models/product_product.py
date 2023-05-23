from odoo import fields,models,api,_

class ProductProduct(models.Model):
	_inherit="product.product"


	def name_get(self):
		res = super(ProductProduct,self).name_get()
		result =[]
		if self:
			for product in self:
				name = product.name
				result.append((product.id, name))
			return result
		return res
