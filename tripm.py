#!/usr/bin/env python

data = """
1	Boldness	Optimism	I’m optimistic more often than not.	+
2	Meanness	Empathy	How other people feel is important to me.	-
3	Disinhibition	Impatient Urgency	I often act on immediate needs.	+
4	Boldness	Intrepidness	I have no strong desire to parachute out of an airplane.	-
5	Disinhibition	Dependability	I've often missed things I promised to attend.	+
6	Meanness	Excitement Seeking	I would enjoy being in a high-speed chase.	+
7	Boldness	Resilience	I am well-equipped to deal with stress.	+
8	Meanness	Empathy	I don’t mind if someone I dislike gets hurt.	+
9	Disinhibition	Problematic Impulsivity	My impulsive decisions have caused problems with loved ones.	+
10	Boldness	Courage	I get scared easily.	-
11	Meanness	Empathy	I sympathize with others’ problems.	-
12	Disinhibition	Irresponsibility	I have missed work without bothering to call in.	+
13	Boldness	Dominance	I'm a born leader.	+
14	Meanness	Physical Aggression	I enjoy a good physical fight.	+
15	Disinhibition	Problematic Impulsivity	I jump into things without thinking.	+
16	Boldness	Optimism	I have a hard time making things turn out the way I want.	-
17	Meanness	Relational Aggression	I return insults.	+
18	Disinhibition	Irresponsibility	I've gotten in trouble because I missed too much school.	+
19	Boldness	Persuasiveness	I have a knack for influencing people.	+
20	Meanness	Empathy	It doesn’t bother me to see someone else in pain.	+
21	Disinhibition	Planful Control	I have good control over myself.	-
22	Boldness	Tolerance for Uncertainty	I function well in new situations, even when unprepared.	+
23	Meanness	Relational Aggression	I enjoy pushing people around sometimes.	+
24	Disinhibition	Theft	I have taken money from someone's purse or wallet without asking.	+
25	Boldness	Self Confidence	I don't think of myself as talented.	-
26	Meanness	Relational Aggression	I taunt people just to stir things up.	+
27	Disinhibition	Alienation	People often abuse my trust.	+
28	Boldness	Courage	I'm afraid of far fewer things than most people.	+
29	Meanness	Empathy	I don't see any point in worrying if what I do hurts someone else.	+
30	Disinhibition	Dependability	I keep appointments I make.	-
31	Disinhibition	Boredom Proneness	I often get bored quickly and lose interest.	+
32	Boldness	Resilience	I can get over things that would traumatize others.	+
33	Meanness	Empathy	I am sensitive to the feelings of others.	-
34	Disinhibition	Fraud	I have conned people to get money from them.	+
35	Boldness	Tolerance for Uncertainty	It worries me to go into an unfamiliar situation without knowing all the details.	-
36	Meanness	Empathy	I don't have much sympathy for people.	+
37	Disinhibition	Problematic Impulsivity	I get in trouble for not considering the consequences of my actions.	+
38	Boldness	Persuasiveness	I can convince people to do what I want.	+
39	Meanness	Honesty	For me, honesty really is the best policy. 	-
40	Meanness	Destructive Aggression	I've injured people to see them in pain.	+
41	Boldness	Dominance	I don’t like to take the lead in groups.	-
42	Meanness	Relational Aggression	I sometimes insult people on purpose to get a reaction from them.	+
43	Disinhibition	Theft	I have taken items from a store without paying for them.	+
44	Boldness	Social Assurance	It's easy to embarrass me.	-
45	Meanness	Excitement Seeking	Things are more fun if a little danger is involved.	+
46	Disinhibition	Impatient Urgency	I have a hard time waiting patiently for things I want.	+
47	Boldness	Intrepidness	I stay away from physical danger as much as I can.	-
48	Meanness	Empathy	I don't care much if what I do hurts others.	+
49	Disinhibition	Irresponsibility	I have lost a friend because of irresponsible things I've done.	+
50	Boldness	Self Confidence	I don't stack up well against most others.	-
51	Disinhibition	Problematic Impulsivity	Others have told me they are concerned about my lack of self-control. 	+
52	Meanness	Empathy	It’s easy for me to relate to other people’s emotions.	-
53	Disinhibition	Theft	I have robbed someone.	+
54	Boldness	Social Assurance	I never worry about making a fool of myself with others.	+
55	Meanness	Empathy	It doesn’t bother me when people around me are hurting.	+
56	Disinhibition	Irresponsibility	I have had problems at work because I was irresponsible.	+
57	Boldness	Persuasiveness	I’m not very good at influencing people.	-
58	Disinhibition	Theft	I have stolen something out of a vehicle.	+
"""

lines = data.split("\n")
scores = {}
for line in lines:
    line = line.strip()
    if len(line) == 0:
        continue
    parts = line.split("\t")
    q = parts[3]
    q = q.replace('.', '?')
    print(q)
    ans = int(input())
    key = parts[4]
    if key == '-':
        ans = 3 - ans
    if not parts[1] in scores:
        scores[parts[1]] = 0
    scores[parts[1]] += ans
print(scores)
