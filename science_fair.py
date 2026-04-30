import random

# Students registered for Robotics
robotics = {"Amit", "Riya", "Kiran", "Neha"}

# Students registered for AI Workshop
ai_workshop = {"Riya", "Neha", "Rahul", "Pooja"}

# Find students who registered for both events
both_events = robotics.intersection(ai_workshop)
print("Students registered for both events:", both_events)

# Find students who registered only for Robotics
only_robotics = robotics.difference(ai_workshop)
print("Students registered only for Robotics:", only_robotics)

# Combine all participants (no duplicates)
all_participants = robotics.union(ai_workshop)
print("All participants:", all_participants)

# Add late registration students
all_participants.add("Sneha")
all_participants.add("Vikram")
print("After late registrations:", all_participants)

# Remove a student who cancelled
all_participants.remove("Rahul")
print("After cancellation:", all_participants)

# Randomly select one student for a special prize
winner = random.choice(list(all_participants))
print("Special prize winner:", winner)

# Finally clear the participant list after the event
all_participants.clear()
print("Participant list after event:", all_participants)