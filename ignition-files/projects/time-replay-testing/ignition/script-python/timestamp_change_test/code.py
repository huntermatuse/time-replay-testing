from com.inductiveautomation.ignition.common.sqltags import BasicTagValue
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.util import Date
import system

def timestamp_change_test():
	current_time = system.date.now()
	three_days_ago = system.date.addDays(current_time, -3)
	tag_value = BasicTagValue(44, DataQuality.GOOD_DATA)
	tag_value.setTimestamp(Date(three_days_ago.time))
	tag_path = "[default]change_me"
	result = system.tag.writeBlocking([tag_path], [tag_value])
	
	if result[0].isGood():
		return "wrote value 44 to 'change_me' with timestamp: %s" % three_days_ago
	else:
		return "Write failed: %s" % result[0]
		