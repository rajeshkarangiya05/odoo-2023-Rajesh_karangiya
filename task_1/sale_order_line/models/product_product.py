from odoo import fields,models,api,_

class ProductProduct(models.Model):
	_inherit="product.product"

	def name_get(self):
		res = super(ProductProduct,self).name_get()
		if ('search_default_my_quotation' in self._context or 'default_description_sale'in self._context) and 'active_model' not in self._context :
			result = []
			for rec in self:
				result.append((rec.id,rec.name))
			return result
		else:
			return res