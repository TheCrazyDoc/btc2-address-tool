# 🔐 BTC2 Address Tool & Paper Wallet Generator
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

An open-source, offline tool to generate **compressed Bitcoin 2 (BTC2) wallets** — secure, simple, and private. Built for speed and beginners.

---

## 🧰 Features

- 🔑 Generates **compressed BTC2 addresses** (WIF + HEX)
- 📄 Optional: Save 10 addresses in a `.csv` file
- 💻 CLI (Command Line Interface) — Python based
- 💯 Fully offline — no internet required
- 🧠 Beginner friendly

---

## 📦 Files

| File | Description |
|------|-------------|
| `BTC2wallet.py` | Generates a single BTC2 compressed paper wallet |
| `BTC2_bulk_wallets.py` | Generates 10 BTC2 compressed wallets and saves them to `btc2_wallets.csv` |
| `sample_btc2_wallets.csv` | Sample output file for bulk wallets (for preview only) |

---

## 🚀 How to Use

### 1. 🐍 Install Python dependencies

Make sure you have Python 3 installed.  
Open terminal or PowerShell and install dependencies:

```bash
pip install ecdsa base58

2. ▶️ Run Single Wallet Generator

python BTC2wallet.py

📋 Output:

✅ BTC2 Compressed Paper Wallet
-------------------------------
BTC2 Address: 1ABCDEF...
Private Key (WIF Compressed): L1xyz...
Private Key (Hex): abc123...

3. 🗂️ Run Bulk Wallet Generator

python BTC2_bulk_wallets.py
📄 This will generate 10 random BTC2 compressed addresses and save them to btc2_wallets.csv.


🎯 BTC2 Vanity Address Generator (Compressed Only)
Generate a Bitcoin2 address that starts with your desired vanity prefix using 18 threads for faster results. Example: 1BTC, 1KING, 1Dork, etc.

⚠️ Compressed addresses only (for modern security & compatibility)

🛠 Requirements
Make sure Python 3 is installed with the following packages:

bash
Copy
Edit
pip install base58 ecdsa
🚀 How to Run
bash
Copy
Edit
python btc2_vanity_search.py <VanityPrefix>
Replace <VanityPrefix> with your desired starting characters.

🔍 Example:
bash
Copy
Edit
python btc2_vanity_search.py 1BTC2
✅ Sample Output
vbnet
Copy
Edit
🚀 Searching for BTC2 compressed address starting with: 1BTC2
🧵 Using 18 threads...

🎯 MATCH FOUND!
Address: 1BTC26hk75TsKUUgBTVe58LDmntS7WKM9r
WIF: L1MnNNzdS5Co9wFyLygnoaBtrTEvEhcoHFWt5d3FymPfrVoN5W6H
Hex: 7b8090ab45950316ac75fd654b71be4b9380dbda31d522dab06aa7d377876c85

✅ Done in 207.58 seconds.
🔒 Notes
Stops automatically after the first match is found.

Uses all 18 threads for maximum speed (adjustable in the script).

Fully offline — no data is sent or shared.


⚠️ Disclaimer
This is an educational tool.
Always verify wallet addresses before sending real BTC2.
Run offline for best security. Use at your own risk.

💸 Donate BTC2
If this helped you, support future development:

BTC2 Address:
1Dork37FWZqFefKiW9yGVKFqNkmKRU8qyh

🙌 Credits
Maintained by @TheCrazyDoc
Inspired by the mission of #Bitcoin2 to make crypto fast, fair, and accessible.




