# 🔐 BTC2 Address Tool & Paper Wallet Generator

**MIT License**

An open-source, offline tool to generate compressed Bitcoin 2 (BTC2) wallets — secure, simple, and private. Built for speed and beginners.

---

## 🧰 Features

* 🔑 Generates compressed BTC2 addresses (WIF + HEX)
* 🎯 High-speed vanity address generator
* 📄 Bulk generation: save 10 addresses to a `.csv` file
* 💻 CLI (Command Line Interface) — Python-based
* 💯 Fully offline — no internet required
* 🧠 Beginner friendly

---

## 🎯 BTC2 Vanity Address Generator (Compressed Only)

Generate a BTC2 address that starts with your desired vanity prefix using **18 threads** for fast results.
Example: `1BTC`, `1KING`, `1Dork`, etc.

⚠️ *Supports compressed BTC2 addresses only (for modern security & compatibility).*

---

## 🛠 Requirements

Make sure you have Python 3 installed, then install dependencies:

```bash
pip install ecdsa base58
```

---

## 🚀 How to Run

### 🧪 Vanity Generator

```bash
python btc2_vanity_search.py <VanityPrefix>
```

Replace `<VanityPrefix>` with your desired starting characters.

#### 🔍 Example:

```bash
python btc2_vanity_search.py 1BTC2
```

#### ✅ Sample Output

```
🚀 Searching for BTC2 compressed address starting with: 1BTC2
🧵 Using 18 threads...

🎯 MATCH FOUND!
Address: 1BTC26hk75TsKUUgBTVe58LDmntS7WKM9r
WIF: L1MnNNzdS5Co9wFyLygnoaBtrTEvEhcoHFWt5d3FymPfrVoN5W6H
Hex: 7b8090ab45950316ac75fd654b71be4b9380dbda31d522dab06aa7d377876c85

✅ Done in 207.58 seconds.
```

---

## 🔒 Notes

* Script stops automatically after the first match is found
* Uses all 18 threads for max speed (adjustable in code)
* Fully offline — no internet access required

---

## 📦 Files

| File                                | Description                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------- |
| `BTC2wallet.py`                     | Generates a single BTC2 compressed paper wallet                                    |
| `BTC2_bulk_wallets.py`              | Generates 10 compressed wallets and saves to `.csv`                                |
| `btc2_vanity_search.py`             | Vanity address generator using 18 threads                                          |
| `sample_btc2_wallets.csv`           | Sample output file for bulk generation                                             |
| `BTC2_Windows_Core_Wallet_Guide.md` | [Setup guide for BTC2 Core Wallet on Windows](./BTC2_Windows_Core_Wallet_Guide.md) |
| `fix_unconfirmed_tx.md`             | Fix stuck/unconfirmed BTC2 transactions using `-zapwallettxes=1`                   |

---

## ▶️ How to Use

### 1. 🐍 Install Python Dependencies

```bash
pip install ecdsa base58
```

### 2. 🔐 Run Single Wallet Generator

```bash
python BTC2wallet.py
```

#### ✅ Output:

```
BTC2 Address: 1ABCDEF...
Private Key (WIF Compressed): L1xyz...
Private Key (Hex): abc123...
```

### 3. 📁 Run Bulk Wallet Generator

```bash
python BTC2_bulk_wallets.py
```

Generates 10 compressed addresses and saves them to `btc2_wallets.csv`.

---

## 🌐 BTC2 Paper Wallet (Offline HTML)

We’ve included a fully offline HTML tool to generate a **single BTC2 paper wallet** (compressed address only).

### 🔹 Features:

* Runs completely in your browser (no install needed)
* Includes compressed address, WIF key, and HEX private key
* Optimized for print (fits on 1 page)
* Uses high-entropy RNG (safe for offline use)

### 🔸 How to Use:

1. Open `index.html` in your browser (no internet required)
2. Click **“Generate New Wallet”**
3. Print or save your wallet securely

### 📁 File:

| File         | Description                                   |
| ------------ | --------------------------------------------- |
| `index.html` | BTC2 paper wallet generator (single, offline) |

> ⚠️ For maximum safety, run this file on an air-gapped (offline) device.

---

## 🚑 Fix Unconfirmed or Stuck BTC2 Transactions

Sometimes a transaction using SwiftTX or an unstable connection can remain **unconfirmed** or **stuck** in your wallet. To safely clear these and reload your wallet state:

### 🧰 Quick Command

**Linux / macOS**

```bash
./bitcoin2-qt -zapwallettxes=1
```

**Windows**

```bash
bitcoin2-qt.exe -zapwallettxes=1
```

> This will start the wallet, **remove all unconfirmed transactions**, and **resync your wallet history** using the blockchain.

#### ✅ Real Example

Community member **@Dork37og** successfully recovered access to over **76 BTC2** stuck in an unconfirmed transaction. After launching the wallet with `-zapwallettxes=1`, the wallet reset and all funds were restored.

---

## ⚠️ Disclaimer

* This is an educational tool.
* Always verify addresses before sending BTC2.
* Run fully offline for best security.
* Use at your own risk.

---

## 💸 Donate BTC2

If this project helped you, consider donating to support future development:

**BTC2 Address:**
`1Dork37FWZqFefKiW9yGVKFqNkmKRU8qyh`
