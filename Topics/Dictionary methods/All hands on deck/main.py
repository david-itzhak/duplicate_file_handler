print(sum([{**{str(i): i for i in range(2, 11)}, **{'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}}[input()]
           for _ in range(6)]) / 6)

