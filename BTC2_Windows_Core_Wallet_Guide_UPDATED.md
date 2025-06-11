
🪟 How to Use the Bitcoin2 Core Wallet (Windows)
This guide walks you through downloading, installing, and using the official Bitcoin2 Core Wallet on Windows.

✅ Step 1: Download the Wallet
Open your browser and go to:
👉 https://www.bitc2.org/#wallets
Scroll to the Bitcoin2 Core Wallets section.
Click the Windows download link (usually a .zip file).
Wait for the file to finish downloading.

📁 Step 2: Create a Folder & Extract the Wallet
On your Desktop, right-click and choose New → Folder
Name it: Bitcoin2Wallet
Move the downloaded .zip file into this folder.
Right-click the .zip file and choose Extract All
Open the extracted folder and double-click:
bitcoin2-qt.exe
(It may take a few seconds to load — that's normal)

⏳ Step 3: Let the Wallet Sync
The wallet will automatically start syncing with the network.
This downloads the entire blockchain and may take several hours the first time.
You can close and reopen the wallet anytime — it will resume syncing from where it left off.

🔐 Step 4: Import a Private Key (Optional)
If you already have a private key (WIF) and want to access your funds:

Go to: Help → Debug Window → Console
In the console box, type:
importprivkey "YourPrivateKeyHere"
Example:
importprivkey "Ky1rKfD9VNHw1Sgf7AbgV8KU9qHtA4eU4T8FbJD6D2kL7nXoE6Xo"
Give the wallet a minute or two to rescan for your balance.

👁️ Step 4B: Add a Watch-Only Address (Optional)
If you want to monitor a BTC2 address without importing the private key (ideal for cold wallets or gifts):

Go to: Help → Debug Window → Console
In the console box, type:
importaddress "YourBTC2AddressHere"

✅ Example:
importaddress "1Dork37FWZqFefKiW9yGVKFqNkmKRU8qyh"

Wait a few seconds — the address will be added as watch-only, and your wallet will track its balance.

ℹ️ Tip:
Use this to scan for past transactions too:
importaddress "1YourAddress" "" false

💰 Step 5: Check Your Balance
In the same console, type:
getbalance
This will display your current BTC2 balance.

🚀 You’re Ready!
You can now send, receive, and store Bitcoin2 (BTC2).

🛡️ Don’t forget to back up your wallet from the File menu!

Maintained by: @TheCrazyDoc
Bitcoin2 Project: https://bitc2.org
