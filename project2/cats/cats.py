"""Typing test implementation"""

from concurrent.futures import process
from errno import ESTALE
from os import times
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    if not paragraphs:
        return ""
    elif select(paragraphs[0]) and k == 0:
        return paragraphs[0]
    else:
        if select(paragraphs[0]):
            return choose(paragraphs[1:],select,k - 1)
        else:
            return choose(paragraphs[1:],select,k)


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
    # END PROBLEM 2
    def exit_or_not(paragraph):
        low_paragraph_without_pun = split(lower(remove_punctuation(paragraph)))
        for topic_element in topic:
            for paragraph_element in low_paragraph_without_pun:
                if topic_element == paragraph_element:
                    return True
        return False
    return exit_or_not


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
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    i = 0
    true_num ,total_num = 0 , len(typed_words)
    loop_number = min(len(typed_words),len(reference_words))
    while i < loop_number:
        if typed_words[i] == reference_words[i]:
            true_num += 1
        i += 1
    if total_num == 0:
        return 0.0
    else:
        true_rate = true_num / total_num * 100
        return true_rate 



def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    word_num = len(typed) / 5
    speed = word_num * (60 / elapsed)
    return speed


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        lowest_diff = 100000
        choosen_word = user_word
        for valid_word in valid_words:
            differ = diff_function(user_word,valid_word,limit)
            if differ <= limit and differ < lowest_diff:
                choosen_word = valid_word
                lowest_diff = differ
        return choosen_word


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    def shifts(start,goal,limit,differ):
        if not goal and not start:
            return differ
        elif differ > limit:
            return differ
        else:
            if not start:
                return shifts(start,goal[1:],limit,differ + 1)
            elif not goal:
                return shifts(start[1:],goal,limit,differ + 1)
            else:
                if start[0] != goal[0]:
                    return shifts(start[1:],goal[1:],limit,differ + 1)
                else:
                    return shifts(start[1:],goal[1:],limit,differ)
    return shifts(start,goal,limit,0)

def pawssible_patches(start, goal, limit):
    def process(start,goal,limit,differ):
        if not start and not goal:
            return differ
        elif differ > limit:
            return differ
        else:
            if not start:
                return process(start,goal[1:],limit,differ + 1)
            elif not goal:
                return process(start[1:],goal,limit,differ + 1)
            else:
                if start[0] != goal[0]:
                    add_diff = process(start,goal[1:],limit,differ + 1)
                    remove_diff = process(start[1:],goal,limit,differ + 1)
                    substitute_diff = process(start[1:],goal[1:],limit,differ + 1)
                    return min(add_diff,remove_diff,substitute_diff)
                else:
                    return process(start[1:],goal[1:],limit,differ)
    return process(start,goal,limit,0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    i = 0
    true_num,total_num = 0,len(prompt)
    while i < len(typed):
        if typed[i] == prompt[i]:
            true_num += 1
        else:
            break
        i += 1
    Progress = true_num / total_num
    info = {'id': user_id,'progress':Progress}
    send(info)
    return Progress


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


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
    # END PROBLEM 9
    players = []
    for player in times_per_player:
        i = 0
        times = []
        while i < len(player):
            if i != 0:
                times.append(player[i] - player[i - 1])
            i += 1
        players.append(times)
    return game(words,players)

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
    # END PROBLEM 10
    fastest_words = []
    fastest_users = []
    for word_index in word_indices:
        fastest_user = 0
        fastest_time = time(game,0,word_index)
        for player_index in player_indices:
            word_time = time(game,player_index,word_index)
            if word_time < fastest_time:
                fastest_user = player_index
                fastest_time = word_time
        fastest_users.append(fastest_user)
    for player_index in player_indices:
        player = []
        fastest_words.append(player)
    for word_index in word_indices:
        fastest_words[fastest_users[word_index]].append(word_at(game,word_index))
    return fastest_words

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

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)