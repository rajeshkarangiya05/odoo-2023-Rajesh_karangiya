{
	"name":"Parking Management",
	"version":"15.0.1.0",
	"category":"Management",
	"license":"LGPL-3",
	"summary":"Parking Management",
	"description":"Parking management app",
	"website":"http://192.46.214.132:8015/web/login",
	"depends":['sale'],
	"data":[
		"security/ir.model.access.csv",
		"data/ticket_sequence.xml",
		"data/mail_template_view.xml",
		"data/admin_mail_template_view.xml",
		"data/action_send_mail.xml",
		"views/parking_user_view.xml",
		"views/parking_data_view.xml",
		"views/payment_type_view.xml",
		"views/vehicle_type_view.xml",
		"views/slot_data_view.xml",
		"views/billing_user_view.xml",
		"views/base_name_view.xml",
		"wizards/choose_vehicle_view.xml",

	],

	'installable': True,
    'application': True,
    'auto_install': False,






}