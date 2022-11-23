
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    list = []
    for para in paragraphs:
        if select(para) : list.append(para)
    if(k >= len(list)) : return ''
    return list[k]
    # END PROBLEM 1
    
# ps = ['short', 'really long', 'tiny']
# s = lambda p: len(p) <= 5
# print(choose(ps, s, 0))
# print(choose(ps, s, 1))
# print(choose(ps, s, 2))


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # def sub_str(sub, str):
    #     if len(str) < len(sub) : return False
    #     sub_len = len(sub)
    #     if sub == str[:sub_len] : return True
    #     return sub_str(sub, str[1:])  
    def match(topic, para):
        s="".join(filter(str.isalpha, para))
        s = lower(s)
        # print("s " + s)
        # print("topic "+ topic)
        return s==topic
    def helper(topics, para):
        para_split = para.split()
        # print(para_split)
        for pp in para_split:
            for topic in topics:
                if match(topic, pp) : return True
        return False
    return lambda para : helper(topic, para)
    # END PROBLEM 2
    

# ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
# print(ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj'))

# about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
# print(about_dogs('Cute Dog!'))
# print(choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0))
# print(choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 1))

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed)==0 or len(reference_words)==0 : return 0.0
    head = 0
    length = len(typed) if len(typed) < len(reference_words) else len(reference_words)
    for i in range(0, length):
        if typed[i].replace('\t', '') == reference_words[i].replace('\t', ''):
            head += 1        
    return head/len(typed) * 100


# print(accuracy('Cute Dog!', 'Cute Dog.'))
# print(accuracy('A Cute Dog!', 'Cute Dog.'))
# print(accuracy('cute Dog.', 'Cute Dog.'))
# print(accuracy('Cute Dog. I say!', 'Cute Dog.'))
# print(accuracy('Cute', 'Cute Dog.'))
# print(accuracy('', 'Cute Dog.'))
# print(accuracy(" a b \tc" , "a b c"))
# print(accuracy("a b c d", " a d "))

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / (elapsed / 60)
    # END PROBLEM 4

# print(wpm("12345", 3))
# print(wpm("a b c", 20))

def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words : return user_word
    alter_word = min(valid_words, key=lambda x : diff_function(x, user_word, limit))
    # print(alter_word)
    # print(diff_function(user_word, alter_word, limit))
    if diff_function(user_word, alter_word, limit) > limit:
        return user_word
    return alter_word
    
    # END PROBLEM 5
# abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1)) 
# print(autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10))
# print(autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0))
# print(autocorrect("wor", ["worry", "car", "part"], abs_diff, 10))

# first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
# print(autocorrect("wrod", ["word", "rod"], first_diff, 1))
# print(autocorrect("inside", ["idea", "inside"], first_diff, 0.5))
# print(autocorrect("inside", ["idea", "insider"], first_diff, 0.5))
# print(autocorrect("outside", ["idea", "insider"], first_diff, 0.5))

# "cul", ["culture", "cult", "cultivate"]

# def shifty_shifts(start, goal, limit):
#     """A diff function for autocorrect that determines how many letters
#     in START need to be substituted to create GOAL, then adds the difference in
#     their lengths.
#     """
#     # BEGIN PROBLEM 6
#     # assert False, 'Remove this line'
#     # print("circle")
    
#     if len(start) == 0 : return len(goal)
#     if len(goal) == 0 : return len(start)
#     # if limit == 0 : return limit+1
#     if start[0] == goal[0] : return shifty_shifts(start[1:], goal[1:], limit)
#     return shifty_shifts(start[1:], goal[1:], limit) + 1
#     # END PROBLEM 6


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    # print("circle")
    def helper(start, goal, limit, count):
        if count > limit : return count
        if len(start) == 0 : return len(goal)
        if len(goal) == 0 : return len(start)
        # if limit == 0 : return limit+1
        # print("hello")
        # print(count)
        if start[0] == goal[0] : return helper(start[1:], goal[1:], limit, count)
        return helper(start[1:], goal[1:], limit, count+1) + 1
    return helper(start, goal, limit, 0)

    # END PROBLEM 6  
    
# shifty_shifts, "someaweqwertyuio", "awesomeasdfghjkl", 3
# print(shifty_shifts("awful", "awesome", 1))
# print(shifty_shifts("one", "two", 10))
# print(shifty_shifts("awe", "awesome", 10))
# print(shifty_shifts("goodbye", "goo", 10))
# print(shifty_shifts("someaweqwertyuio", "awesomeasdfghjkl", 3))

# print(shifty_shifts('pc', 'pc', 0))
# print(shifty_shifts('pc', 'pc', 1))

# def pawssible_patches(start, goal, limit):
#     """A diff function that computes the edit distance from START to GOAL."""
#     if len(start)==0 or len(goal)==0 : 
#         return len(start) if len(goal) == 0 else len(goal)
#     elif start[0] == goal[0] : return pawssible_patches(start[1:], goal[1:], limit)
#     else:
#         if limit == 0: return 1000000
#         add_diff = pawssible_patches(start, goal[1:], limit-1) + 1
#         remove_diff = pawssible_patches(start[1:], goal, limit-1) + 1
#         substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1) + 1
#         res = min(min(add_diff, remove_diff), substitute_diff)
#         return res
        
        
        # if len(start) == len(goal) :
        #     return
        # else:
        #     return pawssible_patches(start[1:], goal, limit) + 1
        
    
    
    # if len(start) > len(goal) : return pawssible_patches(start[1:], goal, limit) + 1
    # elif len(start) < len(goal) : return pawssible_patches(start, goal[1:], limit) + 1
    # return pawssible_patches(start, goal[1:], limit) + 1
    
    
    # if ___________: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # elif ___________: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # else:
    #     add_diff = ... # Fill in these lines
    #     remove_diff = ...
    #     substitute_diff = ...
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END




def pawssible_patches(start, goal, limit):
    # print("hello")
    """A diff function that computes the edit distance from START to GOAL."""
    if len(start)==0 and len(goal)==0 :
        return 0 
    if len(start)==0 or len(goal)==0 : 
        if limit == 0: return 1000000
        return len(start) if len(goal) == 0 else len(goal)
    elif start[0] == goal[0] : return pawssible_patches(start[1:], goal[1:], limit)
    else:
        if limit == 0: return 1000000
        add_diff = pawssible_patches(start, goal[1:], limit-1) + 1
        remove_diff = pawssible_patches(start[1:], goal, limit-1) + 1
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1) + 1
        res = min(min(add_diff, remove_diff), substitute_diff)
        return res


# big_limit = 10
# print(pawssible_patches('rose', 'arose', 10))
# print(pawssible_patches("purng", "purring", big_limit))
# print(pawssible_patches("ckiteus", "kittens", big_limit))
# print(pawssible_patches("cats", "scat", big_limit))
# limit = 2
# print(pawssible_patches("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit))
# print(pawssible_patches("ckite", "kittens", limit))

def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    num_type_right = 0
    for i in range(0, len(typed)):
        if typed[i] == prompt[i]: num_type_right += 1
        else : break
    process = num_type_right / len(prompt)
    message = {'id': user_id, 'progress': process}
    send(message)
    print(process)
    return
    # END PROBLEM 8
    
# print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
# typed = ['I', 'have', 'begun']
# prompt = ['I', 'have', 'begun', 'to', 'type']
# print_progress({'id': 1, 'progress': 0.6})
# report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
# report_progress(['I', 'begun'], prompt, 2, print_progress)
# report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]

def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]

def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]

def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]

def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]

def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    def count_time(lst):
        lst_new = []
        for i in range(1, len(lst)):
            item = lst[i] - lst[i-1]
            lst_new.append(item)
        return lst_new
    lst = []
    for time_player in times_per_player:
        # print(time_player)
        lst.append(count_time(time_player))
    return game(words, lst)    
    # END PROBLEM 9

# print(count_time([1, 4, 6, 7]))

p = [[1, 4, 6, 7], [0, 4, 6, 9]]
words = ['This', 'is', 'fun']
game1 = time_per_word(p, words)
print(all_words(game1))
print(all_times(game1))

p = [[0, 2, 3], [2, 4, 7]]
game2 = time_per_word(p, ['hello', 'world'])
print(word_at(game2, 1))
print(all_times(game2))
print(time(game2, 0, 1))

def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    res = []
    for item in player_indices:
        res.append([])   
    for index1 in word_indices:
        min_time = 1000000
        min_player = -1
        for index2 in player_indices:
            cur_time = time(game, index2, index1)
            if cur_time < min_time: 
                min_time = cur_time
                min_player = index2
        res[min_player].append(word_at(game, index1))
    # print(res)    
    return res
    # END PROBLEM 10

# fastest_words(game)


# p0 = [2, 2, 3]
# p1 = [6, 1, 2]
# fastest_words(game(['What', 'great', 'luck'], [p0, p1]))

# p2 = [4, 3, 1]
# fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))