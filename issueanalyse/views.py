from django.http.response import JsonResponse
from django.shortcuts import render
from simpletransformers.classification import ClassificationModel
import torch

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
