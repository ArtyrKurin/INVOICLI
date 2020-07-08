import json
import re
import requests
# from clockify.clockify import Clockify

from flask import Flask, jsonify
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

# clockify_server = Clockify("XYy/HngZVC0fWaE0")
# headers = {'content-type': "application/json", "X-Api-Key": "XYy/HngZVC0fWaE0"}
# params = {'start': '2020-04-1T05:15:32.998Z', 'end': '2020-04-30T05:15:32.998Z'}
#
# url = "https://clockify-response.p.rapidapi.com/"
#
#
# class User(flask_restful.Resource):
#     def get(self):
#         API_URL_PROJECT = "https://api.clockify.me/api/v1/workspaces/5e2feaa6b128ac31f2589da3/users"
#         result_request = requests.get(API_URL_PROJECT, headers=headers, params=params)
#         List = json.loads(result_request.text)
#         result = []
#         for text in List:
#             formatted = dict()
#             filtering_data = text['memberships']
#             for fd in filtering_data:
#                 formatted['hourlyRate'] = fd['hourlyRate']
#                 formatted['userId'] = fd['userId']
#             formatted['name'] = text['name']
#             formatted['email'] = text['email']
#             result.append(formatted)
#
#         payload = result
#         headerss = {
#             'x-rapidapi-host': "clockify-response.p.rapidapi.com",
#             'x-rapidapi-key': "bd734074e1mshf925fe26873bf52p1e0f89jsndb382deb8c02",
#             'content-type': "application/x-www-form-urlencoded"
#         }
#
#         response = requests.request("GET", url, data=payload, headers=headerss)
#
#         return response
#
#
# class Project(flask_restful.Resource):
#     def get(self):
#         API_URL_PROJECT = "https://api.clockify.me/api/v1/workspaces/5e2feaa6b128ac31f2589da3/projects"
#         result_request = requests.get(API_URL_PROJECT, headers=headers, params=params)
#         List = json.loads(result_request.text)
#         result = []
#         for fp in List:
#             formatted = dict()
#             formatted['name'] = fp["name"]
#             formatting_text = re.sub(r"[PT]", "", fp['duration'])
#             formatting_time2 = re.sub(r"[HMS]", ":", formatting_text)
#             filtering_data = fp['memberships']
#             for fd in filtering_data:
#                 formatted['hourlyRate'] = fd['hourlyRate']
#             formatted['duration'] = formatting_text
#             formatted['duration'] = formatting_time2
#             formatted['clientName'] = fp['clientName']
#             result.append(formatted)
#         return result
#
#
# class TimeEntry(flask_restful.Resource):
#     def get(self):
#         time_entry = clockify_server.get_all_time_entry_user('5e2feaa6b128ac31f2589da3', '5d4451b5d278ae57b51d7dd0')
#
#         # API_URL_PROJECT = "https://api.clockify.me/api/v1/workspaces/5eab925e109fe91523414d2f/user/5e2b2c976b5d0e21a1e863cd/time-entries"
#         # result_request = requests.get(API_URL_PROJECT, headers=headers, params=params)
#         # print(result_request)
#         # List = json.loads(f.text)
#         result = [time_entry]
#         for fp in time_entry:
#             formatted = dict()
#
#             filtering_data = fp['timeInterval']
#             for fd in filtering_data:
#                 formatting_time = re.sub(r"[PT]", "", fp['duration'])
#                 formatting_time2 = re.sub(r"[HMS]", ":", formatting_time)
#                 formatted['duration'] = fd['duration']
#             formatted['memberships'] = fp['memberships']
#             formatted['hourlyRate'] = fp["hourlyRate"]
#             formatted['duration'] = formatting_time2
#
#         return result


@app.route('/')
def index():
    return jsonify("DADA")


# # User parameters
# api.add_resource(User, '/api/user')
# # Project parameters
# api.add_resource(Project, '/api/projects')
# # Time entry by id
# api.add_resource(TimeEntry, '/api/time')

if __name__ == '__main__':
    app.run(debug=True)
