# app.py
from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import heartpy as hp

app = Flask(__name__)


@app.route('/post/', methods=['POST'])
def post_something():
    hrdata = request.get_data()

    sample_rate = 60
    # For debugging
    print(f"got name {hrdata}")

    response = {}

    if not hrdata:
        response["ERROR"] = "no data found, please send data."
    elif len(hrdata) == 0:
        response["BPM"] = 0
        response["HRV"] = 0
    else:
        df = pd.read_json(hrdata)
        data = df["time"]
        sample_rate = round(hp.get_samplerate_datetime(data, timeformat='%Y-%m-%dT%H:%M:%S.%f'))
        data = df["value"]
        data = np.nan_to_num(data)
        filtered_ppg = hp.filter_signal(data[20:],
                                        cutoff=[0.6, 2.5],
                                        filtertype='bandpass',
                                        sample_rate=2 * sample_rate,
                                        order=3,
                                        return_top=False)
        wd, m = hp.process(filtered_ppg, sample_rate=sample_rate,
                           high_precision=True, clean_rr=True)
        response["BPM"] = m["bpm"]
        response["HRV"] = m["rmssd"]

    # Return the response in json format
    return jsonify(response)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
