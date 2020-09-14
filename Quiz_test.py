import random

business_score = 0
childrens_score = 0
classics_score = 0
fantasy_score = 0
history_score = 0
horror_score = 0
mystery_score = 0
nonfiction_score = 0
romance_score = 0
scifi_score = 0
sports_score = 0
youngadult_score = 0




#Question 1
answer1 = input("What sounds good? \na)History \nb)ambition \nc)wit \nd)moral ambiguity \nAnswer:")
if answer1 == "a":
    history_score += 50
    nonfiction_score += 10
elif answer1 =="b":
    sports_score += 10
    business_score += 10
elif answer1 == "c":
    scifi_score += 20
    fantasy_score += 10
elif answer1 == "d":
    sports_score += 10
    business_score += 10
    classics_score += 15
else:
    pass

#Question 2
answer2 = input("How long do you want the book to be? \na)Long \nb)Longer \nc)Medium n\d)Short \nAnswer:")
if answer2 == "a":
    fantasy_score += 50
    scifi_score += 20
elif answer2 =="b":
    youngadult_score += 10
    nonfiction_score += 10
elif answer2 == "c":
    history_score += 10
    romance_score += 10
elif answer2 == "d":
    classics_score += 10
else:
    pass

#Question 3
answer3 = input("What sounds good? \na)The Dark Side of Wealth \nb)Young Professionals \nc)Social Analysis \nd)Post Apoctolyptic \nAnswer:")
if answer3 == "a":
    business_score += 20
    sports_score += 30
elif answer3 =="b":
    sports_score += 20
    business_score += 30
elif answer3 == "c":
    nonfiction_score += 10
    youngadult_score += 10
elif answer3 == "d":
    youngadult_score += 20
    scifi_score += 20
else:
    pass

#Question 4
answer4 = input("What sounds good? \na)Twists and Turns \nb)Elemental Magic \nc)Brutal Honesty \nd)Positive Read \nAnswer:")
if answer4 == "a":
    mystery_score += 50
elif answer4 =="b":
    fantasy_score += 50
elif answer4 == "c":
    nonfiction_score += 10
    business_score += 10
elif answer4 == "d":
    romance_score += 10
    scifi_score += 10
    childrens_score += 20
else:
    pass

#Question 5
answer5 = input("What sounds good? \na)Modern Love \nb)Memoirs \nc)Fantasy \nd)Murder Mystery \nAnswer:")
if answer5 == "a":
    romance_score += 50
elif answer5 =="b":
    nonfiction_score += 30
elif answer5 == "c":
    fantasy_score += 50
elif answer5 == "d":
    mystery_score += 50
else:
    pass

#Question 6
answer6 = input("What sounds good? \na)Something Modern \nb)Something Haunting \nc)Something Helpful \nd)Something Fun \nAnswer:")
if answer6 == "a":
    business_score += 10
    scifi_score += 10
    youngadult_score += 10
elif answer6 =="b":
    horror_score += 50
    mystery_score += 10
elif answer6 == "c":
    business_score += 30
    sports_score += 10
elif answer6 == "d":
    romance_score += 10
    youngadult_score += 20
    scifi_score += 10
else:
    pass

#Question 7
answer7 = input("What sounds good? \na)A real person \nb)An amateur detective \nc)A headstrong heroine \nd)A royal with a secret \nAnswer:")
if answer7 == "a":
    nonfiction_score += 10
    horror_score += 20
elif answer7 =="b":
    mystery_score += 20
elif answer7 == "c":
    youngadult_score += 20
    fantasy_score += 10
elif answer7 == "d":
    nonfiction_score += 20
    history_score += 10
else:
    pass

#Question 8
answer8 = input("What sounds good? \na)An epic adventure \nb)Thriller \nc)Romance \nd)Real Stories \nAnswer:")
if answer8 == "a":
    fantasy_score += 10
    scifi_score += 20
elif answer8 =="b":
    horror_score += 20
    mystery_score += 20
elif answer8 == "c":
    romance_score += 30
elif answer8 == "d":
    nonfiction_score += 20
    history_score += 20
else:
    pass

#Question 9
answer9 = input("What age Range? \na)Kids \nb)Teens \nc)Young Adult \nd)Adult \nAnswer:")
if answer9 == "a":
    childrens_score += 200
elif answer9 =="b":
    childrens_score += 50
    scifi_score += 10
elif answer9 == "c":
    youngadult_score += 100
elif answer9 == "d":
    youngadult_score += 10
else:
    pass

#Question 10
answer10 = input("Where do you want to go? \na)New York \nb)California \nc)No where \nd)London \nAnswer:")
if answer10 == "a":
    business_score += 50
    youngadult_score += 10
elif answer10 =="b":
    sports_score += 10
elif answer10 == "c":
    pass
elif answer10 == "d":
    fantasy_score += 20
    youngadult_score += 10
    romance_score += 10
else:
    pass

queue = []

total_score = business_score + childrens_score + classics_score + fantasy_score + history_score + horror_score + mystery_score + nonfiction_score + romance_score + scifi_score + sports_score + youngadult_score

business_percentage = (business_score / total_score) * 100
childrens_percentage = (childrens_score / total_score) * 100
classics_percentage = (classics_score / total_score) * 100
fantasy_percentage = (fantasy_score / total_score) * 100
history_percentage = (history_score / total_score) * 100
horror_percentage = (horror_score / total_score) * 100
mystery_percentage = (mystery_score / total_score) * 100
nonfiction_percentage = (nonfiction_score / total_score) * 100
romance_percentage = (romance_score / total_score) * 100
scifi_percentage = (scifi_score / total_score) * 100
sports_percentage = (sports_score / total_score) * 100
youngadult_percentage = (youngadult_score / total_score) * 100

print(business_percentage,childrens_percentage,classics_percentage,fantasy_percentage,fantasy_percentage,history_percentage,horror_percentage,mystery_percentage,scifi_percentage,sports_percentage,youngadult_percentage)

for x in range(0,101):
    random_num = random.randrange(100)
    if(0 < random_num and random_num < business_percentage):
        pass
    if (business_percentage < random_num and
            random_num < business_percentage+childrens_percentage):
        pass
    if (business_percentage+childrens_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage+scifi_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage+scifi_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage+scifi_percentage+sports_percentage):
        pass
    if (business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage+scifi_percentage+sports_percentage < random_num and
            random_num < business_percentage+childrens_percentage+classics_percentage+fantasy_percentage+history_percentage+horror_percentage+mystery_percentage+nonfiction_percentage+romance_percentage+scifi_percentage+sports_percentage+youngadult_percentage):
        pass

