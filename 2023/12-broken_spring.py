import math

input_text = [i.replace('\n', '') for i in list(open("2023/12-broken_spring.txt"))]

# def get_candidates(start: str, spring: str):
#     cadidate = []
#     for i in range(len(spring)):
#         for sti, stj in enumerate(start):
#             if spring[i] == '?':
#                 cadidate.append(i)
#             if spring[i] == '?':

# print(find_group(3, '.??..??...?##.'))

for i in input_text:
    print(i)
    spring = i.split(' ')[0]
    arrangements = i.split(' ')[1].split(',')
    arrangements = [int(j) for j in arrangements]
    num_pound = sum(arrangements)
    num_dot = len(arrangements) - 1
    num_spring_pound = 0
    num_spring_dot = 0
    num_spring_question = 0
    for i in spring:
        if i == '#':
            num_spring_pound += 1
        if i == '.':
            num_spring_dot += 1
        if i == '?':
            num_spring_question += 1
    dot_to_place = num_spring_question - (num_pound - num_spring_pound) - max(0, (num_dot - num_spring_dot))
    print(num_spring_question, num_pound, num_spring_pound, num_dot)
    places = num_spring_question - (num_pound - num_spring_pound)
    choices = math.factorial(places)//(math.factorial(dot_to_place) * math.factorial(places - dot_to_place))
    print(choices)

        
