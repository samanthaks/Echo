from CBSLogin import CBSLogin

def cbslogin_test():
	print("Testing CBSLogin...")
	print("Please input credentials:")
	username = input("Username:")
	password = input("Password:")
	cbslogin_mba_test(username, password)
	cbslogin_emba_test(username, password)
	print("All tests passed!")


def cbslogin_mba_test(username, password):
	print("Testing Login and retrieve MBA info...")
	a = CBSLogin(username, password)
	assert(a.getInfo('CBartlett18') == ('Clay Everett Bartlett', "MBA '18", 'Fall 2016', 'B', 'CBartlett18@gsb.columbia.edu'))
	print("Passed!")

def cbslogin_emba_test(username, password):
	print("Testing Login and retrieve EMBA info...")
	a = CBSLogin(username, password)
	assert(a.getInfo('DClayton01') == ('Denise M. Clayton', "EMBA '01", 'Fall 1999', '01B', 'DClayton01@gsb.columbia.edu'))
	print("Passed!")