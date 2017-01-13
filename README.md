Use at your own risk. Designed to work with quarter systems.

```python
from planner import *

ics31 = Class('ICS 31')
ics32 = Class('ICS 32')

ics32.prereq(ics31)

schedule = build_schedule()
print_schedule(schedule)
```

Check out `example.py` for a more complete example (my own four-year plan).