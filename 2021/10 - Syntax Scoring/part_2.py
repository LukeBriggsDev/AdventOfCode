"""--- Part Two ---

Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?"""
import os 
def autocomplete(input_file):
    corrupt_lines = []
    autocompletes = []
    score_map = {')':1, '}':3, '>':4, ']':2}
    with open(input_file) as f:
        line_no = -1
        for line in f:
            line_no += 1
            block_close = {'(':')', '{':'}', '<':'>', '[':']'}
            blocks = []
            for character in line.strip():
                if character in block_close.keys():
                    blocks.append(character)
                elif character != block_close[blocks.pop()]:
                    corrupt_lines.append(line_no)
                    break
            if line_no not in corrupt_lines:
                autocompletes.append([block_close[x] for x in blocks][::-1])
    
    scores = [0 for _ in autocompletes]

    for i in range(len(autocompletes)):
        for character in autocompletes[i]:
            scores[i] *= 5
            scores[i] += score_map[character]

    return sorted(scores)[len(scores)//2]




if __name__ == "__main__":
    print(autocomplete((os.path.dirname(__file__) + "/input.txt")))