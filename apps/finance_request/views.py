from django.shortcuts import render, redirect
from apps.finance_request.api.services import get_clients, put_request, delete_request
from .models import RequestCredit


def index_clients(request):
    # Params for search or order in the api
    params = {'order': 'desc'}

    # get clients in the api
    clients = get_clients(params)

    # context for submit in the template
    context = {
        'clients': clients
    }
    return render(request, 'requests/index.html', context)


def delete_request_credit(request, pk=None):

    # get response in the api
    response = delete_request(pk=pk)
    print(response)

    # redirect
    return redirect('client_index')


def change_approved(request, pk=None):

    # search request credit in the database
    request_credit = RequestCredit.objects.filter(id=pk).first()

    # validation
    if request_credit:
        # change is_approved inverse
        if request_credit.is_approved:
            is_approved = False
        else:
            is_approved = True

        # construct data for submit in the api by put
        data = {
            "id": request_credit.id,
            "request_mount": request_credit.request_mount,
            "is_approved": is_approved,
            "client": request_credit.client.id
        }

        # call function for submit data
        response = put_request(pk, data)
        print(response)

        # redirect
    return redirect('client_index')



