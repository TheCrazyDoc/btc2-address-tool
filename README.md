# 🔐 BTC2 Address Tool — CLI Paper Wallet Generator

A secure, lightweight, and offline-compatible **Bitcoin2 (BTC2)** wallet generator written in Python.  
Generate single or multiple **compressed BTC2 addresses + WIF private keys** for cold storage or offline backups.

---

## ✨ Features

- 🔐 Non-custodial — you control the keys
- ⚡ Generates compressed BTC2 addresses
- 📦 Bulk generator: create 10 wallets at once
- ✅ Supports both terminal (CLI) and future web version
- 🔒 Works fully offline — perfect for air-gapped systems

---

## 📁 Included Files

| File | Description |
|------|-------------|
| `BTC2wallet.py` | Generates a **single BTC2 compressed paper wallet** |
| `BTC2_bulk_wallets.py` | Generates **10 BTC2 wallets at once** and saves to `btc2_wallets.csv` |
| `sample_btc2_wallets.csv` | (Optional) Sample output of the bulk generator — no real funds |

---

## 🚀 How to Use

### 1. 🔧 Install Python (if not already installed)
Download Python: https://www.python.org/downloads/

Make sure `pip` is available:
```bash
python --version
pip --version
