from django.shortcuts import render


def book(request):
    return render(request, 'tourism/book.html')

def book_list(request):
    from tourism.views import book_list

    return render(request, 'tourism/booklist.html')
    

def view_booking(request):
    return render(request, 'tourism/view.html')

def payment(request):
    return render(request, 'tourism/payment.html')

def refund(request):
    return render(request, 'tourism/refund.html')


# Create your views here.
