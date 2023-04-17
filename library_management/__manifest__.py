{
	

	"name":"Library Management",
	"version":"15.0.0.0",
	"summary":"Library Management",
	"description":"Library Management",
	"category":"Management",
	"website":"https://www.aktivsoftware.com",
	"license": "LGPL-3",
	"depends":["mail"],
	"data":[
		"security/ir.model.access.csv",
		"data/ir_sequence_book_id.xml",
		"data/mail_template_view.xml",
		"views/issue_books_view.xml",
		"views/book_author_view.xml",
		"views/books_details_view.xml",
		"views/register_books_view.xml",
		"views/register_date_view.xml",
		"views/book_type_view.xml",
		"wizards/expected_return_date_view.xml",





	],
	"installable":True,
	"application":True,
	"auto_install":False,

}