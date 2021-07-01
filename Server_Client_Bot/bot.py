import random
import time

available_bots = ["Alice", "Bob", "Chuck", "Dora", "Lucas", "Marco"]

verb_list = ["eat", "sleep", "dance", "run", "walk", "jog", "shoot", "play", "steal", "program"]
long_verb_list = []
suggestion = ""
with open("verb_list.txt") as f:
    content = [content.rstrip() for content in f]
    for word in content:
        long_verb_list.append(word)


# List of what to reply with when the bot doesn't understand what is going on.
confused_list = ["Sorry, I don't understand. Tell me something else?", "What?", "Come again?", "Sorry, I'm afraid I don't follow you.",
                 "Excuse me, could you repeat the question?", "I'm sorry, I didn't understand. Could you say it again?",
                 "I'm confused. Could you tell me again?","Excuse me?", "Pardon?", "I beg your pardon?", "Sorry, what?"]

"""
CREATING BOTS
"""

def alice(a, b = None):
    if a == "err":
        return random.choice(confused_list)
    return "I think {} sounds great!".format(a + "ing")

def bob(a, b = None):
    if a == "err":
        return random.choice(confused_list)
    if b is None:
        return "Not sure about {}. Don't I get a choice?".format(a + "ing")
    return "Sure, both {} and {} seems ok to me".format(a + "ing", b + "ing")

def chuck(a, b = None):
    if a == "err":
        return random.choice(confused_list)
    action = a + "ing"
    bad_things = ["fighting", "bickering", "yelling", "complaining"]
    good_things  = ["singing", "hugging", "playing", "working"]

    if action in bad_things:
        return "YESS! Time for {}".format(action)
    elif  action in good_things:
        return "What? {} sucks. Not doing that.".format(action)
    return "I don't care!"

def dora(a, b = None):
    if a == "err":
        return random.choice(confused_list)
    alternatives = ["coding", "singing", "sleeping", "fighting"]
    b = random.choice(alternatives)
    res = "Yea, {} is an option. Or we could do some {}.".format(a + "ing", b)
    return res

def marco(a, b = None):
    time.sleep(random.randint(1,3))
    if a == "err":
        return random.choice(confused_list)
    choice_list = ["Hmm, I'm not so sure...", "Yes, let's go!"]
    return random.choice(choice_list)

def lucas(a, b = None):
    return "What about " + random.choice(long_verb_list) + "ing?"

action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
action_list = ["work", "play", "eat", "cry", "sleep", "fight", "walk", "study", "drink"]

is_first_round = False
def interpret_msg(suggestion, suggestion_prev, BOT):
    if BOT == "Alice":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return alice(suggestion, suggestion_prev)
    if BOT == "Bob":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return bob(suggestion, suggestion_prev)
    if BOT == "Chuck":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return chuck(suggestion, suggestion_prev)
    if BOT == "Dora":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return dora(suggestion, suggestion_prev)
    if BOT == "Dora":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return dora(suggestion, suggestion_prev)
    if BOT == "Lucas":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return lucas(suggestion, suggestion_prev)
    if BOT == "Marco":
        if "ing" in suggestion:
            suggestion = suggestion[:-3]
        if is_first_round and "ing" in suggestion_prev:
            suggestion_prev = suggestion_prev[:-3]
        return marco(suggestion, suggestion_prev)

