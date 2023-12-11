import json
from datetime import datetime, timezone
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User

from call_log.models import CallLog
from contact_person.models import ContactPerson
from lead.models import Lead

def index(request):
    if request.user.is_anonymous:
        return redirect("/admin/login")

    return render(request, 'call_log/index.html', {
        "message": "This is calls page.",
        "callLogs": [
            {
                'call_log_id': callLog.call_log_id,
                'company_name': callLog.lead.company_name,
                'person_name': callLog.contact_person.person_name,
                'calling_time': callLog.calling_time,
                'call_duration': callLog.call_duration,
                'call_type': callLog.call_type,
                'creator_name': f"{callLog.creator.first_name} {callLog.creator.last_name}",
                'created_date': callLog.created_date
                } for callLog in CallLog.objects.all()]
    })

def add_modal(request):
    leadList = Lead.objects.all()
    contactPersons = []
    if len(leadList) > 0:
        contactPersons = [{'display': f'{contactPerson.person_name}', 'value': f'{contactPerson.contact_person_id}'} for contactPerson in ContactPerson.objects.filter(lead=leadList[0])]
    
    return render(request, 'call_log/add_modal.html', {
        "callTypes": [
            {
                "display": "Incoming",
                "value": "I"
            }, {
                "display": "Outgoing",
                "value": "O"
            }, {
                "display": "Missed",
                "value": "M"
            }
        ],
        "callers": [{'display': f'{user.first_name} {user.last_name}', 'value': user.id} for user in User.objects.all()], 
        "leads": [{'display': f'{lead.company_name}', 'value': f'{lead.lead_id}'} for lead in leadList],
        "contactPersons": contactPersons
    })

def add(request):
    if request.method == 'POST':
        try:
            # Retrieve JSON data from the request body
            requestBody = json.loads(request.body.decode('utf-8'))

            # Access the JSON data
            caller=User.objects.filter(id=requestBody.get('caller_id')).first()
            lead=Lead.objects.filter(lead_id=requestBody.get('lead_id')).first()
            contactPerson=ContactPerson.objects.filter(contact_person_id=requestBody.get('contact_person_id')).first()

            # Your logic with the JSON data here
            callLog = CallLog(caller=caller, lead=lead, contact_person=contactPerson, call_type=requestBody.get('call_type'), calling_time=requestBody.get('calling_time'), call_duration=requestBody.get('call_duration'), purpose_of_the_call=requestBody.get('purpose_of_the_call'), outcome_of_the_call=requestBody.get('outcome_of_the_call'), is_call_recording_available=requestBody.get('is_call_recording_available'), call_recording_urls={}, created_date=datetime.now(), creator=request.user, changed_date=datetime.now(), changer=request.user, is_deleted=False)
            callLog.save()

            # Example: Return a JSON response
            response = JsonResponse({'messageType': 'success', 'message': f'Call log successfully created.'}, status=201)
            response['Content-Type'] = 'application/json'
            return response
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def edit_modal(request, uuid):
    leadList = Lead.objects.all()
    contactPersons = []
    if len(leadList) > 0:
        contactPersons = [{'display': f'{contactPerson.person_name}', 'value': f'{contactPerson.contact_person_id}'} for contactPerson in ContactPerson.objects.filter(lead=leadList[0])]

    # Retrieve the object using the UUID
    callLog = CallLog.objects.filter(call_log_id=uuid).first()

    return render(request, 'call_log/edit_modal.html', {
        "callTypes": [
            {
                "display": "Incoming",
                "value": "I"
            }, {
                "display": "Outgoing",
                "value": "O"
            }, {
                "display": "Missed",
                "value": "M"
            }
        ],
        "callers": [{'display': f'{user.first_name} {user.last_name}', 'value': user.id} for user in User.objects.all()], 
        "leads": [{'display': f'{lead.company_name}', 'value': f'{lead.lead_id}'} for lead in leadList],
        "contactPersons": contactPersons,
        "callLog": {
            "call_log_id": callLog.call_log_id,
            "caller_id": callLog.caller.pk,
            "call_type": callLog.call_type,
            "calling_time": callLog.calling_time.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M'),
            "call_duration": callLog.call_duration.strftime('%H:%M:%S'),
            "lead_id": callLog.lead.lead_id,
            "contact_person_id": callLog.contact_person.contact_person_id,
            "purpose_of_the_call": callLog.purpose_of_the_call,
            "outcome_of_the_call": callLog.outcome_of_the_call,
            "is_call_recording_available": callLog.is_call_recording_available
        }
    })

def edit(request, uuid):
    if request.method == 'PUT':
        try:
            # Retrieve JSON data from the request body
            requestBody = json.loads(request.body.decode('utf-8'))

            # Access the JSON data
            caller=User.objects.filter(id=requestBody.get('caller_id')).first()
            lead=Lead.objects.filter(lead_id=requestBody.get('lead_id')).first()
            contactPerson=ContactPerson.objects.filter(contact_person_id=requestBody.get('contact_person_id')).first()

            # Your logic with the JSON data here
            callLog = CallLog.objects.filter(call_log_id=uuid).first()
            callLog.caller=caller
            callLog.lead=lead
            callLog.contact_person=contactPerson
            callLog.call_type=requestBody.get('call_type')
            callLog.calling_time=requestBody.get('calling_time')
            callLog.call_duration=requestBody.get('call_duration')
            callLog.purpose_of_the_call=requestBody.get('purpose_of_the_call')
            callLog.outcome_of_the_call=requestBody.get('outcome_of_the_call')
            callLog.is_call_recording_available=requestBody.get('is_call_recording_available')
            callLog.call_recording_urls=[]
            callLog.changed_date=datetime.now()
            callLog.changer=request.user
            callLog.save()

            # Example: Return a JSON response
            response = JsonResponse({'messageType': 'success', 'message': f'Call log successfully updated.'}, status=201)
            response['Content-Type'] = 'application/json'

            return response
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def delete_modal(request):
    return render(request, 'call_log/delete_modal.html', {})

def delete(request):
    return render(request, "")