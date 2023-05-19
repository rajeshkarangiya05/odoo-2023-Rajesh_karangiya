{
	
	"name":"Bulk Order",
	"license":"LGPL-3",
	"category":"Sales Bulk Order",
	"summary":"Sales Bulk Order",
	"description":"Sales Bulk Order",
	"depends":['sale','product'],
	"data":[
		"security/ir.model.access.csv",
		"views/sale_view_inherit_view.xml",
		"views/sale_bulk_product_view.xml",
		
	],
	"installable":True,
	"application":True,
	"auto_install":False,
}