import os
import sys
import time
import random
import multiprocessing
from bitcoin import random_key, encode_privkey, privtopub, compress, pubtoaddr

def generate_key():
    priv_key = random_key()
    pub_key = compress(privtopub(priv_key))
    address = pubtoaddr(pub_key)
    wif = encode_privkey(priv_key, 'wif_compressed')
    return address, wif, priv_key

def worker(target, queue, stop_event):
    while not stop_event.is_set():
        address, wif, priv = generate_key()
        if address.startswith(target):
            result = f"\n🎯 MATCH FOUND!\nAddress: {address}\nWIF: {wif}\nHex: {priv}\n"
            queue.put(result)
            stop_event.set()
            return

def main():
    if len(sys.argv) != 2:
        print("Usage: python btc2_vanity_search.py <VanityPrefix>")
        print("Example: python btc2_vanity_search.py 1BTC2")
        sys.exit(1)

    target = sys.argv[1]
    num_threads = 18  # You wanted 18 threads for speed

    print(f"🚀 Searching for BTC2 compressed address starting with: {target}")
    print(f"🧵 Using {num_threads} threads...\n")

    manager = multiprocessing.Manager()
    queue = manager.Queue()
    stop_event = multiprocessing.Event()
    processes = []

    start = time.time()
    for _ in range(num_threads):
        p = multiprocessing.Process(target=worker, args=(target, queue, stop_event))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    while not queue.empty():
        print(queue.get())

    duration = round(time.time() - start, 2)
    print(f"✅ Done in {duration} seconds.")

if __name__ == '__main__':
    main()
