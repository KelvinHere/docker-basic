import numpy as np

while True:
    num = np.random.randint(100)
    print(f"\nRandom number created inside docker container = {num}")
    again = input("Enter Y to generate another or any other key to quit - ")
    if not again:
        break
    if again[0].lower() != 'y':
        break