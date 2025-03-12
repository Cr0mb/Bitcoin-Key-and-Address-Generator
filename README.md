# Bitcoin-Key-and-Address-Generator
This repository contains two Python scripts that generate Bitcoin keys, mnemonic phrases, and addresses. It demonstrates the process of creating Bitcoin private and public keys, converting them to addresses, and generating a mnemonic phrase for wallet backup.

## Requirements
To run the scripts, make sure to install the required dependencies:
```
pip install ecdsa mnemonic base58 bech32
```

## How Bitcoin Works
Bitcoin is a decentralized cryptocurrency that relies on cryptographic principles to secure transactions and control the creation of new units. Each user has a pair of cryptographic keys:

> Private Key: This is a secret number that is used to sign transactions. It gives the user full control over the associated Bitcoin.

> Public Key: This is derived from the private key and is shared publicly. It is used by others to send Bitcoin to the user.

Bitcoin addresses are derived from public keys using a series of cryptographic hashing algorithms. The address is what others use to send Bitcoin to a specific user.

## Key Generation

- Private Key: The private key is a random 256-bit number generated using a secure random function (os.urandom(32) in Python).

- Public Key: The public key is generated from the private key using elliptic curve cryptography (ECC) with the SECP256k1 curve. This is a one-way process, meaning you can generate the public key from the private key, but not the other way around.

- Mnemonic Phrase: A mnemonic phrase is a human-readable backup of your private key, typically 12 or 24 words. These words are derived from the SHA-256 hash of the private key.


## Bitcoin Address: Bitcoin addresses can be of different formats. The two main types used in these scripts are:

> Legacy Address (P2PKH): A traditional Bitcoin address that starts with a '1'.

> SegWit Address (P2WPKH/P2SH): A more modern address format that starts with a '3' or 'bc1', offering lower fees and more efficient transactions.

## Explanation of Key Concepts

[ECDSA](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (Elliptic Curve Digital Signature Algorithm): This cryptographic algorithm is used to generate private/public key pairs and sign transactions in Bitcoin.

[SHA-256](https://en.wikipedia.org/wiki/SHA-2): A cryptographic hash function that creates a 256-bit output. It is used to hash the private key to produce a public key and to create the seed for the mnemonic phrase.

[RIPEMD-160](https://en.wikipedia.org/wiki/RIPEMD): A cryptographic hash function that is applied to the SHA-256 hash of the public key. It is used in the creation of Bitcoin addresses.

[Base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58): This encoding is used to generate Bitcoin legacy addresses (P2PKH), which are human-readable and compact.

[Bech32](https://en.bitcoin.it/wiki/Bech32): This is a SegWit address format, more efficient than legacy addresses, that uses the "bc1" prefix.
