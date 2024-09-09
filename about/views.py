from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary, Contact, Slider, Text
from .sarializer import ScientificTeamSerializer, ScientistsSerializer, ExpressionsSerializer, NewsSerializer, \
    ProvensiyaSerializer, DictionarySerializer, ContactSerializer, SliderSerializer, TextSerializer


@api_view(['GET'])
def scientific_team_list(request):
    teams = ScientificTeam.objects.all()
    serializer = ScientificTeamSerializer(teams, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def scientific_team_detail(request, pk):
    try:
        team = ScientificTeam.objects.get(pk=pk)
    except ScientificTeam.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ScientificTeamSerializer(team, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def scientists_list(request):
    scientists = Scientists.objects.all()
    serializer = ScientistsSerializer(scientists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def expressions_list(request):
    expressions = Expressions.objects.all()
    serializer = ExpressionsSerializer(expressions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_list(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, pk):
    try:
        news_item = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = NewsSerializer(news_item, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def provensiya_list(request):
    provensiyas = Provensiya.objects.all()
    serializer = ProvensiyaSerializer(provensiyas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dictionary_list(request):
    dictionaries = Dictionary.objects.all()
    serializer = DictionarySerializer(dictionaries, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_list_create(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def slider_list(request):
    if request.method == 'GET':
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        for slider in serializer.data:
            slider['image'] = request.build_absolute_uri(slider['image'])
        return Response(serializer.data)


@api_view(['GET'])
def text_list(request):
    text = Text.objects.all()
    serializer = TextSerializer(text, many=True)
    return Response(serializer.data)
