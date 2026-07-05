import re
from collections import defaultdict

LOG_FILE = "network_traffic.log"

# Step 1: Open and read the network traffic log
with open(LOG_FILE, "r") as f:
    lines = f.readlines()

# Step 2: Parse each line into timestamp, source IP, and destination IP:port
line_pattern = re.compile(
    r"(\d{2}:\d{2}:\d{2})\s+(\d+\.\d+\.\d+\.\d+)\s+->\s+(\d+\.\d+\.\d+\.\d+:\d+)"
)
pair_timestamps = defaultdict(list)

for line in lines:
    match = line_pattern.search(line)
    if match:
        timestamp, source_ip, dest = match.groups()
        pair = f"{source_ip} -> {dest}"
        pair_timestamps[pair].append(timestamp)

# Step 3: Count connections per (source -> destination:port) pair
pair_counts = {pair: len(timestamps) for pair, timestamps in pair_timestamps.items()}

# Step 4: Find the pair with the most connections
top_pair = max(pair_counts, key=pair_counts.get)
top_count = pair_counts[top_pair]
top_timestamps = pair_timestamps[top_pair]

# Step 5: Compute average seconds between consecutive exchanges
def to_seconds(timestamp):
    hours, minutes, seconds = map(int, timestamp.split(":"))
    return hours * 3600 + minutes * 60 + seconds

seconds_list = [to_seconds(ts) for ts in top_timestamps]
gaps = [seconds_list[i + 1] - seconds_list[i] for i in range(len(seconds_list) - 1)]
avg_gap = sum(gaps) / len(gaps) if gaps else 0

# Step 6: Print the beaconing suspect and its connection timeline
print("=== Beaconing Suspect ===")
print(f"Pair: {top_pair}")
print(f"Connections: {top_count}")
print(f"Timestamps: {top_timestamps}")
print(f"Average time between exchanges: {avg_gap:.1f} seconds")
