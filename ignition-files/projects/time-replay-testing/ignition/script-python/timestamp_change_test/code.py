from com.inductiveautomation.ignition.common.sqltags import BasicTagValue
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.util import Date
import system

def timestamp_change_test():
	tag_prep = make_testing_tag()
	if tag_prep != True:
		return tag_prep
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
		
def make_testing_tag():
	change_me_tag_config = {
	  "valueSource": "memory",
	  "name": "change_me",
	  "tagType": "AtomicTag"
	}
	
	change_me_tag_path = '[default]change_me'
	
	try:
		if system.tag.exists(change_me_tag_path):
			system.tag.deleteTags([change_me_tag_path])
			
		system.tag.configure('[default]', [change_me_tag_config])
		
		return True
	except Exception as e:
		return str(e)