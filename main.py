import requests

def get_crypto_flow(coin_id, symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false"
    }

    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        
       
        
        if response.status_code != 200:
            print(f"Error response: {response.text[:200]}")
            return

        data = response.json()
        market = data.get("market_data", {})

        if not market:
            print(f"No market data returned for {symbol}")
            print(f"Keys in response: {list(data.keys())}")
            return

        price = market.get("current_price", {}).get("usd", 0)
        change_24h = market.get("price_change_percentage_24h", 0)
        volume_24h = market.get("total_volume", {}).get("usd", 0)
        market_cap = market.get("market_cap", {}).get("usd", 0)
        high_24h = market.get("high_24h", {}).get("usd", 0)
        low_24h = market.get("low_24h", {}).get("usd", 0)

        if change_24h > 2:
            regime = "🟢 ACCUMULATION — Price up, buying pressure strong"
        elif change_24h < -2:
            regime = "🔴 DISTRIBUTION — Price down, selling pressure detected"
        else:
            regime = "🟡 NEUTRAL — No strong directional signal"

        print(f"\n{'='*50}")
        print(f"  {symbol} Exchange Flow Tracker")
        print(f"{'='*50}")
        print(f"  Price:        ${price:,.2f}")
        print(f"  24h Change:   {change_24h:.2f}%")
        print(f"  24h High:     ${high_24h:,.2f}")
        print(f"  24h Low:      ${low_24h:,.2f}")
        print(f"  Volume (24h): ${volume_24h:,.0f}")
        print(f"  Market Cap:   ${market_cap:,.0f}")
        print(f"\n  Regime Signal:")
        print(f"  {regime}")
        print(f"{'='*50}\n")

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

def main():
    print("\n🔍 Crypto Exchange Flow Tracker")
    print("Tracking: BTC, ETH, SOL\n")

    coins = [
        ("bitcoin", "BTC"),
        ("ethereum", "ETH"),
        ("solana", "SOL")
    ]

    for coin_id, symbol in coins:
        get_crypto_flow(coin_id, symbol)

if __name__ == "__main__":
    main()