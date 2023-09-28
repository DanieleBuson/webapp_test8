from django.shortcuts import render, redirect
from .forms import ContactForm
import datetime
from .models import News

def main(request):
    return render(request, 'skaaltec_test8/main.html')

def solutions(request):
    return render(request, 'skaaltec_test8/solutions.html')

def aboutus(request):
    return render(request, 'skaaltec_test8/aboutus.html')

def news(request):
    all_news = News.objects.all()
    context = {
        'all_news': all_news,
    }
    return render(request, 'skaaltec_test8/news.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     subject=form.subject,
            #     message=form.message,
            #     from_email="busond5@gmail.com",
            #     recipient_list=[form.email],
            #     fail_silently=False,
            # )
            print(form.cleaned_data['name'])
            file = open('message_' + form.cleaned_data['name'] + str(datetime.date.today().strftime("%d%m%Y")) + ".txt", 'w')
            file.write("Subject:  " + form.cleaned_data['subject'] + "\n" + "Message: " + form.cleaned_data['message'])
            file.close()
            return render(request, 'skaaltec_test8/main.html', {'message': 'We received your message, we will answer as soon as possible. Thanks for you patient!'})
    else:
        form = ContactForm()
    return render(request, "skaaltec_test8/contactus.html", {'form': form})