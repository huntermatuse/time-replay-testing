# Manual Timestamp for Ignition Tag

This repo was meant to test if it was possible to manually write a timestamp while calling `system.tag.writeBlocking` when creating the tag value using BasicTagValue. 

### imports

```jython
from com.inductiveautomation.ignition.common.sqltags import BasicTagValue
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.util import Date
import system
```

by using the ignition java sdk, we have more control over what we can do. i think. 

### writing past dates

```jython
current_time = system.date.now()
three_days_ago = system.date.addDays(current_time, -3)
tag_value = BasicTagValue(44, DataQuality.GOOD_DATA)
tag_value.setTimestamp(Date(three_days_ago.time))
tag_path = "[default]change_me"
result = system.tag.writeBlocking([tag_path], [tag_value])
```

## Findings

Using the jython code above you are able to write past dates in tag timestamps. Doing the same scripting while trying to write future dates is not possible as currently written.

## Future Testing

- writing dates in the future
- 'replaying' historical data are higher speeds for testing

