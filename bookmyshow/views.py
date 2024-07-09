
from rest_framework.decorators import api_view
from .models import Flight,Booking
from django.contrib.auth import  login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from.forms import SignupForm ,Authentication
from rest_framework.exceptions import ValidationError
from .serializer import Validator,BookSerializer


@api_view(['POST'])
def logins(request):
    if not request.user.is_authenticated ==True:
        print(request.data)
        fm = Authentication(request=request,data=request.POST)
        if fm.is_valid():
            print("hello")
            username  = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username = username,password =password)
            login(request,user)
            return Response({} , status=202)
        if not fm.is_valid():
            raise ValidationError(fm.errors)
    else:
        return Response({} , status=406)
    


@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({} ,status=200)

    

@api_view(["POST"])
def register_account(request):
    if not request.user.is_authenticated ==True:
        print(request.POST)
        if request.method =="POST":
            print(request.data)
            form = SignupForm(request.data)
            if form.is_valid():
                user = form.save(commit=True)
                user.set_password(form.cleaned_data["password1"])
                login(request ,user)
                return Response({} ,status=201)
            elif not form.is_valid():
                raise ValidationError(form.errors)
        else:
            return Response({} , status=403)
    else:
       return Response({} , status=406)
    

@api_view(['POST'])
def book_flight(request):
    def book_flight(request):
        try:
            # Extract flight number from the request
            number = request.data.get("flight")
            if not number:
                return Response({"error": "Flight number is required."}, status=400)

            # Get the flight object
            flight = Flight.objects.get(flight_number=number)
            
            # Check if there are available seats
            if flight.available_seats > 0:
                # Create a booking
                booking = Booking.objects.create(user=request.user, flight=flight)
                # Decrease available seats
                flight.available_seats -= 1
                flight.save()
                return Response({"message": "Booking successful."}, status=200)
            else:
                return Response({"error": "No available seats."}, status=400)
        except Flight.DoesNotExist:
            return Response({"error": "Flight not found."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    


@login_required
@api_view(['POST'])    
def search_flights(request):
    if request.method == 'POST':
        date = request.data.get('date')
        flights = Validator(Flight.objects.filter(departure_time__date=date),many=True)
        return Response(flights.data,status= 200)


        

        

@login_required
@api_view(['POST'])
def view_flight(request):
    serializers = Validator(Flight.objects.all(),many=True)
    return Response(serializers.data,status=200)


@login_required
@api_view(['POST'])
def my_bookings(request):
    bookings = BookSerializer(Booking.objects.filter(user=request.user),many =True)
    return Response(bookings.data,status=200)
    

    