## This iteration only generates one address and the script stops
# gen_auto.py continuously generates wallets non stop forever.

import os
import ecdsa
import hashlib
import base58
from mnemonic import Mnemonic
import bech32

def generate_keys_and_addresses(mnemonic_length):
    private_key = os.urandom(32)
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    public_key = sk.get_verifying_key().to_string()

    seed = hashlib.sha256(private_key).digest()
    mnemonic_phrase = Mnemonic("english").to_mnemonic(seed) if mnemonic_length == "random" else Mnemonic("english").generate(strength=mnemonic_length)

    ripemd160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
    legacy_address = base58.b58encode_check(b'\x00' + ripemd160)
    segwit_address = bech32.encode('bc', 0, ripemd160)

    return private_key, public_key, mnemonic_phrase, legacy_address.decode('utf-8'), segwit_address

mnemonic_choice = input("Would you like a 12-word, 24-word, or random mnemonic? (Enter 12, 24, or random): ").strip().lower()

if mnemonic_choice == '12':
    mnemonic_length = 128
elif mnemonic_choice == '24':
    mnemonic_length = 256
elif mnemonic_choice == 'random':
    mnemonic_length = 'random'
else:
    print("Invalid choice, defaulting to random.")
    mnemonic_length = 'random'

private_key, public_key, mnemonic_phrase, legacy_address, segwit_address = generate_keys_and_addresses(mnemonic_length)

print(f"Mnemonic Phrase: {mnemonic_phrase}")
print(f"Private Key (Hex): {private_key.hex()}")
print(f"Public Key (Hex): {public_key.hex()}")
print(f"Legacy Address (P2PKH): {legacy_address}")
print(f"SegWit Address (P2WPKH/P2SH): {segwit_address}")
