# Simple Reflex Vacuum Cleaner Agent

def vacuum_agent(location, status):

    if status == "Dirty":
        return "Suck"
    elif location == "Left":
        return "Right"
    else:
        return "Left"

def display_environment(left_room, right_room, vacuum_location):

    left = f"[{left_room}]"
    right = f"[{right_room}]"

    if vacuum_location == "Left":
        left = f"[Vacuum, {left_room}]"
    else:
        right = f"[Vacuum, {right_room}]"

    print(f"{left}  {right}")

def run_vacuum_world(left_room, right_room, start_location, steps=10):

    location = start_location

    print("\nINITIAL STATE")
    display_environment(left_room, right_room, location)

    for step in range(1, steps + 1):

        if location == "Left":
            status = left_room
        else:
            status = right_room

        percept = (location, status)

        action = vacuum_agent(location, status)

        print(f"\nStep {step}")
        print("Percept:", percept)
        print("Action :", action)

        if action == "Suck":
            if location == "Left":
                left_room = "Clean"
            else:
                right_room = "Clean"

        elif action == "Right":
            location = "Right"

        elif action == "Left":
            location = "Left"

        display_environment(left_room, right_room, location)

        if left_room == "Clean" and right_room == "Clean":
            print("\n✔ Goal Achieved: Both rooms are clean!")
            break

print("===== PERCEPT SEQUENCE 1 =====")

run_vacuum_world(
    left_room="Dirty",
    right_room="Dirty",
    start_location="Left"
)

print("\n\n===== PERCEPT SEQUENCE 2 =====")

run_vacuum_world(
    left_room="Dirty",
    right_room="Dirty",
    start_location="Right"
)