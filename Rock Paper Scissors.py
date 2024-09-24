import random

def play():
    # prompt user input, since we're playing against the computer
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")  # adding a line break (\n)
    computer = random.choice(['r', 'p', 's']) # computer randomly chooses one of the 3 options

# now, we know the users choice of inputs and the computers random choice of inputs
# since we have that, now it is time to build the conditions / rules in order to determine who wins

    if user == computer: # if user and computer have the same choice:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if win(user, computer): # apply the helper function
        return 'You won!'

    return 'You lost!'
    # notice, there is no IF statement before this last return
    # the reason behind this is because we've already passed two prior cases.
    # the function ends after each of these cases if the condition is met, so if you lost, 
    # then neither of those 2 prior cases of tie or win will pass
    # leaving you with the last case, of you lost

# for a basic understanding of how RPS works:
# rock beats scissors, scissors beats paper, and paper beats rock

# define a helper function to determine who wins
def win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())