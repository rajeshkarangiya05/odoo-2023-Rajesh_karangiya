{
	"name":"Sale order line",
	"description":"Sale order inhert",
	"version":"15.0.0",
	"category":'sales',
	'depends':['sale'],
	"data":[
		"views/sale_order_line_view.xml",
		"views/stock_move_view.xml",
		"views/account_move_view.xml",
	],
	"installable":True,
	"application":True,
	'auto_install':False,
}