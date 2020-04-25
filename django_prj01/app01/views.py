from django.shortcuts import render

def index( request ) :
    return render( request, 'app01/index.html')


def help( request ) :
    return render( request, 'app01/help.html')
