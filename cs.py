from planner import *


# CHP

human1A = Class('HUMAN 1A', units=8, quarters=FALL)
human1B = Class('HUMAN 1B', units=8, quarters=WINTER)
human1C = Class('HUMAN 1C', units=8, quarters=SPRING)

socsciH1E = Class('SOCSCI H1E', units=6, quarters=FALL)
socsciH1F = Class('SOCSCI H1F', units=6, quarters=WINTER)
socsciH1G = Class('SOCSCI H1G', units=6, quarters=SPRING)

scicore1 = Class('SCIENCE', quarters=FALL)
scicore2 = Class('SCIENCE', quarters=WINTER)
scicore3 = Class('SCIENCE', quarters=SPRING)

research1 = Class('COMPSCI H198')
research2 = Class('COMPSCI H198')


# Lower div

ics32 = Class('ICS 32')
ics33 = Class('ICS 33')
ics45C = Class('ICS 45C')
ics46 = Class('ICS 46')
ics51 = Class('ICS 51', units=6)
ics53 = Class('ICS 53-53L', units=6, quarters=WINTER | SPRING)
in4matx43 = Class('IN4MATX 43', quarters=FALL | SPRING)  # Also required for Informatics minor
ics90 = Class('ICS 90', units=1, quarters=FALL)

ics6B = Class('ICS 6B')
ics6D = Class('ICS 6D', quarters=FALL | WINTER)  # Get the good prof
ics6N = Class('ICS 6N', quarters=FALL | WINTER)
stats67 = Class('STATS 67')


# Upper div

cs161 = Class('COMPSCI 161', quarters=FALL | WINTER)
ics139W = Class('ICS 139W')

# Networked Systems
cs132 = Class('COMPSCI 132', quarters=FALL | SPRING)
cs133 = Class('COMPSCI 133', quarters=WINTER)  # Project Course
cs134 = Class('COMPSCI 134', quarters=FALL)
cs143A = Class('COMPSCI 143A', quarters=WINTER | SPRING)

cs122A = Class('COMPSCI 122A')
cs122B = Class('COMPSCI 122B', quarters=WINTER | SPRING)  # Project Course
cs167 = Class('COMPSCI 167', quarters=WINTER)

# Courses of my own choosing
cs178 = Class('COMPSCI 178', quarters=WINTER)
cs131 = Class('COMPSCI 131', quarters=WINTER)
cs163 = Class('COMPSCI 163', quarters=SPRING)
cs145 = Class('COMPSCI 145-145L', units=6, quarters=SPRING)


# Informatics minor
in4matx131 = Class('IN4MATX 131', quarters=FALL | WINTER)
in4matx161 = Class('IN4MATX 161', quarters=FALL | WINTER)

# Informatics minor - courses of my own choosing
in4matx113 = Class('IN4MATX 113', quarters=WINTER)
in4matx121 = Class('IN4MATX 121', quarters=FALL)
in4matx151 = Class('IN4MATX 151', quarters=FALL | WINTER)



# Extras

physics7C = Class('PHYSICS 7C-7LC', units=5)


# PREREQS

ics33.prereq(ics32)
ics45C.prereq(ics33)
ics46.prereq(ics45C)
ics51.prereq(ics6B)
ics53.prereq(ics51)
in4matx43.prereq(ics32)

ics6D.prereq(ics6B)

cs161.prereq(ics6B)
cs161.prereq(ics6D)
cs161.prereq(ics46)
ics139W.prereq(human1C)

cs132.prereq(stats67)
cs133.prereq(cs132)
cs134.prereq(ics6D)
cs134.prereq(ics33)
cs134.prereq(cs122A)
cs143A.prereq(ics46)
cs143A.prereq(ics51)

cs122A.prereq(ics33)
cs122B.prereq(cs122A)
cs167.prereq(cs161)

cs178.prereq(ics6B)
cs178.prereq(ics6D)
cs178.prereq(ics6N)
cs178.prereq(stats67)
cs131.prereq(ics53)
cs131.prereq(cs143A)
cs163.prereq(cs161)
cs145.prereq(ics46)
cs145.prereq(ics51)

in4matx113.prereq(ics33)
in4matx113.prereq(in4matx43)
in4matx121.prereq(ics33)
in4matx151.prereq(in4matx43)

research1.prereq(human1C)
research2.prereq(human1C)


# BASIC SCHEDULE

schedule = [
    [
        [
            human1A, ics32, ics6B
        ],
        [
            human1B, ics33, physics7C
        ],
        [
            human1C
        ]
    ],
    [
        [
            socsciH1E, ics90
        ],
        [
            socsciH1F,
        ],
        [
            socsciH1G
        ]
    ],
    [
        [
            scicore1
        ],
        [
            scicore2
        ],
        [
            scicore3
        ]
    ],
    [
        [

        ],
        [
            research1  # Or whenever
        ],
        [
            research2
        ]
    ]
]

final_schedule = build_schedule(schedule, packing=10)
print_schedule(final_schedule)
