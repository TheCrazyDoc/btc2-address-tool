# 🪟 How to Use the Bitcoin2 Core Wallet (Windows)

This guide walks you through downloading, installing, and using the **official Bitcoin2 Core Wallet** on Windows.

---

## ✅ Step 1: Download the Wallet

1. Open your browser and go to:  
   👉 [https://www.bitc2.org/#wallets](https://www.bitc2.org/#wallets)
2. Scroll to the **Bitcoin2 Core Wallets** section.
3. Click the **Windows download** link (usually a `.zip` file).
4. Wait for the file to finish downloading.

---

## 📁 Step 2: Create a Folder & Extract the Wallet

1. On your Desktop, right-click and choose **New → Folder**  
   Name it: `Bitcoin2Wallet`
2. Move the downloaded `.zip` file into this folder.
3. Right-click the `.zip` file and choose **Extract All**
4. Open the extracted folder and double-click:  
   `bitcoin2-qt.exe`  
   *(It may take a few seconds to load — that's normal)*

---

## ⏳ Step 3: Let the Wallet Sync

- The wallet will automatically start syncing with the network.
- This downloads the entire blockchain and may take several hours the first time.
- You can close and reopen the wallet anytime — it will resume syncing from where it left off.

---

## 🔐 Step 4: Import a Private Key (Optional)

If you already have a private key (WIF) and want to access your funds:

1. Go to: **Help → Debug Window → Console**
2. In the console box, type:

```
importprivkey "YourPrivateKeyHere"
```

**Example:**

```
importprivkey "Ky1rKfD9VNHw1Sgf7AbgV8KU9qHtA4eU4T8FbJD6D2kL7nXoE6Xo"
```

Give the wallet a minute or two to rescan for your balance.

---

## 💰 Step 5: Check Your Balance

In the same console, type:

```
getbalance
```

This will display your current BTC2 balance.

---

## 🚀 You’re Ready!

You can now send, receive, and store **Bitcoin2 (BTC2)**.

🛡️ Don’t forget to **back up your wallet** from the **File** menu!

---

**Maintained by:** [@TheCrazyDoc](https://github.com/TheCrazyDoc)  
**Bitcoin2 Project:** [https://bitc2.org](https://bitc2.org)