from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calls/index.html', {
        "message": "This is calls page.",
        "calls": [
            {
                "callId": 1,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }, {
                "callId": 2,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }, {
                "callId": 3,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }, {
                "callId": 4,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }, {
                "callId": 5,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }, {
                "callId": 6,
                "customerName": "Javed Pathan",
                "callingTime": "8 Nov 2023 at 11:00 PM",
                "status": "DONE",
                "remark": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }
        ]
    })

def add_modal(request):
    return render(request, 'calls/add_modal.html', {
        "callTypes": [
            {
                "display": "Incoming",
                "value": "ICONMING"
            }, {
                "display": "Outgoing",
                "value": "OUTGOING"
            }, {
                "display": "Missed",
                "value": "MISSED"
            }
        ], "callDurationType": [
            {
                "display": "Seconds",
                "value": "SECONDS"
            }, {
                "display": "Minutes",
                "value": "MINUES"
            }
        ], "users": [
            {
                "display": "Javed Pathan",
                "value": "1",
                "disabled": "false"
            }, {
                "display": "Adil Pathan",
                "value": "2",
                "disabled": "false"
            }
        ], "customers": [
            {
                "display": "First Customer",
                "value": "1",
                "disabled": "false"
            }, {
                "display": "Secods Customer",
                "value": "2",
                "disabled": "false"
            }, {
                "display": "Third Customer",
                "value": "3",
                "disabled": "false"
            }, {
                "display": "Forth Customer",
                "value": "4",
                "disabled": "true"
            }
        ]
    })

def edit_modal(request):
    return render(request, 'calls/edit_modal.html', {
        "callTypes": [
            {
                "display": "Incoming",
                "value": "ICONMING"
            }, {
                "display": "Outgoing",
                "value": "OUTGOING"
            }, {
                "display": "Missed",
                "value": "MISSED"
            }
        ], "callDurationType": [
            {
                "display": "Seconds",
                "value": "SECONDS"
            }, {
                "display": "Minutes",
                "value": "MINUTES"
            }
        ], "users": [
            {
                "display": "Javed Pathan",
                "value": "1",
                "disabled": "false"
            }, {
                "display": "Adil Pathan",
                "value": "2",
                "disabled": "false"
            }
        ], "customers": [
            {
                "display": "First Customer",
                "value": "1",
                "disabled": "false"
            }, {
                "display": "Secods Customer",
                "value": "2",
                "disabled": "false"
            }, {
                "display": "Third Customer",
                "value": "3",
                "disabled": "false"
            }, {
                "display": "Forth Customer",
                "value": "4",
                "disabled": "true"
            }
        ], "call": {
            "call_id": "1",
            "caller_id": "1",
            "call_type": "ICONMING",
            "calling_time": "2024-01-01T07:00",
            "call_duration": "1.30",
            "call_duration_type": "MINUES",
            "customer_id": "3",
            "nodal_contact_id": "1",
            "purpose_of_the_call": "Custom Remark",
            "outcome_of_the_call": "Custom Remark",
            "is_call_recording_available": "true/false"
        }
    })

def delete_modal(request):
    return render(request, 'calls/delete_modal.html', {})