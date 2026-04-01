from django.http import HttpResponse
import random
import string

def home_page(request):
    return HttpResponse("""<h1 style="color:red;font-weight:bold;">"Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here<h1>""")  

def careRentals_services(request):
    return HttpResponse("""<p style="color:red;font-weight:bold;"> Our Services: We offer a wide range of vehicles for rent,Our rental processis simple and convenient, allowing you tobook your desired vehicle online or at our rental locations. We also provide flexible rental durations to suit your needs</p>""")

def password_generator(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return HttpResponse(f"""<h2 style="color:blue;font-weight:bold;">Generated Password: {password}</h2>""")