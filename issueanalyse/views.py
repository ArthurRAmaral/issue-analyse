from django.http.response import JsonResponse
from django.shortcuts import render
# from simpletransformers.classification import ClassificationModel


# model = ClassificationModel(
#     "roberta", "../outputs/checkpoint-1313-epoch-1",
#     use_cuda=False
# )

result_map = {0: False, 1: True}


def dashboard(request):
    return render(request, 'index.html')


def analyseIfIsBug(request, text):
    # predictions, raw_outputs = model.predict([text])
    return JsonResponse({'isBug': result_map[1], 'text': text})
