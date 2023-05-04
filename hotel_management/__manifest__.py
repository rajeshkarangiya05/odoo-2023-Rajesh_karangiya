{
	"name":"Hotel Management",
	"version":"15.0.1.0",
	"category":"Management",
	"description":"Hotel Management App",
	"summary":"Hotel Management app for easy booking of hotel room instantly",
	"website":"https://www.aktivsoftware.com",
	"license":"LGPL-3",
	"depends":['mail'],
	"data":[
		"security/ir.model.access.csv",
		"data/ir_sequence_room_id.xml",
		"data/action_send_mail_checkout.xml",
		"data/action_send_mail_checkout_template.xml",
		"data/user_mail_template_view.xml",
		"data/cancel_booking_mail_template.xml",
		"views/hotel_management_view.xml",
		"views/hotel_room_view.xml",
		"views/hotel_room_booking_lines_view.xml",
		"views/hotel_room_booking_view.xml",
		"wizard/cancel_booking_view.xml"

	],
	"installable":True,
	"application":True,
	"auto_install":False,
}