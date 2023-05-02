dwarves_list = ["Doc", "Dopey", "Bashful", "Grumpy"]

def roll_call_dwarves(dwarves_list):
    for i in range (len(dwarves_list)):
        print(f"{i+1}. {dwarves_list[i]}")

roll_call_dwarves(dwarves_list)
    

def summon_captain_planet():
    pass

short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
        
    return False

print(long_planeteer_calls(assorted_words)) # input short_words, assorted_words, or a custom list

def find_the_cheese():
    pass
