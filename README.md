# 🔐 BTC2 Address Tool & Paper Wallet Generator
MIT License

An open-source, offline tool to generate compressed Bitcoin 2 (BTC2) wallets — secure, simple, and private. Built for speed and beginners.

---

## 🎯 BTC2 Vanity Address Generator (Compressed Only)

Generate a Bitcoin2 address that starts with your desired vanity prefix using 18 threads for fast results. Example: `1BTC`, `1KING`, `1Dork`, etc.

⚠️ Supports **compressed BTC2 addresses only** (for modern security & compatibility).

### 🛠 Requirements

```bash
pip install base58 ecdsa
```

### 🚀 How to Run

```bash
python btc2_vanity_search.py <VanityPrefix>
```

Replace `<VanityPrefix>` with your desired starting characters.

### 🔍 Example

```bash
python btc2_vanity_search.py 1BTC2
```

### ✅ Sample Output

```
🚀 Searching for BTC2 compressed address starting with: 1BTC2
🧵 Using 18 threads...

🎯 MATCH FOUND!
Address: 1BTC26hk75TsKUUgBTVe58LDmntS7WKM9r
WIF: L1MnNNzdS5Co9wFyLygnoaBtrTEvEhcoHFWt5d3FymPfrVoN5W6H
Hex: 7b8090ab45950316ac75fd654b71be4b9380dbda31d522dab06aa7d377876c85

✅ Done in 207.58 seconds.
```

### 🔒 Notes

- Script stops **automatically** after the first match is found.
- Uses all **18 threads** for max speed (adjustable in code).
- Fully offline — **no internet access required**.

---

## 🧰 Features

- 🔑 Generates compressed BTC2 addresses (WIF + HEX)
- 🎯 Includes a high-speed vanity address generator
- 📄 Bulk generation: save 10 addresses in a `.csv` file
- 💻 CLI (Command Line Interface) — Python based
- 💯 Fully offline — no internet required
- 🧠 Beginner friendly

---

## 📦 Files

| File                  | Description                                           |
|-----------------------|-------------------------------------------------------|
| `BTC2wallet.py`       | Generates a single BTC2 compressed paper wallet       |
| `BTC2_bulk_wallets.py`| Generates 10 compressed wallets and saves to `.csv`   |
| `btc2_vanity_search.py` | Vanity address generator using 18 threads           |
| `sample_btc2_wallets.csv` | Sample output file for bulk generation            |

---

## ▶️ How to Use

### 1. 🐍 Install Python Dependencies

Make sure Python 3 is installed. Then run:

```bash
pip install ecdsa base58
```

---

### 2. 🔐 Run Single Wallet Generator

```bash
python BTC2wallet.py
```

**Output:**

```
✅ BTC2 Compressed Paper Wallet
-------------------------------
BTC2 Address: 1ABCDEF...
Private Key (WIF Compressed): L1xyz...
Private Key (Hex): abc123...
```

---

### 3. 📁 Run Bulk Wallet Generator

```bash
python BTC2_bulk_wallets.py
```

This creates **10 BTC2 compressed addresses** and saves them to `btc2_wallets.csv`.

---

## ⚠️ Disclaimer

- This is an **educational tool**.
- Always verify wallet addresses before sending real BTC2.
- Run completely offline for maximum security.
- Use at your own risk.

---

## 💸 Donate BTC2

If this project helped you, support development!

**BTC2 Address:**  
`1Dork37FWZqFefKiW9yGVKFqNkmKRU8qyh`

---

## 🙌 Credits

Maintained by **@TheCrazyDoc**  
Inspired by the mission of #Bitcoin2 — fast, fair, and accessible crypto for all.
