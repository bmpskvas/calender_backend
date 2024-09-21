from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event


@api_view(['POST'])
def addevent(request):
  data = request.data
  print(data)
  Event.objects.create(title=data['title'], description=data['description'],
                       email=data['email'], start_time=data['start'], end_time=data['end'])
  return Response(({'message': 'event-added'}))


@api_view(['POST'])
def readevent(request):
    data = request.data
    email = data['email']
    if email:
        events = Event.objects.filter(email=email)  
        event_list = []
        
        for event in events:
            event_list.append({
                'title': event.title,
                'email': event.email,
                'description': event.description,
                'start': event.start_time,
                'end': event.end_time
            })
        
        return Response(event_list, status=200)  # Return the list of events
    else:
        return Response({'error': 'Email parameter is required'}, status=400)


@api_view(['POST'])
def deleteevent(request):
    data = request.data
    print(data)
    try:
        event = Event.objects.get(title=data['title'], email=data['email'])
        event.delete()  
        return Response({'message': 'event-deleted'}, status=200)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)
    
@api_view(['POST'])
def updateevent(request):
    data = request.data
    print(data)
    try:
        event = Event.objects.get(title=data['oldtitle'], email=data['oldemail'])
        event.title=data['newtitle']
        event.description=data['description']
        event.start_time=data['start']
        event.end_time=data['end']
        event.email=data['oldemail']
        event.save() 
        return Response({'message': 'event-updated'}, status=200)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)



