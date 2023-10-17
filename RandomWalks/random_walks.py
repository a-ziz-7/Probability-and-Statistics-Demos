import random


def randomWalk(arg):

    particle_pos = 0
    x = arg
    arr = []

    while x > 0:
        if particle_pos not in arr:
            arr.append(particle_pos)
        rand = random.randint(0, 1)
        if rand == 1:
            particle_pos += 1
        else:
            particle_pos -= 1
        x -= 1
    arr.sort()
    print(f"Random walk ({arg}) covered: {arr[0]}  ---  {arr[len(arr)-1]}")
    print(f"Particle position is {particle_pos}")


def monkey_and_cliff(pos_of_monkey=1, seconds=10, probability=60, simulation=False):
    pos = pos_of_monkey
    sec = seconds
    sec_counter = 0
    options = ([-1]*probability)
    options.extend([1]*(100-probability))
    while sec != sec_counter and pos > 0:
        pos += random.choice(options)
        sec_counter += 1
        # if sec_counter % 10 == 0:
        #     print(pos, "---", sec_counter)
    print(("Expected: to " +
          ("survive" if probability <= 50 else f"die in {round(pos_of_monkey/((probability/100)-((100-probability)/100)))}") +
           "\nMonkey "+(f"survived at {pos}" if pos != 0 else "died") + " after " + str(sec_counter) + " seconds starting at " +
           str(pos_of_monkey) + " with p=" + str(probability)+"\n") if not simulation else "", end="")
    print((str(pos) + ((" After: " + str(sec_counter) + " seconds\n") if pos == 0 else "\n")) if simulation else "", end="")
    return pos != 0


def monkey_and_cliff_simulation(amount_of_runs=100, pos_of_monkey=1, seconds=10, probability=60):
    count_alive = 0
    count_dead = 0
    for i in range(amount_of_runs):
        if monkey_and_cliff(pos_of_monkey, seconds, probability, True):
            count_alive += 1
        else:
            count_dead += 1
    print(f"{amount_of_runs} runs\n" +
          f"Starting at: {pos_of_monkey}\n" +
          f"Probability to step towards the cliff: {probability}%\n" +
          f"Duration of each run: {seconds}\n" +
          f"{count_alive} monkeys survived\n" + 
          f"{count_dead} monkeys dies")


total_count = 0

def gambler_ruin(a=1, b=1, probability=50, simulation=False):
    options = ([1]*probability)
    options.extend([-1]*(100-probability))
    A = a
    B = b
    counter = 0
    while a > 0 and b > 0:
        c = random.choice(options)
        if c == 1:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
        counter += 1
    if not simulation:
        if a == 0:
            print(
                f"Player B won starting with {B} and p={100-probability} and player A lost starting with {A} and q={probability}")
        else:
            print(
                f"Player A won starting with {A} and p={probability} and player B lost starting with {B} and q={100-probability}")
    print(f"After {counter} Games Final Score: A={a} : B={b}")
    global total_count
    total_count += counter
    return 1 if a > 0 else -1


def gamblers_ruin_simulation(amount_of_runs=1, a=1, b=1, probability=50):
    ca = 0
    cb = 0
    for i in range(amount_of_runs):
        if 1 == gambler_ruin(a, b, probability, True):
            ca += 1
        else:
            cb += 1
        print()
    print(f"A won: {ca} times\nB won: {cb} times")
    print(f"Total amoun of games played: {total_count}")


def default_run():
    randomWalk(100000)
    print()
    monkey_and_cliff(pos_of_monkey=10, seconds=200, probability=50)
    print()
    gambler_ruin(a=1000, b=1000, probability=50)


def main():
    # default_run()
    # monkey_and_cliff_simulation(10000, 10, 200, 50)
    gamblers_ruin_simulation(20, a=1000, b=1000, probability=50)


if __name__ == "__main__":
    main()
