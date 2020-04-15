import time
import sys

name = str(input("What's your name? "))
love_count = 0


def first_dialogue():
    global love_count
    answer = str(input("You: "))

    if 'are you sure' or 'sure' in answer.lower():
        time.sleep(1)
        print("Kaylee: Of course I am, don't ever be skeptical about my decisions!")
        love_count -= 1

    elif 'fuck him' in answer.lower():
        time.sleep(1)
        print("Kaylee: Yeah!")
        love_count += 1
    else:
        print("Kaylee: what??")
        first_dialogue()


def second_dialogue():
    answer = str(input("You: "))
    accept = ['ok', 'okay', 'sure', 'you got it']
    not_accept = ['nah', 'no', 'fuck you', 'go to hell']

    if answer.lower() in not_accept:
        time.sleep(2)
        print("Kaylee: Ugh, fuck you", name + ", don't ever talk to me again!!")
        time.sleep(1)
        print("")
        print("You lost to Kaylee's bitchy-ness")
        quit()

    elif answer.lower() in accept:
        time.sleep(1)
        print("Kaylee: Thank you! You're the best", name + "!")
        time.sleep(1.5)

    else:
        print('Kaylee: What??')
        second_dialogue()


def third_dialogue():
    answer = str(input("You: "))
    insult = ["fuck you", "scum", "whore", "bitch", "scumbag"]

    if answer.lower() in insult or 'fuck you' in answer.lower():
        time.sleep(2)
        print("Jackson: Whoa, the fuck did ya jus say to me ya little shit?")
        time.sleep(2)
        print("Jackson: Wait until we meet again >:(")
        time.sleep(2)

    elif 'i like you' or 'i love you' in answer.lower():
        time.sleep(2)
        print("Jackson: Aww, thanks dude :)")
        print("")
        time.sleep(1)
        print("You betrayed Kaylee but won a friend, congrats!")
        quit()

    else:
        print("Jackson: what?")
        third_dialogue()


def fourth_dialogue():
    global love_count
    answer = str(input("You: "))

    if 'better' in answer.lower():
        love_count -= 1
        time.sleep(2)
        print("Kaylee: what do you mean by that >:(")
        print("")
        print("Options: 'nothing' or 'you heard me'")
        answer = str(input("You: "))

        if 'nevermind' or 'nothing' in answer.lower():
            time.sleep(2)
            print("Kaylee: anyways, ill talk to you tomorrow")

        else:
            time.sleep(2)
            print("Kaylee: for a second I thought we're cool, fuck you")
            print("")
            print("You lost to Kaylee's bitchy-ness")
            quit()

    elif 'glad' in answer.lower():
        love_count += 1
        time.sleep(1)
        print("Kaylee: you honestly make me so happy :))")
        time.sleep(2)
        print("Kaylee: anyways, ill talk to you tomorrow")

    else:
        print("Kaylee: what??")
        fourth_dialogue()


def fifth_dialogue():
    global love_count
    answer = str(input("You: "))

    if 'talk' in answer.lower():
        love_count += 1
        time.sleep(2)
        print("Kaylee: Awwe, don't worry, ill wake up early")
        time.sleep(1)
        print("Kaylee: sweet dreams")
        time.sleep(2)
        print("")

    elif 'bye' or 'see you' in answer.lower():
        love_count -= 1
        time.sleep(1)
        print("Kaylee: sweet dreams")
        time.sleep(2)
        print("")

    else:
        print("Kaylee: what??")
        fifth_dialogue()


def sixth_dialogue():
    answer = str(input("You: "))

    if 'idc' in answer.lower():
        time.sleep(1.5)
        print("Kaylee: Oh my god")
        time.sleep(2)
        print("Kaylee: i cant believe you >:( fucking bitch")
        print("")
        time.sleep(1.5)
        print("You lost to Kaylee, because you're an asshole")
        quit()

    elif 'why' or '?' in answer.lower():
        time.sleep(2)
        print("Kaylee: bcz of jackson...he used to comfort me")
        time.sleep(2)
        print("Kaylee: i miss that ")
        time.sleep(1)

    else:
        print("Kaylee: what?")
        sixth_dialogue()


def seventh_dialogue():
    answer = str(input("You: "))

    if 'me' in answer.lower() and love_count == 3:
        time.sleep(2)
        print("Kaylee: well you have been nice to me lately..")
        time.sleep(2)
        print("Kaylee: okay", name + ", let's be a couple")
        time.sleep(2)
        print("")
        print("You won the game. You've became a SIMP, slave of sluts, and jackson's enemy :)")
        quit()

    elif 'me' in answer.lower() and love_count < 3:
        time.sleep(2)
        print("Kaylee: you are a good person", name + ", but you've kind of been a dick")
        time.sleep(2)
        print("Kaylee: i prefer you as a friend more than a boyfriend")
        time.sleep(2)
        print("")
        print("You've won yourself an endless friend-zone with Kaylee. Congrats :)")
        quit()

    elif 'too bad' or 'who cares' in answer.lower():
        time.sleep(2)
        print("Kaylee: well fuck you", name + ", fucking asshole")
        time.sleep(2)
        print("")
        print("Ouch..Thanks for playing :)")
        quit()


print("")
print("Kaylee: what the hell??")
time.sleep(2)
print("Kaylee: jackson went to Jessica's party without inviting me!!")
input("You: ")
time.sleep(2)
print("Kaylee: I am so breaking up with him")
print("")
print("Options: 'are you sure' or 'fuck him'")
first_dialogue()

time.sleep(2)
print("Kaylee: hey, can u do me a favor?")
time.sleep(3)
print("Kaylee: I want you to go to Jackson and insult the shit out of him")
print("")
print("Options: 'no' or 'okay'")
second_dialogue()

print("Kaylee: I'll be waiting for you here! Babe ;)")
time.sleep(1)
print("")

print("Going to Jackson's chat...")

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('=' * i, 1 * i))
    sys.stdout.flush()
    time.sleep(0.04)

time.sleep(1)
print("")
print("")
print("Jackson: What's up ", name + "!")
print("")
print("Options: insult him or not")
third_dialogue()
print("")

print("Going to Kaylee's chat...")

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('=' * i, 1 * i))
    sys.stdout.flush()
    time.sleep(0.04)

time.sleep(1)
print("")
print("")
print("Kaylee: Thank you soooo much", name)
time.sleep(2)
print("Kaylee: I feel much better")
print("")
print("Options: 'you better be' or 'im glad'")
fourth_dialogue()

print("")
print("Options: 'see you tomorrow' or 'i still want to talk'")
fifth_dialogue()

time.sleep(7)
print("The Next Day")
print("")
time.sleep(2)
print("Loading Chat", end="")
s = [".", ".", "."]
for i in s:
    time.sleep(1.5)
    print(str(i), end="")

time.sleep(0.8)
print("")
print("")

print("Going to Kaylee's chat...")

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('=' * i, 1 * i))
    sys.stdout.flush()
    time.sleep(0.04)

print("")
print("")

print("Kaylee: how's it going", name + "?")
input("You: ")
time.sleep(2)
print("Kaylee: Well, im doing fine..")
time.sleep(2)
print("Kaylee: im just lonely")
print("")
print("Options: 'why' or 'i don't care'")
sixth_dialogue()

print("")
print("Options: 'what about me' or 'too bad'")
seventh_dialogue()
