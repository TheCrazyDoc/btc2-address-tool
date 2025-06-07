import os
import ecdsa
import base58
import hashlib
import csv
from datetime import datetime

def generate_private_key():
    return os.urandom(32)

def private_key_to_wif_compressed(private_key_bytes):
    extended_key = b'\x80' + private_key_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    return base58.b58encode(extended_key + checksum).decode()

def private_key_to_compressed_pubkey(private_key_bytes):
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    return prefix + x.to_bytes(32, 'big')

def pubkey_to_btc2_address(pubkey_bytes):
    sha256 = hashlib.sha256(pubkey_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    prefixed = b'\x00' + ripemd160  # BTC2 uses same version prefix as Bitcoin
    checksum = hashlib.sha256(hashlib.sha256(prefixed).digest()).digest()[:4]
    return base58.b58encode(prefixed + checksum).decode()

def generate_wallets(n=10, output_file="btc2_wallets.csv"):
    wallets = []
    for _ in range(n):
        priv = generate_private_key()
        wif = private_key_to_wif_compressed(priv)
        pub = private_key_to_compressed_pubkey(priv)
        addr = pubkey_to_btc2_address(pub)
        wallets.append({
            "BTC2 Address (Compressed)": addr,
            "Private Key (WIF Compressed)": wif,
            "Private Key (Hex)": priv.hex()
        })

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=wallets[0].keys())
        writer.writeheader()
        writer.writerows(wallets)

    print(f"\n✅ {n} BTC2 Wallets saved to: {output_file}")

# Run the generator
if __name__ == "__main__":
    generate_wallets(n=10)
