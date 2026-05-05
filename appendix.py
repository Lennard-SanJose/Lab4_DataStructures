from collections import defaultdict, Counter, deque

# --- GLOBAL SETUP ---
SEED_NUM = 7 
STUDENT_MAJOR = "BSECE"
FAVORITE_ARTIST = "BINI"
LOCAL_HAZARD = "FLOOD"
CONTROL_NUM = max(3, SEED_NUM)

# --- EXERCISE 1: Unstructured Data Aggregator ---
print("--- Exercise 1 Output ---")
stream = [
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", STUDENT_MAJOR),
    ("TUP Taguig", "BSECE"),
    ("TUP Manila", "BSECE")
]

# Data Expansion: Add exactly (CONTROL_NUM + 3) = 10 custom tuples
for i in range(CONTROL_NUM + 3):
    stream.append(("TUP Manila", "BSIT"))

# Phase 1: Aggregation
aggregated_data = defaultdict(list)
for campus, program in stream:
    aggregated_data[campus].append(program)

# Phase 2: Frequency Analysis
manila_counter = Counter(aggregated_data["TUP Manila"])
top_program, frequency = manila_counter.most_common(1)[0]

print(f"Expanded Stream Length: {len(stream)}")
print(f"Total Manila Apps: {len(aggregated_data['TUP Manila'])}")
print(f"Top Manila Program: {top_program} ({frequency} counts)\n")


# --- EXERCISE 2: Jaccard Similarity Engine ---
print("--- Exercise 2 Output ---")
festival = {"Ben&Ben", "SB19", "Bini", "Eraserheads", FAVORITE_ARTIST, "Zild", f"Indie Artist {CONTROL_NUM}"}
user_a = {"Ben&Ben", "Bini", "Maki", "Dionela", FAVORITE_ARTIST}
user_b = {"SB19", "Eraserheads", "Zild", f"Indie Artist {CONTROL_NUM}", "Parokya ni Edgar"}

# Data Expansion: Add exactly CONTROL_NUM = 7 new artists
new_artists = {f"Artist_{i}" for i in range(CONTROL_NUM)}
festival.update(new_artists)

def get_jaccard(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return (len(intersection) / len(union)) * 100, len(intersection), len(union)

sim_a, inter_a, union_a = get_jaccard(user_a, festival)
sim_b, _, _ = get_jaccard(user_b, festival)
dealbreakers = user_a.difference(festival)

print(f"Total Artists in Festival: {len(festival)}")
print(f"User A Jaccard: {sim_a:.2f}%")
print(f"User B Jaccard: {sim_b:.2f}%")
print(f"User A Dealbreakers: {dealbreakers}\n")


# --- EXERCISE 3: Stateful Sliding Window Filter ---
print("--- Exercise 3 Output ---")
buffer = deque(maxlen=5)
burst = [
    (CONTROL_NUM, "WEATHER"),
    (CONTROL_NUM + 1, "TRAFFIC"),
    (CONTROL_NUM + 2, "WEATHER"),
    (CONTROL_NUM + 3, "WEATHER"),
    (CONTROL_NUM + 4, LOCAL_HAZARD),
    (CONTROL_NUM + 5, "WEATHER"),
    (CONTROL_NUM + 6, "TRAFFIC")
]

# Data Expansion: Add (CONTROL_NUM + 2) = 9 custom alerts
last_ts = burst[-1][0]
for i in range(1, CONTROL_NUM + 3):
    burst.append((last_ts + i, "SYSTEM_CHECK"))

# Algorithm: Sliding Window
for ts, cat in burst:
    current_categories = [item[1] for item in buffer]
    counts = Counter(current_categories)
    
    # Spam Rule: Reject if category exists 2 or more times
    if counts[cat] < 2:
        buffer.append((ts, cat))

final_sum = sum(item[0] for item in buffer)
print(f"Total Burst Size: {len(burst)}")
print(f"Final Deque Length: {len(buffer)}")
print(f"Sum of Timestamps: {final_sum}")
print(f"Exact Deque: {list(buffer)}")