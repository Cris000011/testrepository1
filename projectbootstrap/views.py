from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        # Pobieramy dane przesłane z formularza (atrybuty 'name' z HTML)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Wypisujemy dane w konsoli (zobaczysz to w Anaconda Prompt lub logach Render)
        print("\n--- NOWA WIADOMOŚĆ Z FORMULARZA ---")
        print(f"Imię: {name}")
        print(f"Email: {email}")
        print(f"Telefon: {phone}")
        print(f"Wiadomość: {message}")
        print("------------------------------------\n")

        # Dodajemy powiadomienie, które wyświetli się na stronie
        messages.success(request, f"Dziękujemy {name}, Twoja wiadomość została odebrana!")

        # Przekierowujemy na dół strony do sekcji kontakt, aby uniknąć ponownego wysłania przy odświeżeniu
        return redirect('/#contact')

    # Jeśli to zwykłe wejście na stronę (GET), po prostu wyświetlamy index.html
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')

# Create your views here.
