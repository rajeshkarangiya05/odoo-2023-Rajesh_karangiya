{
	
	"name":"Shop Inherit",
	"license":"LGPL-3",
	"category":"Inherit",
	"summary":"Shop Inherit",
	"description":"Shop Inherit",
	"depends":['website_sale','sale','product'],
	"data":[
		"views/add_menu_contact.xml",
		"views/contact_data_template.xml",
		"views/product_description_view.xml",
		"views/product_description_template.xml",

	],

	"assets":{

		'web.assets_frontend':[
			"shop_inherit/static/scss/contact_data.scss"
		]
	},
	"installable":True,
	"application":True,
	"auto_install":False,
}