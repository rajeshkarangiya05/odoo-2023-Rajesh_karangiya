{
	"name":"Sale order rajesh",
	"description":"Sale order inhert",
	"version":"15.0.0",
	"category":'sales',
	'depends':['sale','contacts','product','website'],
	"data":[
		"security/ir.model.access.csv",
		"data/action_merge_quotation.xml",
		"data/action_split_delivery.xml",
		# "views/sale_name_change_view.xml",
		"views/product_product_inherit_view.xml",
		"views/main_view.xml",
		"wizards/split_delivery_wizard_view.xml",

	],
	"assets":{
		'web.assets_frontend':[
			"sale_order_inherit/static/js/test.js",
			"sale_order_inherit/static/scss/portal.scss"
		]
	},
	"installable":True,
	"application":True,
	'auto_install':False,


}