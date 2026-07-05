from datetime import datetime

AUTH_LOG = "auth_events.log"
FILE_LOG = "file_events.log"
KEY_MARKERS = ("SUCCESS LOGIN", ".locked", "READ_ME")

# Step 1: Read all lines from both log files
with open(AUTH_LOG, "r") as f:
    auth_lines = f.readlines()
with open(FILE_LOG, "r") as f:
    file_lines = f.readlines()

# Step 2: Merge events from both sources into one list
events = [line.rstrip("\n") for line in auth_lines + file_lines if line.strip()]

# Step 3: Sort events chronologically by the date/time at the start of each line
def event_time(line):
    return datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")

events.sort(key=event_time)

# Step 4: Flag key events that indicate compromise or ransomware activity
def is_key_event(line):
    return any(marker in line for marker in KEY_MARKERS)

# Step 5: Print the merged timeline
print("=== Incident Timeline ===")
for line in events:
    marker = " *** KEY EVENT ***" if is_key_event(line) else ""
    print(f"{line}{marker}")

# Step 6: Calculate dwell time from first SUCCESS LOGIN to first .locked file
first_login = next(event_time(line) for line in events if "SUCCESS LOGIN" in line)
first_locked = next(event_time(line) for line in events if ".locked" in line)
dwell_minutes = (first_locked - first_login).total_seconds() / 60

print()
print(f"Dwell time: {dwell_minutes:.1f} minutes (first SUCCESS LOGIN to first .locked file)")
