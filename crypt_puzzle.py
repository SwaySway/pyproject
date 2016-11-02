from itertools import permutations

# demo code to dissect
def solve(puzzle):
    words = [w for w in puzzle.split() if w.isalpha()]
    print(words)
    nonzeros = {w[0] for w in words}
    others = {a for a in ''.join(words) if a not in nonzeros}
    chars = [ord(c) for c in nonzeros] + [ord(c) for c in others]
    assert len(chars) < 10, 'Too many letters'
    for guess in permutations('0123456789', len(chars)):
        if '0' not in guess[:len(nonzeros)]:
            print(guess[:len(nonzeros)])
            equation = puzzle.translate(dict(zip(chars, guess)))
            if eval(equation):
                return puzzle, equation


if __name__=='__main__':
    print('\n'.join(solve("send + more == money")))
