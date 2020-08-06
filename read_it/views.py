from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
import random



def setup_book(user):

    business_books = Book.objects.filter(genre='business')
    childrens_books = Book.objects.filter(genre='childrens')
    classics_books = Book.objects.filter(genre='classics')
    fantasy_books = Book.objects.filter(genre='fantasy')
    history_books = Book.objects.filter(genre='history')
    horror_books = Book.objects.filter(genre='horror')
    mystery_books = Book.objects.filter(genre='mystery')
    nonfiction_books = Book.objects.filter(genre='nonfiction')
    romance_books = Book.objects.filter(genre='romance')
    scifi_books = Book.objects.filter(genre='science')
    sports_books = Book.objects.filter(genre='sports')
    youngadult_books = Book.objects.filter(genre='youngadult')

    if user.is_authenticated:
        profile = user.profile
        genre_profile = profile.genre_profile
    else:
        genre_profile = "010010010010010010010010010010010010"



    business_score = int(genre_profile[0:3])
    childrens_score = int(genre_profile[3:6])
    classics_score = int(genre_profile[6:9])
    fantasy_score = int(genre_profile[9:12])
    history_score = int(genre_profile[12:15])
    horror_score = int(genre_profile[15:18])
    mystery_score = int(genre_profile[18:21])
    nonfiction_score = int(genre_profile[21:24])
    romance_score = int(genre_profile[24:27])
    scifi_score = int(genre_profile[27:30])
    sports_score = int(genre_profile[30:33])
    youngadult_score = int(genre_profile[33:36])

    total_score = business_score + childrens_score + classics_score + fantasy_score + history_score + horror_score + mystery_score + nonfiction_score + romance_score + scifi_score + sports_score + youngadult_score

    business_percentage = (business_score / total_score) * 100
    childrens_percentage = (childrens_score / total_score) * 100
    classics_percentage = (classics_score / total_score) * 100
    fantasy_percentage = (fantasy_score / total_score) * 100
    history_percentage = (history_score / total_score) * 100
    horror_percentage = (horror_score / total_score) * 100
    mystery_percentage = (mystery_score / total_score) * 100
    nonfiction_percentage = (nonfiction_score / total_score) * 100
    romance_percentage = (romance_score / total_score) * 100
    scifi_percentage = (scifi_score / total_score) * 100
    sports_percentage = (sports_score / total_score) * 100
    youngadult_percentage = (youngadult_score / total_score) * 100

    random_num = random.randrange(100)
    if (0 < random_num and random_num < business_percentage):
        return random.choice(business_books)
    if (business_percentage < random_num and random_num < business_percentage + childrens_percentage):
        return random.choice(childrens_books)
    if (business_percentage + childrens_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage):
        return random.choice(classics_books)
    if (business_percentage + childrens_percentage + classics_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage):
        return random.choice(fantasy_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage):
        return random.choice(history_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage):
        return random.choice(horror_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage):
        return random.choice(mystery_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage):
        return random.choice(nonfiction_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage):
        return random.choice(romance_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage + scifi_percentage):
        return random.choice(scifi_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage + scifi_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage + scifi_percentage + sports_percentage):
        return random.choice(sports_books)
    if (business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage + scifi_percentage + sports_percentage < random_num and random_num < business_percentage + childrens_percentage + classics_percentage + fantasy_percentage + history_percentage + horror_percentage + mystery_percentage + nonfiction_percentage + romance_percentage + scifi_percentage + sports_percentage + youngadult_percentage):
        return random.choice(youngadult_books)



def home(request):
    book = setup_book(request.user)
    books = [
        {
            'title' : book.title.replace("*","'").replace("|",","),
            'genre' : book.genre.capitalize(),
            'author' : book.author.replace("*","'"),
            'cover_image_link' : book.cover_image_link,
            'number_of_pages' : book.number_of_pages,
            'audible_link' : book.audible_link,
            'barnes_noble_link' : book.barnes_noble_link,
            'amazon_link' : book.amazon_link,
            'google_link' : book.google_link,
            'rating' : book.rating,
            'synopsis' : book.synopsis.replace("|",",").replace("*","'"),
            'book_link' : book.title.replace(" ","_"),
        },
    ]
    if request.user.is_authenticated:
        likes = request.user.profile.book_set.all()
        return render(request,'read_it/home.html', {'books':books ,'likes':likes})
    else:
        return render(request, 'read_it/home.html', {'books': books})

@login_required
def upload(request):

    #file =
    #for line in file:
    #    Book.objects.create(title=line[0],genre=line[1],author=line[2],cover_image_link=line[3],number_of_pages=line[4],audible_link=line[5],barnes_noble_link=line[6],amazon_link=line[7],google_link=line[8],rating=line[9],synopsis=line[10])


    return render(request, 'read_it/home.html')

@login_required
def quiz(request):
    return render(request, 'read_it/quiz.html')

@login_required
def quiz_response(request, new_genre_profile="000000000000000000000000000000000001"):
    current_user = request.user.profile
    current_user.genre_profile = new_genre_profile
    current_user.save()

    return render(request, 'read_it/quiz_response.html')

@login_required
def book_liked(request, book_title):
    title = book_title.replace("_"," ")
    book = Book.objects.filter(title=title).first()
    if book==None:
        pass
    else:
        user = request.user.profile
        book.likes.add(user)

    return render(request, 'read_it/book_like.html')

def book_detail(request,book_title):
    title = book_title.replace("_", " ")
    book = Book.objects.filter(title=title).first()
    books = [
        {
            'title': book.title.replace("*", "'").replace("|", ","),
            'genre': book.genre.capitalize(),
            'author': book.author.replace("*", "'"),
            'cover_image_link': book.cover_image_link,
            'number_of_pages': book.number_of_pages,
            'audible_link': book.audible_link,
            'barnes_noble_link': book.barnes_noble_link,
            'amazon_link': book.amazon_link,
            'google_link': book.google_link,
            'rating': book.rating,
            'synopsis': book.synopsis.replace("|", ",").replace("*", "'"),
        },
    ]
    return render(request, 'read_it/book.html',{'books':books})

def recommend_book(request):
    return render(request, 'read_it/recommend.html')
