from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store data (temporary – can be replaced with DB)
street_light_data = []

@app.route('/update', methods=['GET', 'POST'])
def update_data():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    status = request.args.get('status')
    light_id = request.args.get('id', 'SL-001')

    if latitude and longitude and status:
        record = {
            "Light ID": light_id,
            "Latitude": latitude,
            "Longitude": longitude,
            "Status": status,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        street_light_data.append(record)

        print("New Fault Update:", record)

        return jsonify({"message": "Data received successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400


@app.route('/data', methods=['GET'])
def view_data():
    return jsonify(street_light_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
