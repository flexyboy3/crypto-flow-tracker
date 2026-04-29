from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def get_crypto_data(coin_id, symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false"
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    market = data.get("market_data", {})

    price = market.get("current_price", {}).get("usd", 0)
    change_24h = market.get("price_change_percentage_24h", 0)
    volume_24h = market.get("total_volume", {}).get("usd", 0)
    market_cap = market.get("market_cap", {}).get("usd", 0)
    high_24h = market.get("high_24h", {}).get("usd", 0)
    low_24h = market.get("low_24h", {}).get("usd", 0)

    if change_24h > 2:
        regime = "ACCUMULATION"
    elif change_24h < -2:
        regime = "DISTRIBUTION"
    else:
        regime = "NEUTRAL"

    return {
        "symbol": symbol,
        "price": price,
        "change_24h": change_24h,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "volume_24h": volume_24h,
        "market_cap": market_cap,
        "regime": regime
    }

@app.route("/api/crypto", methods=["GET"])
def crypto():
    coins = [
        ("bitcoin", "BTC"),
        ("ethereum", "ETH"),
        ("solana", "SOL")
    ]
    results = []
    for coin_id, symbol in coins:
        try:
            results.append(get_crypto_data(coin_id, symbol))
        except Exception as e:
            results.append({"symbol": symbol, "error": str(e)})
    return jsonify(results)

@app.route("/")
def home():
    return "Crypto Flow Tracker API is running!"

if __name__ == "__main__":
    app.run(debug=True)