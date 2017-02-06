Use at your own risk. Designed to work with quarter systems.

```python
from planner import *

ics31 = Class('ICS 31')
ics32 = Class('ICS 32')

ics32.prereq(ics31)

schedule = build_schedule()
print_schedule(schedule)
```

Check out `cs.py` or `cse.py` for more complete examples.

```bash
jack@osgiliath:~/PycharmProjects/planner$ python3 cs.py
Year 1
HUMAN 1A, ICS 32, ICS 6B, UNITS: 16
HUMAN 1B, ICS 33, PHYSICS 7C-7LC, UNITS: 17
HUMAN 1C, ICS 51, ICS 45C, UNITS: 18

Year 2
SOCSCI H1E, ICS 90, ICS 46, COMPSCI 122A, UNITS: 15
SOCSCI H1F, ICS 6D, COMPSCI 143A, STATS 67, UNITS: 18
SOCSCI H1G, IN4MATX 43, ICS 53-53L, UNITS: 16

Year 3
SCIENCE, COMPSCI 161, ICS 6N, IN4MATX 121, UNITS: 16
SCIENCE, COMPSCI 167, COMPSCI 131, ICS 139W, UNITS: 16
SCIENCE, COMPSCI 132, COMPSCI 163, COMPSCI 122B, UNITS: 16

Year 4
IN4MATX 161, COMPSCI 134, IN4MATX 151, IN4MATX 131, UNITS: 16
COMPSCI H198, COMPSCI 178, IN4MATX 113, COMPSCI 133, UNITS: 16
COMPSCI H198, COMPSCI 145-145L, UNITS: 10
```