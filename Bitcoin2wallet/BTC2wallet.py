import os
import ecdsa
import base58
import hashlib

def generate_private_key():
    return os.urandom(32)

def private_key_to_wif_compressed(private_key_bytes):
    extended_key = b'\x80' + private_key_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def private_key_to_compressed_public_key(private_key_bytes):
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    return prefix + x.to_bytes(32, 'big')

def pubkey_to_btc2_address_compressed(pubkey_bytes):
    sha256 = hashlib.sha256(pubkey_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    prefixed = b'\x00' + ripemd160  # BTC2 uses Bitcoin-style prefix
    checksum = hashlib.sha256(hashlib.sha256(prefixed).digest()).digest()[:4]
    address = base58.b58encode(prefixed + checksum)
    return address.decode()

# Main wallet generation
private_key = generate_private_key()
wif_compressed = private_key_to_wif_compressed(private_key)
compressed_pubkey = private_key_to_compressed_public_key(private_key)
btc2_address = pubkey_to_btc2_address_compressed(compressed_pubkey)

# Print results
print("\n✅ BTC2 Compressed Paper Wallet")
print("-------------------------------")
print("BTC2 Address:", btc2_address)
print("Private Key (WIF Compressed):", wif_compressed)
print("Private Key (Hex):", private_key.hex())
