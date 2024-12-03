from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loan_elg(request):
    output='''<HTML>
    <BODY bgcolor=pink>
    <h2>this is loan eligibility page</h2>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response
