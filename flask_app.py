from flask import Flask, request

app = Flask(__name__)

usd = 12737 # 1 USD = 12 737 UZS

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amounts
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    amount = request.args.get('amount')
    usd = round(int(amount) / 12737, 2)
    if amount:
        return {
            "amount": amount,
            "currency": "UZS",
            "converted": usd,
            "convertedCurrency": "USD"
        }

    return {
        "statust": "error"
    }


@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    amount = request.args.get('amount')
    uzs = round(int(amount)*12737, 2)
    if amount:
        return {
            "amount":amount,
            "currency" : "USD",
            "converted": uzs,
            "convertedCurrency": "UZS"

        }
    return {
        "status": "error"
    }


if __name__ == '__main__':
    app.run(debug = True)    