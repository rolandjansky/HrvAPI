# app.py
from random import random

from flask import Flask, request, jsonify
from flask import send_from_directory
import numpy as np
import pandas as pd
import math
import heartpy as hp

app = Flask(__name__, static_url_path='')

@app.route('/hrv/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
        return jsonify(response), 400
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
        return jsonify(response), 400
    # Check if the user is bob
    elif str(name) != 'Bob':
        response["ERROR"] = "User can't be found."
        return jsonify(response), 404
    # Check if server is in the mood
    elif random() < 0.1:
        response["ERROR"] = "Server not in the mood to answer your request. Try again."
        return jsonify(response), 503
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!! Here's your daily heart-rate data."
        response["data"] = [
            {
                "date": "22.08.2020 07:27",
                "hrrest": "53",
                "hrvrest": "48",
                "hrpeak": "93",
                "hrstanding": "78",
                "hrvstanding": "10"
            },
            {
                "date": "21.08.2020 06:18",
                "hrrest": "51",
                "hrvrest": "57",
                "hrpeak": "91",
                "hrstanding": "79",
                "hrvstanding": "12"
            },
            {
                "date": "20.08.2020 05:44",
                "hrrest": "56",
                "hrvrest": "46",
                "hrpeak": "94",
                "hrstanding": "79",
                "hrvstanding": "9"
            },
            {
                "date": "19.08.2020 06:29",
                "hrrest": "52",
                "hrvrest": "57",
                "hrpeak": "86",
                "hrstanding": "76",
                "hrvstanding": "9"
            },
            {
                "date": "18.08.2020 06:55",
                "hrrest": "55",
                "hrvrest": "40",
                "hrpeak": "86",
                "hrstanding": "79",
                "hrvstanding": "8"
            },
            {
                "date": "17.08.2020 07:08",
                "hrrest": "50",
                "hrvrest": "59",
                "hrpeak": "87",
                "hrstanding": "69",
                "hrvstanding": "12"
            },
            {
                "date": "16.08.2020 08:06",
                "hrrest": "55",
                "hrvrest": "44",
                "hrpeak": "93",
                "hrstanding": "80",
                "hrvstanding": "13"
            },
            {
                "date": "15.08.2020 06:49",
                "hrrest": "56",
                "hrvrest": "51",
                "hrpeak": "95",
                "hrstanding": "82",
                "hrvstanding": "12"
            },
            {
                "date": "13.08.2020 07:30",
                "hrrest": "51",
                "hrvrest": "65",
                "hrpeak": "93",
                "hrstanding": "84",
                "hrvstanding": "11"
            },
            {
                "date": "12.08.2020 07:14",
                "hrrest": "53",
                "hrvrest": "52",
                "hrpeak": "95",
                "hrstanding": "82",
                "hrvstanding": "6"
            },
            {
                "date": "11.08.2020 06:16",
                "hrrest": "52",
                "hrvrest": "49",
                "hrpeak": "87",
                "hrstanding": "74",
                "hrvstanding": "15"
            },
            {
                "date": "09.08.2020 07:45",
                "hrrest": "51",
                "hrvrest": "68",
                "hrpeak": "88",
                "hrstanding": "72",
                "hrvstanding": "14"
            },
            {
                "date": "08.08.2020 06:58",
                "hrrest": "55",
                "hrvrest": "54",
                "hrpeak": "91",
                "hrstanding": "74",
                "hrvstanding": "12"
            },
            {
                "date": "06.08.2020 07:21",
                "hrrest": "59",
                "hrvrest": "32",
                "hrpeak": "94",
                "hrstanding": "81",
                "hrvstanding": "14"
            },
            {
                "date": "05.08.2020 06:19",
                "hrrest": "50",
                "hrvrest": "45",
                "hrpeak": "91",
                "hrstanding": "79",
                "hrvstanding": "10"
            },
            {
                "date": "04.08.2020 08:48",
                "hrrest": "60",
                "hrvrest": "43",
                "hrpeak": "99",
                "hrstanding": "87",
                "hrvstanding": "18"
            },
            {
                "date": "03.08.2020 06:18",
                "hrrest": "51",
                "hrvrest": "57",
                "hrpeak": "88",
                "hrstanding": "77",
                "hrvstanding": "12"
            },
            {
                "date": "02.08.2020 08:39",
                "hrrest": "53",
                "hrvrest": "67",
                "hrpeak": "91",
                "hrstanding": "70",
                "hrvstanding": "26"
            },
            {
                "date": "01.08.2020 07:43",
                "hrrest": "63",
                "hrvrest": "29",
                "hrpeak": "99",
                "hrstanding": "83",
                "hrvstanding": "8"
            },
            {
                "date": "30.07.2020 05:38",
                "hrrest": "54",
                "hrvrest": "51",
                "hrpeak": "88",
                "hrstanding": "60",
                "hrvstanding": "35"
            },
            {
                "date": "29.07.2020 06:24",
                "hrrest": "53",
                "hrvrest": "48",
                "hrpeak": "86",
                "hrstanding": "77",
                "hrvstanding": "9"
            },
            {
                "date": "28.07.2020 06:32",
                "hrrest": "62",
                "hrvrest": "25",
                "hrpeak": "93",
                "hrstanding": "83",
                "hrvstanding": "8"
            },
            {
                "date": "27.07.2020 06:25",
                "hrrest": "62",
                "hrvrest": "38",
                "hrpeak": "95",
                "hrstanding": "84",
                "hrvstanding": "9"
            },
            {
                "date": "26.07.2020 08:34",
                "hrrest": "53",
                "hrvrest": "46",
                "hrpeak": "82",
                "hrstanding": "81",
                "hrvstanding": "7"
            },
            {
                "date": "25.07.2020 05:23",
                "hrrest": "54",
                "hrvrest": "45",
                "hrpeak": "82",
                "hrstanding": "69",
                "hrvstanding": "14"
            },
            {
                "date": "24.07.2020 07:40",
                "hrrest": "51",
                "hrvrest": "48",
                "hrpeak": "85",
                "hrstanding": "73",
                "hrvstanding": "8"
            },
            {
                "date": "23.07.2020 08:06",
                "hrrest": "50",
                "hrvrest": "47",
                "hrpeak": "84",
                "hrstanding": "68",
                "hrvstanding": "9"
            },
            {
                "date": "20.07.2020 06:47",
                "hrrest": "54",
                "hrvrest": "41",
                "hrpeak": "78",
                "hrstanding": "64",
                "hrvstanding": "18"
            },
            {
                "date": "19.07.2020 07:24",
                "hrrest": "56",
                "hrvrest": "38",
                "hrpeak": "85",
                "hrstanding": "75",
                "hrvstanding": "13"
            },
            {
                "date": "18.07.2020 06:12",
                "hrrest": "51",
                "hrvrest": "51",
                "hrpeak": "86",
                "hrstanding": "74",
                "hrvstanding": "7"
            },
            {
                "date": "17.07.2020 06:09",
                "hrrest": "49",
                "hrvrest": "69",
                "hrpeak": "80",
                "hrstanding": "59",
                "hrvstanding": "25"
            },
            {
                "date": "15.07.2020 07:32",
                "hrrest": "56",
                "hrvrest": "44",
                "hrpeak": "81",
                "hrstanding": "70",
                "hrvstanding": "11"
            },
            {
                "date": "14.07.2020 06:50",
                "hrrest": "52",
                "hrvrest": "48",
                "hrpeak": "78",
                "hrstanding": "65",
                "hrvstanding": "16"
            },
            {
                "date": "13.07.2020 06:45",
                "hrrest": "50",
                "hrvrest": "57",
                "hrpeak": "79",
                "hrstanding": "68",
                "hrvstanding": "12"
            },
            {
                "date": "12.07.2020 06:39",
                "hrrest": "52",
                "hrvrest": "49",
                "hrpeak": "83",
                "hrstanding": "69",
                "hrvstanding": "12"
            },
            {
                "date": "11.07.2020 06:51",
                "hrrest": "55",
                "hrvrest": "44",
                "hrpeak": "86",
                "hrstanding": "73",
                "hrvstanding": "10"
            },
            {
                "date": "10.07.2020 06:19",
                "hrrest": "56",
                "hrvrest": "45",
                "hrpeak": "87",
                "hrstanding": "71",
                "hrvstanding": "19"
            },
            {
                "date": "09.07.2020 07:02",
                "hrrest": "55",
                "hrvrest": "47",
                "hrpeak": "89",
                "hrstanding": "72",
                "hrvstanding": "10"
            },
            {
                "date": "08.07.2020 07:04",
                "hrrest": "53",
                "hrvrest": "53",
                "hrpeak": "88",
                "hrstanding": "72",
                "hrvstanding": "15"
            },
            {
                "date": "07.07.2020 06:15",
                "hrrest": "52",
                "hrvrest": "59",
                "hrpeak": "90",
                "hrstanding": "78",
                "hrvstanding": "6"
            },
            {
                "date": "06.07.2020 06:19",
                "hrrest": "51",
                "hrvrest": "55",
                "hrpeak": "88",
                "hrstanding": "79",
                "hrvstanding": "7"
            },
            {
                "date": "05.07.2020 07:48",
                "hrrest": "50",
                "hrvrest": "42",
                "hrpeak": "78",
                "hrstanding": "70",
                "hrvstanding": "12"
            },
            {
                "date": "04.07.2020 09:30",
                "hrrest": "52",
                "hrvrest": "54",
                "hrpeak": "90",
                "hrstanding": "76",
                "hrvstanding": "9"
            },
            {
                "date": "03.07.2020 06:32",
                "hrrest": "56",
                "hrvrest": "38",
                "hrpeak": "91",
                "hrstanding": "76",
                "hrvstanding": "12"
            },
            {
                "date": "02.07.2020 05:38",
                "hrrest": "57",
                "hrvrest": "39",
                "hrpeak": "88",
                "hrstanding": "75",
                "hrvstanding": "13"
            },
            {
                "date": "01.07.2020 06:09",
                "hrrest": "50",
                "hrvrest": "67",
                "hrpeak": "82",
                "hrstanding": "65",
                "hrvstanding": "8"
            },
            {
                "date": "30.06.2020 06:13",
                "hrrest": "49",
                "hrvrest": "59",
                "hrpeak": "87",
                "hrstanding": "68",
                "hrvstanding": "9"
            },
            {
                "date": "29.06.2020 06:44",
                "hrrest": "48",
                "hrvrest": "77",
                "hrpeak": "82",
                "hrstanding": "68",
                "hrvstanding": "15"
            },
            {
                "date": "28.06.2020 06:27",
                "hrrest": "47",
                "hrvrest": "66",
                "hrpeak": "81",
                "hrstanding": "66",
                "hrvstanding": "10"
            },
            {
                "date": "27.06.2020 07:03",
                "hrrest": "49",
                "hrvrest": "71",
                "hrpeak": "87",
                "hrstanding": "73",
                "hrvstanding": "10"
            },
            {
                "date": "26.06.2020 06:46",
                "hrrest": "54",
                "hrvrest": "49",
                "hrpeak": "86",
                "hrstanding": "69",
                "hrvstanding": "14"
            },
            {
                "date": "25.06.2020 05:43",
                "hrrest": "51",
                "hrvrest": "58",
                "hrpeak": "85",
                "hrstanding": "72",
                "hrvstanding": "14"
            },
            {
                "date": "24.06.2020 06:15",
                "hrrest": "47",
                "hrvrest": "74",
                "hrpeak": "87",
                "hrstanding": "68",
                "hrvstanding": "14"
            },
            {
                "date": "23.06.2020 06:13",
                "hrrest": "49",
                "hrvrest": "55",
                "hrpeak": "84",
                "hrstanding": "67",
                "hrvstanding": "15"
            },
            {
                "date": "22.06.2020 06:17",
                "hrrest": "47",
                "hrvrest": "63",
                "hrpeak": "81",
                "hrstanding": "66",
                "hrvstanding": "12"
            },
            {
                "date": "21.06.2020 08:38",
                "hrrest": "48",
                "hrvrest": "84",
                "hrpeak": "90",
                "hrstanding": "74",
                "hrvstanding": "11"
            },
            {
                "date": "20.06.2020 07:22",
                "hrrest": "47",
                "hrvrest": "79",
                "hrpeak": "87",
                "hrstanding": "72",
                "hrvstanding": "11"
            },
            {
                "date": "19.06.2020 07:56",
                "hrrest": "56",
                "hrvrest": "41",
                "hrpeak": "95",
                "hrstanding": "84",
                "hrvstanding": "9"
            },
            {
                "date": "18.06.2020 06:13",
                "hrrest": "50",
                "hrvrest": "74",
                "hrpeak": "88",
                "hrstanding": "75",
                "hrvstanding": "11"
            },
            {
                "date": "17.06.2020 06:42",
                "hrrest": "50",
                "hrvrest": "63",
                "hrpeak": "88",
                "hrstanding": "75",
                "hrvstanding": "14"
            },
            {
                "date": "16.06.2020 06:15",
                "hrrest": "48",
                "hrvrest": "78",
                "hrpeak": "81",
                "hrstanding": "66",
                "hrvstanding": "13"
            },
            {
                "date": "15.06.2020 06:54",
                "hrrest": "48",
                "hrvrest": "77",
                "hrpeak": "81",
                "hrstanding": "72",
                "hrvstanding": "8"
            },
            {
                "date": "14.06.2020 07:31",
                "hrrest": "48",
                "hrvrest": "70",
                "hrpeak": "84",
                "hrstanding": "72",
                "hrvstanding": "12"
            },
            {
                "date": "13.06.2020 07:45",
                "hrrest": "47",
                "hrvrest": "69",
                "hrpeak": "88",
                "hrstanding": "77",
                "hrvstanding": "13"
            },
            {
                "date": "12.06.2020 05:42",
                "hrrest": "52",
                "hrvrest": "59",
                "hrpeak": "89",
                "hrstanding": "77",
                "hrvstanding": "13"
            },
            {
                "date": "11.06.2020 06:13",
                "hrrest": "51",
                "hrvrest": "56",
                "hrpeak": "88",
                "hrstanding": "75",
                "hrvstanding": "7"
            },
            {
                "date": "10.06.2020 06:53",
                "hrrest": "46",
                "hrvrest": "76",
                "hrpeak": "88",
                "hrstanding": "70",
                "hrvstanding": "8"
            },
            {
                "date": "09.06.2020 06:12",
                "hrrest": "47",
                "hrvrest": "76",
                "hrpeak": "79",
                "hrstanding": "64",
                "hrvstanding": "15"
            },
            {
                "date": "08.06.2020 06:52",
                "hrrest": "50",
                "hrvrest": "74",
                "hrpeak": "86",
                "hrstanding": "74",
                "hrvstanding": "8"
            },
            {
                "date": "07.06.2020 08:02",
                "hrrest": "52",
                "hrvrest": "63",
                "hrpeak": "92",
                "hrstanding": "77",
                "hrvstanding": "12"
            },
            {
                "date": "06.06.2020 07:22",
                "hrrest": "51",
                "hrvrest": "66",
                "hrpeak": "86",
                "hrstanding": "84",
                "hrvstanding": "6"
            },
            {
                "date": "05.06.2020 06:13",
                "hrrest": "47",
                "hrvrest": "72",
                "hrpeak": "88",
                "hrstanding": "72",
                "hrvstanding": "12"
            },
            {
                "date": "04.06.2020 05:43",
                "hrrest": "55",
                "hrvrest": "55",
                "hrpeak": "89",
                "hrstanding": "76",
                "hrvstanding": "15"
            },
            {
                "date": "03.06.2020 06:13",
                "hrrest": "50",
                "hrvrest": "74",
                "hrpeak": "83",
                "hrstanding": "71",
                "hrvstanding": "9"
            },
            {
                "date": "02.06.2020 06:18",
                "hrrest": "51",
                "hrvrest": "55",
                "hrpeak": "84",
                "hrstanding": "69",
                "hrvstanding": "9"
            },
            {
                "date": "01.06.2020 07:23",
                "hrrest": "51",
                "hrvrest": "64",
                "hrpeak": "88",
                "hrstanding": "71",
                "hrvstanding": "12"
            },
            {
                "date": "31.05.2020 07:44",
                "hrrest": "50",
                "hrvrest": "58",
                "hrpeak": "88",
                "hrstanding": "71",
                "hrvstanding": "12"
            },
            {
                "date": "30.05.2020 07:22",
                "hrrest": "52",
                "hrvrest": "56",
                "hrpeak": "90",
                "hrstanding": "76",
                "hrvstanding": "11"
            },
            {
                "date": "29.05.2020 06:23",
                "hrrest": "55",
                "hrvrest": "45",
                "hrpeak": "86",
                "hrstanding": "76",
                "hrvstanding": "9"
            },
            {
                "date": "28.05.2020 05:46",
                "hrrest": "52",
                "hrvrest": "56",
                "hrpeak": "87",
                "hrstanding": "72",
                "hrvstanding": "13"
            },
            {
                "date": "27.05.2020 06:18",
                "hrrest": "62",
                "hrvrest": "26",
                "hrpeak": "90",
                "hrstanding": "76",
                "hrvstanding": "12"
            },
            {
                "date": "26.05.2020 06:18",
                "hrrest": "57",
                "hrvrest": "36",
                "hrpeak": "90",
                "hrstanding": "78",
                "hrvstanding": "6"
            },
            {
                "date": "25.05.2020 06:53",
                "hrrest": "62",
                "hrvrest": "25",
                "hrpeak": "88",
                "hrstanding": "78",
                "hrvstanding": "8"
            },
            {
                "date": "24.05.2020 07:21",
                "hrrest": "62",
                "hrvrest": "23",
                "hrpeak": "83",
                "hrstanding": "71",
                "hrvstanding": "9"
            },
            {
                "date": "23.05.2020 07:50",
                "hrrest": "54",
                "hrvrest": "55",
                "hrpeak": "85",
                "hrstanding": "79",
                "hrvstanding": "9"
            },
            {
                "date": "22.05.2020 07:07",
                "hrrest": "57",
                "hrvrest": "35",
                "hrpeak": "85",
                "hrstanding": "81",
                "hrvstanding": "7"
            },
            {
                "date": "21.05.2020 08:06",
                "hrrest": "59",
                "hrvrest": "34",
                "hrpeak": "91",
                "hrstanding": "83",
                "hrvstanding": "8"
            },
            {
                "date": "20.05.2020 06:54",
                "hrrest": "60",
                "hrvrest": "50",
                "hrpeak": "93",
                "hrstanding": "83",
                "hrvstanding": "9"
            },
            {
                "date": "19.05.2020 06:52",
                "hrrest": "58",
                "hrvrest": "46",
                "hrpeak": "88",
                "hrstanding": "79",
                "hrvstanding": "11"
            },
            {
                "date": "18.05.2020 06:54",
                "hrrest": "56",
                "hrvrest": "57",
                "hrpeak": "84",
                "hrstanding": "76",
                "hrvstanding": "9"
            },
            {
                "date": "17.05.2020 07:22",
                "hrrest": "58",
                "hrvrest": "45",
                "hrpeak": "85",
                "hrstanding": "77",
                "hrvstanding": "9"
            },
            {
                "date": "16.05.2020 06:43",
                "hrrest": "61",
                "hrvrest": "37",
                "hrpeak": "89",
                "hrstanding": "75",
                "hrvstanding": "10"
            }
        ]

    # Return the response in json format
    return jsonify(response), 200

@app.route('/post/', methods=['POST'])
def post_something():
    hrdata = request.get_data()

    sample_rate = 60
    # For debugging
    print(f"got name {hrdata}")

    response = {}

    if not hrdata:
        response["ERROR"] = "no data found, please send data."
    else:
        df = pd.read_json(hrdata)
        if not df.empty:
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
            if math.isnan(m["bpm"]):
                response["BPM"] = 0.0
            else:
                response["BPM"] = m["bpm"]
            if math.isnan(m["rmssd"]):
                response["HRV"] = 0.0
            else:
                response["HRV"] = m["rmssd"]
        else:
            response["BPM"] = 0.0
            response["HRV"] = 0.0

    # Return the response in json format
    return jsonify(response)


# A welcome message to test our server
@app.route('/')
def index():
    return app.send_static_file('DataScientist_EngineerCaseStudy.pdf')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
