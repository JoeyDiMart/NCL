import requests

BASE = "https://00f667152b75539b723661e2698cd30f-jackpot.web.cityinthe.cloud"

MULTIPLIER = 0x5DEECE66D
INCREMENT = 0xB
MASK = (1 << 48) - 1

def next_seed(seed):
    return (seed * MULTIPLIER + INCREMENT) & MASK

session = requests.Session()

# Buy 2 tickets to recover seed
r1 = session.post(f"{BASE}/buy", json={"numbers": [0,0,0,0,0,0]})
uuid1 = r1.json()['ticket']['uuid']
print(f"UUID1: {uuid1}")

r2 = session.post(f"{BASE}/buy", json={"numbers": [0,0,0,0,0,0]})
uuid2 = r2.json()['ticket']['uuid']
print(f"UUID2: {uuid2}")

print("Brute forcing...")
found_seed = None
for low16 in range(1 << 16):
    seed1 = (uuid1 << 16) | low16
    seed2 = next_seed(seed1)
    if (seed2 >> 16) == uuid2:
        found_seed = seed2
        break

if found_seed is None:
    print("Not found!")
else:
    # Skip 1 seed for the winning ticket's UUID generation
    s = next_seed(found_seed)  # UUID of ticket 3 (the one we're about to buy)
    predicted = []
    for _ in range(6):
        s = next_seed(s)
        predicted.append((s >> 17) % 100)
    print(f"Predicted winning: {predicted}")

    r3 = session.post(f"{BASE}/buy", json={"numbers": predicted})
    win_uuid = r3.json()['ticket']['uuid']
    print(f"Winning ticket UUID: {win_uuid}")

    r4 = session.post(f"{BASE}/redeem", json={"uuid": win_uuid})
    print("Result:", r4.json())