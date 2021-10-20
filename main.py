# import http.client
# import json

# conn = http.client.HTTPSConnection("api.github.com")

# api_token = "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"
# headers = {
#     'Authorization': 'token %s' % api_token,
#     'User-Agent': 'PUC-LAB-APP',
#     # 'cookie': '_octo=GH1.1.20155132.1619476650; logged_in=yes; dotcom_user=ArthurRAmaral; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=America%2FSao_Paul'
# }

# conn.request("GET", "/repos/nestjs/nest/issues/8111", None, headers)

# response = conn.getresponse()
# data = response.read()

# d = json.loads(data)
# print(d["body"])

# print(response.status, response.reason)


params = {'name': 'nestjs', 'owner': 'nest', 'issueId': '8111'}
print("/repos/%(name)s/%(owner)s/issues/%(issueId)s" % params)
