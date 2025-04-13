import random

# Determines if there is a possible three-in-a-row
def four_in_a_row(grid, turn):
    win = set([(0, turn, turn, turn), (turn, 0, turn, turn), (turn, turn, 0, turn), (turn, turn, turn, 0)])
    for x in range(2):
        for y in range(5):
            r = (grid[y][x], grid[y][x + 1], grid[y][x + 2], grid[y][x + 3])
            if r in win:
                return True
    for x in range(5):
        for y in range(2):
            r = (grid[y][x], grid[y + 1][x], grid[y + 2][x], grid[y + 3][x])
            if r in win:
                return True
    for x in range(2):
        for y in range(2):
            r = (grid[y][x], grid[y + 1][x + 1], grid[y + 2][x + 2], grid[y + 3][x + 3])
            if r in win:
                return True
    for x in range(2):
        for y in range(3, 5):
            r = (grid[y][x], grid[y - 1][x + 1], grid[y - 2][x + 2], grid[y - 3][x + 3])
            if r in win:
                return True
    return False

# Blocks opponent from having a 4-in-a-row
def block_opponent(grid, turn):
    opp = 3 - turn
    win = set([(0, opp, opp, opp), (opp, 0, opp, opp), (opp, opp, 0, opp), (opp, opp, opp, 0)])
    for x in range(2):
        for y in range(5):
            r = (grid[y][x], grid[y][x + 1], grid[y][x + 2], grid[y][x + 3])
            if r in win:
                for i in range(4):
                    if r[i] == 0:
                        return (x + i, y)
    for x in range(5):
        for y in range(2):
            r = (grid[y][x], grid[y + 1][x], grid[y + 2][x], grid[y + 3][x])
            if r in win:
                for i in range(4):
                    if r[i] == 0:
                        return (x, y + i)
    for x in range(2):
        for y in range(2):
            r = (grid[y][x], grid[y + 1][x + 1], grid[y + 2][x + 2], grid[y + 3][x + 3])
            if r in win:
                for i in range(4):
                    if r[i] == 0:
                        return (x + i, y + i)
    for x in range(2):
        for y in range(3, 5):
            r = (grid[y][x], grid[y - 1][x + 1], grid[y - 2][x + 2], grid[y - 3][x + 3])
            if r in win:
                for i in range(4):
                    if r[i] == 0:
                        return (x + i, y - i)
    return ""

#Stores possible moves
moves = {}

# All possibilities for next move
def possibilities(grid, move):
    if four_in_a_row(grid, 3 - move):
        if four_in_a_row(grid, move):
            p = block_opponent(grid, 3 - move)
        else:
            p = block_opponent(grid, move)
        newgrid = []
        for y in range(5):
            row = []
            for x in range(5):
                if x == p[0] and y == p[1]:
                    row.append(move)
                else:
                    row.append(grid[y][x])
            newgrid.append(tuple(row))
        moves[grid] = [p]
        return tuple(newgrid), p
    if grid in moves:
        if len(moves[grid]) == 0:
            return "Loss", "Loss"
        r = moves[grid][random.randrange(len(moves[grid]))]
        newgrid = []
        for y in range(5):
            row = []
            for x in range(5):
                if x == r[0] and y == r[1]:
                    row.append(move)
                else:
                    row.append(grid[y][x])
            newgrid.append(tuple(row))
        return tuple(newgrid), r
    else:
        poss = []
        for x in range(5):
            for y in range(5):
                if grid[y][x] == 0:
                    poss.append((x, y))
        if len(poss) == 0:
            return "Draw", "Draw"
        moves[grid] = poss
        r = poss[random.randrange(len(poss))]
        newgrid = []
        for y in range(5):
            row = []
            for x in range(5):
                if x == r[0] and y == r[1]:
                    row.append(move)
                else:
                    row.append(grid[y][x])
            newgrid.append(row)
        return tuple(map(tuple, newgrid)), r

# Simulates game
def game(grid, player):
    g, m = possibilities(grid, player)
    if g == "Loss":
        moves[grid] = [i for i in moves[grid] if i != m]
        return 0
    elif g == "Draw":
        return 0
    n = 3 - player
    if four_in_a_row(g, n):
        moves[grid] = [i for i in moves[grid] if i != m]
        return 0
    else:
        return game(g, n)

# Starting Text
print("\nHi! My name is Max, and this is a tic-tac-toe simulator. For starters, here are the rules:\n")
print("   1. There is a 5x5 board, you plays as X and the computer plays as O.")
print("   2. You will alternate turns, placing your symbol into any free cell.")
print("   3. The first to create a 4-in-a-row (in any direction) wins.")
print("\nSo you might now be wondering, \"Max, where is the game? I want to play!\"")
print("You see, the computer has been preparing while you've been reading this, playing against itself 250 thousand times. Let me explain.")
print("\n\nAt first, your machine has no idea which moves are good and which are bad, only starting with 2 rules it must follow:")
print("\n   1. If you have a potential 4-in-a-row, you should complete it")
print("   2. If your opponent has a potential 4-in-a-row, you should block it\n")
print("Since it doesn't know anything else, it starts making random moves.")
print("However, once the machine loses against itself, it learns that it shouldn't have played that previous move.")
print("It remembers that mistake, and the next time it sees the same position, it doesn't repeat it.")
print("\nAfter 250,000 games, it has been through a ton of positions, knowing what to do for each.")
print("Now, is it perfect? Absolutely not. It can still make many mistakes. But it will, on average, win more than what it was 250,000 rounds ago.")
print("This idea of learning from mistakes is called \"Machine Learning\", and is the basis of all major AI on earth today.")
print("Good luck, and let's see if you can beat my AI!")

# Repeats 500,000 times
for _ in range(250000):
    game(((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)), 1)

print("\nAI is done training! You make the first move:\n")

def display(grid):
    print("   1 2 3 4 5")
    print("  -----------")
    n = 1
    for i in grid:
        s = str(n) + " |"
        for j in i:
            if j == 0:
                s += " "
            elif j == 1:
                s += "X"
            else:
                s += "O"
            s += "|"
        n += 1
        print(s)
        print("  -----------")
    print("\n")

# Let's the user play the game.
def play(grid = ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0))):
    if grid == "Game resigned.":
        return "Game resigned."

    # Your Turn
    r = "Invalid"
    while r == "Invalid":
        try:
            r = input("Enter move (format as \"x, y\", type \"resign\" to resign):   ")
            if r.lower() == "resign":
                return "Game resigned."
            if "," in r:
                r = r.split(",")
            else:
                r = r.split()
            r[0], r[1] = int(r[0]) - 1, int(r[1]) - 1
            if r[0] >= 5 or r[1] >= 5 or r[0] < 0 or r[1] < 0:
                print("Error: Invalid board position\n")
                display(grid)
                r = "Invalid"
            elif grid[r[1]][r[0]] != 0:
                print("Board spot alrady taken!\n")
                display(grid)
                r = "Invalid"
        except:
            print("Error: Invalid board position\n")
            r = "Invalid"
            display(grid)

    # AI's Turn
    n = []
    for y in range(5):
        row = []
        for x in range(5):
            if x == r[0] and y == r[1]:
                row.append(1)
            else:
                row.append(grid[y][x])
        n.append(tuple(row))
    if four_in_a_row(n, 2):
        r = block_opponent(n, 1)
        newgrid = []
        for y in range(5):
            row = []
            for x in range(5):
                if x == r[0] and y == r[1]:
                    row.append(2)
                else:
                    row.append(n[y][x])
            newgrid.append(tuple(row))
        display(tuple(newgrid))
        return "The AI found a 4-in-a-row, you lose."
    newgrid = tuple(n)
    newgrid = possibilities(newgrid, 2)[0]
    if newgrid == "Loss":
        display(n)
        return "Bot Resigns, You Win!"
    if newgrid == "Draw":
        display(n)
        return "The game is a draw."
    if four_in_a_row(newgrid, 1):
        display(n)
        return "Bot Resigns, You Win!"
    display(newgrid)
    return play(newgrid)

# Loop to play the game as much as you want
while True:
    display(((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)))
    print(play())
    print("\nDo you want to play again? (Type \"no\" to exit)")
    s = input()
    if s.lower() == "no":
        break
