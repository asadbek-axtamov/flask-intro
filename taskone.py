from flask import Flask, request

app = Flask(__name__)

@app.route('/api/get-sum', methods=['GET'])

def get_sum():
    """
    this function returns sum of two number from request data.

    Returns:
        json: sum of two number

    Note:
        request data will be like this:
            /api/get-sum/?a=1&b=2
            
        response data will be like this:
            {
                "sum": 3
            }
    """  
    args_value = request.args
    a = args_value.get('a')
    b = args_value.get('b')
    if a!=None and b!=None:
        results = {
            "sum" : int(a) + int(b)
        }
        return results
    else:
        return {
            "status": "error"
        }
    

if __name__ == "__main__":
    app.run(port=8010, debug = True )