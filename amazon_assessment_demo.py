def cellCompete(states, days):
    states = states[:]
    for _ in range(days):
        prev = 0
        for i in range(len(states)):
            x = states[i]
            if i+1 == len(states):
                post = 0
            else:
                post = states[i+1]
            if post == prev:
                states[i] = 0
            else:
                states[i] = 1
            prev = x
    return states


print(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))
