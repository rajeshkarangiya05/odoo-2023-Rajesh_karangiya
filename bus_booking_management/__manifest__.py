{
	"name":'Bus Booking',
	"description":"Bus Booking",
	"category":"Management",
	"license":"LGPL-3",
	"depends":['base_address_city'],
	"data":[
		"security/ir.model.access.csv",
		"data/action_copy_data.xml",
		"views/bus_data_view.xml",
		"views/user_bus_booking_view.xml",
		"views/bus_management_view.xml",

	],
	"installable":True,
	"application":True,
	"auto_install":True,
}