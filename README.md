# Crypto Exchange Flow Tracker
A command-line tool that fetches live BTC, ETH, and SOL market data and generates a simple accumulation/distribution regime signal based on price action and volume.
## Features

Live price, 24h high/low, volume, and market cap
Regime signal: Accumulation, Distribution, or Neutral
Tracks BTC, ETH, and SOL simultaneously
No API key required

## Setup

Clone the repo
Install dependencies:

pip install -r requirements.txt
## Usage
python main.py
No input needed — automatically tracks BTC, ETH, and SOL.
## Example Output
🔍 Crypto Exchange Flow Tracker
Tracking: BTC, ETH, SOL
==================================================
BTC Exchange Flow Tracker
Price:        $77,200.00
24h Change:   0.30%
24h High:     $77,343.00
24h Low:      $75,706.00
Volume (24h): $34,478,671,641
Market Cap:   $1,545,766,272,314
Regime Signal:
🟡 NEUTRAL — No strong directional signal
## Tech Stack

Python
CoinGecko API (free, no key required)