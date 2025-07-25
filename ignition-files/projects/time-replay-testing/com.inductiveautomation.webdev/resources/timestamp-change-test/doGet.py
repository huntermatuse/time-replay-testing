def doGet(request, session):
	from timestamp_change_test import timestamp_change_test
	return {'response': timestamp_change_test()}