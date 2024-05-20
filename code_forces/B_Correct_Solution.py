alice_input = [int(x) for x in input()]
bob_ans = [int(x) for x in input()]

alice_input.sort()

idx = 0
while alice_input[idx] == 0 and idx < len(alice_input) - 1:
    idx += 1
alice_input[idx], alice_input[0] = alice_input[0], alice_input[idx]

if alice_input == bob_ans:
    print("OK")
else:
    print("WRONG_ANSWER")
