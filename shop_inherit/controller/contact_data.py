from odoo import fields,models, http, tools
from odoo.http import request

class ContactData(http.Controller):

	@http.route(['/contact'], type="http", auth="public", website=True, sitemap=True, method=['get'])
	def contact_data(self,**post):

		data = request.env["res.partner"].search([])
		vals ={
			"record":data,
		}
		return request.render('shop_inherit.Contact_data',vals)


