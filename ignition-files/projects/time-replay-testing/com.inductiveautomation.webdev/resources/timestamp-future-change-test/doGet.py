def doGet(request, session):
	from timestamp_change_test import timestamp_future_change_test
	return {'response': timestamp_future_change_test()}