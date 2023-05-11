from odoo import fields,http
from odoo.http import request

class ResData(http.Controller):
	@http.route(['/res'],type='http', auth='public', website=True, sitemap=False)
	def res_data(self,**post):
		return request.render('sale_order_inherit.main_template')

	@http.route(['/res/submit'],type='http',auth='public', website=True, sitemap=False)
	def submit_data(self,**post):

		vals={

			"name":post.get('name')
		}
		request.env["res.partner"].create(vals)
		return request.render('sale_order_inherit.submit_template')
