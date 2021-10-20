from django.http.response import JsonResponse
from django.shortcuts import render
from simpletransformers.classification import ClassificationModel
import torch
import http.client
import json

conn = http.client.HTTPSConnection("api.github.com")
headers = {
    'User-Agent': 'PUC-LAB-APP',
}


cuda_available = torch.cuda.is_available()

print(cuda_available)

model = ClassificationModel(
    "roberta", "outputs/checkpoint-1313-epoch-1",
    use_cuda=cuda_available
)

print('Model created.')

result_map = {0: False, 1: True}


def dashboard(request):
    return render(request, 'index.html')


def analyseIfIsBug(request, text):
    predictions, raw_outputs = model.predict([text])
    return JsonResponse({'isBug': result_map[predictions[0]], 'text': text})


def analyseIfIsBugFromGit(request, name, owner, issueId):

    params = {'name': name, 'owner': owner, 'issueId': issueId}
    conn.request("GET", "/repos/%(name)s/%(owner)s/issues/%(issueId)s" %
                 params, None, headers)

    response = conn.getresponse()
    data = response.read()
    issue = json.loads(data)

    text = "%(title)s %(body)s" % issue

    predictions, raw_outputs = model.predict([text])

    return JsonResponse({
        'isBug': result_map[predictions[0]],
        'title': issue["title"],
        'body': issue["body"],
        'text-analysed': text
    })
