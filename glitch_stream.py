import random, time, os, sys

W = 30            # tunnel width
player = W // 2   # start position
speed = 0.08      # lower = faster
score = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input():
    import tty, termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    except:
        ch = ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

clear()
print("⚡ GLITCH STREAM ⚡")
print("Use A/D to move | Avoid X | Press ENTER to start")
input()

try:
    while True:
        clear()
        score += 1

        # Tunnel slowly shifts left/right
        offset = random.randint(-1, 1)

        # Random obstacles
        obstacles = [" "] * W
        if random.random() < 0.25:
            obs_pos = random.randint(0, W-1)
            obstacles[obs_pos] = "X"

        # Render tunnel and player
        row = "".join(obstacles)
        player = max(0, min(W-1, player))

        row_list = list(row)
        row_list[player] = "●"
        print("".join(row_list))
        print(f"Score: {score}")

        # Non-blocking input
        import select
        dr, _, _ = select.select([sys.stdin], [], [], speed)
        if dr:
            ch = get_input()
            if ch.lower() == 'a': player -= 1
            elif ch.lower() == 'd': player += 1

        # Collision
        if obstacles[player] == "X":
            clear()
            print("💥 GAME OVER 💥")
            print("Your Score:", score)
            break

        # Speed up
        speed = max(0.02, speed * 0.995)

        # Tunnel bending
        if offset != 0:
            player += offset

except KeyboardInterrupt:
    print("\nQuit")
