import time
import sys

def print_lyrics():
    lyrics = [
        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun torrun khud se jo thay waaday",
        "Ke ab yeh ishq nibhahna nahi",
        "Mein morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nahi?"
    ]

    # FIXED: 8 lines → 8 delays (your list had only 7)
    delays = [
        0.3, 0.3, 0.4, 0.3,
        0.3, 0.3, 0.8, 0.5   # last delay added
    ]

    print("\n Pal Pal : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)   # typing speed
        print()
        time.sleep(delays[i])  # now properly aligned

print_lyrics()
