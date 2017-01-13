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

```bash
jack@osgiliath:~/PycharmProjects/planner$ python3 example.py
Year 1
HUMAN 1A, CSE 42, ICS 6B, UNITS: 16
HUMAN 1B, PHYSICS 7C-7LC, CSE 43, UNITS: 17
HUMAN 1C, PHYSICS 7D-7LD, MATH 2D, UNITS: 17

Year 2
SOCSCI H1E, MATH 3A, CSE 31, CSE 45C, UNITS: 18
SOCSCI H1F, MATH 3D, CSE 46, STATS 67, UNITS: 18
SOCSCI H1G, CSE 31L, CSE 70A, ICS 6D, UNITS: 17

Year 3
Idiom and Practice, CSE 50, CSE 132, CSE 90, CSE 141, UNITS: 18
Idiom and Practice, CSE 145-145L, CSE 135A, CSE 161, UNITS: 18
Idiom and Practice, COMPSCI 143A, CSE 142, IN4MATX 43, UNITS: 16

Year 4
CSE 181A, Elective 1, CSE 132L, CSE 112, CSE 135B, UNITS: 17
CSE 181B, Elective 2, EECS 148, UNITS: 11
CSE 181CW, UNITS: 3
```