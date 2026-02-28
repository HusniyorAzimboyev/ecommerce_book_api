from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import ai_recommends

@api_view(['GET'])
def dummy(request):
    return Response({"nn":"yes"}, status=200)

@api_view(['POST'])
def survey_recommendations(request):
    survey_response = request.data
    if not survey_response:
        return Response({"error": "survey_response is required"}, status=400)
    recommendations = ai_recommends(survey_response)["result"]
    # recommendations = "snasjncikudsn jndsiujcnskijb2 oaibdvodncoiands"
    return Response({"recommendations": recommendations}, status=200)

