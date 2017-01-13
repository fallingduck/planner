from planner import *


human1A = Class('HUMAN 1A', units=8, quarters=FALL)
human1B = Class('HUMAN 1B', units=8, quarters=WINTER)
human1C = Class('HUMAN 1C', units=8, quarters=SPRING)
cse42 = Class('CSE 42')
cse43 = Class('CSE 43')
ics6B = Class('ICS 6B')
physics7C = Class('PHYSICS 7C-7LC', units=5)
physics7D = Class('PHYSICS 7D-7LD', units=5)
stats67 = Class('STATS 67')
ics6D = Class('ICS 6D')
cse31 = Class('CSE 31')

socsciH1E = Class('SOCSCI H1E', units=6, quarters=FALL)
socsciH1F = Class('SOCSCI H1F', units=6, quarters=WINTER)
socsciH1G = Class('SOCSCI H1G', units=6, quarters=SPRING)
math2D = Class('MATH 2D')
cse31L = Class('CSE 31L', units=3)
cse45C = Class('CSE 45C')
math3D = Class('MATH 3D')
cse70A = Class('CSE 70A')
cse46 = Class('CSE 46')
math3A = Class('MATH 3A')
cse112 = Class('CSE 112')
cse50 = Class('CSE 50')

scicore1 = Class('Idiom and Practice', quarters=FALL)
scicore2 = Class('Idiom and Practice', quarters=WINTER)
scicore3 = Class('Idiom and Practice', quarters=SPRING)
cse132 = Class('CSE 132')
cse90 = Class('CSE 90', units=2)
in4matx43 = Class('IN4MATX 43')
cse132L = Class('CSE 132L', units=3)
cse141 = Class('CSE 141')
cse135A = Class('CSE 135A')
cse145 = Class('CSE 145-145L', units=6)
cse142 = Class('CSE 142')
cse135B = Class('CSE 135B', units=3)

cse181A = Class('CSE 181A', units=3, quarters=FALL)
cse181B = Class('CSE 181B', units=3, quarters=WINTER)
cse181CW = Class('CSE 181CW', units=3, quarters=SPRING)
elective1 = Class('Elective 1')
elective2 = Class('Elective 2')
eecs148 = Class('EECS 148')
compsci143A = Class('COMPSCI 143A')
cse161 = Class('CSE 161')


cse43.prereq(cse42)

cse31L.prereq(cse31)
cse45C.prereq(cse43)

in4matx43.prereq(cse42)
cse46.prereq(cse45C)
cse141.prereq(cse46)
cse141.prereq(cse31)
cse142.prereq(cse141)

cse70A.prereq(physics7C)
cse70A.coreq(math3D)
cse112.prereq(cse70A)
cse132.prereq(cse31L)
cse132L.prereq(cse132)
cse161.coreq(ics6D)
cse161.prereq(cse46)
compsci143A.prereq(cse46)
compsci143A.prereq(cse31)

cse50.prereq(cse70A)
cse145.prereq(cse132)
cse145.prereq(cse46)
eecs148.prereq(stats67)

cse135A.prereq(cse50)
cse135B.prereq(cse135A)

cse181A.prereq(cse145)
cse181B.prereq(cse181A)
cse181CW.prereq(cse181B)

math3D.prereq(math3A)
math3D.prereq(math2D)

physics7D.coreq(math2D)


schedule = [
    [
        [
            human1A, cse42, ics6B
        ],
        [
            human1B, physics7C, cse43
        ],
        [
            human1C, physics7D, math2D
        ]
    ],
    [
        [
            socsciH1E, math3A
        ],
        [
            socsciH1F, math3D
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
            cse181A, elective1
        ],
        [
            cse181B, elective2
        ],
        [
            cse181CW
        ]
    ]
]

final_schedule = build_schedule(schedule)
print_schedule(final_schedule)
