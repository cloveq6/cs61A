from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact
from hog import always_roll

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum = 0
    flag = False
    while num_rolls > 0 :
        tmp = dice()
        if tmp == 1:
            flag = True
        sum += tmp
        num_rolls -= 1 
    if flag :
        return 1
    return sum
    # END PROBLEM 1

# counted_dice = make_test_dice(4, 1, 2, 6)  
# print(roll_dice(3, counted_dice))
# print(roll_dice(1, counted_dice))
# print(roll_dice(1, counted_dice))


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    count = 100 - score
    while count > 0 : # 循环count 次
        pi = pi // 10
        count -= 1
    # END PROBLEM 2

    return pi % 10 + 3

# print(roll_dice(4))

s = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[41])
# print(s[42])
# print(s[100])
# print(s[80])
# print(s[12])
# print(s[5])

# print(len(s))

# print(free_bacon(0))
# print(free_bacon(1))
# print(free_bacon(2))
# print(free_bacon(8))
# print(free_bacon(42))
# print(free_bacon(9))
# print(free_bacon(0))
# print(free_bacon(2))
print(s[19])





def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls==0 : return free_bacon(opponent_score)
    return roll_dice(num_rolls, dice)
    
    # END PROBLEM 3
    

# print(take_turn(2, 0, make_test_dice(4, 5, 1)))
# print(take_turn(3, 0, make_test_dice(4, 6, 1)))
# print(take_turn(0, 2))
# print(take_turn(0, 0))

def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"
    def gcd_inner(a, b):
        if a<b: #如果a<b，则交换两数位置，否则不交换
            a,b = b,a
        r = a % b #求a/b的余数
        while r != 0: #在余数不为零时，始终进行交换和相除
            a,b = b,r
            r = a % b
        return b #余数为零后，打印输出b
    if player_score <=0 or opponent_score <=0 : return False
    gcd = gcd_inner(player_score, opponent_score)
    return gcd >= 10
    # END PROBLEM 4a
    
def gcd(a, b):
    if a<b: #如果a<b，则交换两数位置，否则不交换
        a,b = b,a
    r = a % b #求a/b的余数
    while r != 0: #在余数不为零时，始终进行交换和相除
        a,b = b,r
        r = a % b
    return b #余数为零后，打印输出b
    


# print(swine_align(8, 36))
# print(swine_align(20, 30))
# print(swine_align(24, 36))
# print(swine_align(36, 36))
# print(swine_align(15, 0))

def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    "*** YOUR CODE HERE ***"
    if player_score >= opponent_score : return False
    diff = opponent_score - player_score
    if diff < 3 : return True
    return False
    # END PROBLEM 4b
    
def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence
    
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal or score1 < goal :
        
        if who == 0:
            count0 = strategy0(score0, score1)
            # print("count0 :"+str(count0))
            cur_score0 = take_turn(count0, score1, dice)
            # print("cur_score0 :"+str(cur_score0))
            score0 += cur_score0
            say = say(score0, score1)
            if score0 >= goal : 
                return score0, score1
            # print("swine_align(score0, score1)" + str(swine_align(score0, score1)))
            # print("pig_pass(score0, score1)" + str(pig_pass(score0, score1)))
            if swine_align(score0, score1)==False and pig_pass(score0, score1)==False :
                who = 1
        if who == 1:
            count1 = strategy1(score1, score0)
            # print("count1 :"+str(count1))
            cur_score1 = take_turn(count1, score0, dice)
            # print("cur_score1 :"+str(cur_score1))
            score1 += cur_score1
            say = say(score0, score1)
            if score1 >= goal : 
                return score0, score1
            if swine_align(score1, score0)==False and pig_pass(score1, score0)==False :
                who = 0
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return score0, score1

# always_three = make_test_dice(3)
# always_seven = make_test_dice(7)

# always = always_roll

# strat0 = lambda score, opponent: opponent % 10
# strat1 = lambda score, opponent: max((score // 10) - 4, 0)

# # s0, s1 = play(always(5), always(3), score0=91, score1=10, dice=always_three)
# # s0, s1 = play(always(5), always(5), goal=10, dice=always_three)
# s0, s1 = play(strat0, strat1, score0=71, score1=80, dice=always_seven)
# print(s0)
# print(s1)

# def total(s0, s1):
#     print(s0 + s1)
#     return echo
# def echo(s0, s1):
#     print(s0, s1)
#     return total

# s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)

# def echo(s0, s1):
#     print(s0, s1)
#     return echo
# strat0 = lambda score, opponent: 1 - opponent // 10
# strat1 = always_roll(3)
# s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def say(score0, score1):
        cur_run_high = 0
        cur_score = 0
        latest_run_high = running_high
        if who == 0:
            cur_run_high = score0 - last_score
            cur_score = score0
        if who == 1:
            cur_run_high = score1 - last_score
            cur_score = score1
        if cur_run_high > running_high:
            latest_run_high = cur_run_high
            print(cur_run_high, 'point(s)! The most yet for Player', who)
        return announce_highest(who, cur_score, latest_run_high)
    return say
    # END PROBLEM 7
    
# f0 = announce_highest(1)
# f1 = f0(12, 0)
# f2 = f1(12, 9)
# f3 = f2(20, 9)
# f4 = f3(20, 30)
# f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
# f6 = f5(21, 47)
# f7 = f6(21, 77)

# def printed(f):
#     def print_and_return(*args):
#         result = f(*args)
#         print('Result:', result)
#         return result
#     return print_and_return

# printed_pow = printed(pow)
# printed_pow(2, 8)


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def process_and_return(*args):
        sum = 0
        cur_count = trials_count
        while(cur_count > 0):
            sum += original_function(*args)
            cur_count -= 1
        return sum / trials_count
    return process_and_return
    # END PROBLEM 8
    
# dice = make_test_dice(3, 1, 5, 6)
# averaged_dice = make_averaged(dice, 1000)
# print(averaged_dice())

# averaged_roll_dice = make_averaged(roll_dice, 1000)
# print(averaged_roll_dice(2, dice))


def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    count = 10
    averaged_roll_dice = make_averaged(roll_dice, 1000)
    max_score = 0
    res = 10
    while count>0 :
        avg_score = averaged_roll_dice(count, dice)
        if avg_score >= max_score : 
            res = count
            max_score = avg_score
        count -= 1
    return res
    # END PROBLEM 9

# dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
# averaged_roll_dice = make_averaged(roll_dice, 1000)
# count = 10
# while count>0 :
#     print(averaged_roll_dice(count, dice))  count=4最大 所以max_scoring_num_rolls返回4
#     count -= 1

# dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
# dice = make_test_dice(*([2] * 55 + [1, 2] * 500))
# dice = make_test_dice(2)
# dice = make_test_dice(1, 6)
# print(max_scoring_num_rolls(dice))

def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    res = free_bacon(opponent_score)
    if(res >= cutoff):
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 10
    
    
def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    cur_point = free_bacon(opponent_score)
    if pig_pass(score+cur_point, opponent_score) or swine_align(score+cur_point, opponent_score):
        return 0
    return bacon_strategy(score, opponent_score, cutoff, num_rolls)  # Replace this statement
    # END PROBLEM 11

print(bacon_strategy(10, 19, 8, 6))
print(extra_turn_strategy(10, 19, cutoff=8, num_rolls=6))
print(free_bacon(19))