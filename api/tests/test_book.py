from django.urls import reverse
from rest_framework import status,test
from django.contrib.auth import get_user_model
from api.models import Book,Genre,Author,Review,Order

User = get_user_model()

class BookViewSetTestCase(test.APITestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(phone_number="+998521245163",password="staffPass",is_staff=True)
        self.user = User.objects.create_user(phone_number="+998901234567",password="testPass")

        self.author = Author.objects.create(name="alibek",age=17)

        self.genre1 = Genre.objects.create(name="psychological")
        self.genre2 = Genre.objects.create(name="historical")

        self.book1 = Book.objects.create(stock=30,title="Dark Psychology 101",genre=self.genre1,price=12000,pages=451,author=self.author)
        self.book2 = Book.objects.create(stock=30,title="Jangchi",genre=self.genre2,price=51000,pages=546,author=self.author)

        Review.objects.create(user=self.user,book=self.book1,rating=5)
        Review.objects.create(user=self.user,book=self.book1,rating=4)
        Review.objects.create(user=self.user,book=self.book2,rating=2)

    def test_book_list(self):
        url = reverse('book-list')
        self.client.force_authenticate(self.staff_user) #only staff users have permission
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_genre_list(self):
        url = reverse("genre-list")
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_book_list_filter_by_genre(self):
        url = reverse("book-list")+"?genre="+str(self.genre1.id)
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]),1)
    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book1.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['book']['title'], 'Dark Psychology 101')

    def test_average_rating(self):
        url = reverse('book-average-rating', args=[self.book1.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_rating'], 4.5) # avg(5,4)
    def test_permission_deny_for_anonymous(self):
        self.client.force_authenticate(user=None)  # "Log out"
        url = reverse('book-list')
        data = {'name': 'Test Product', 'description': 'This is a test product', 'price': 10.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_permission_granted_for_staff(self):
        url = reverse('book-list')
        self.client.force_authenticate(self.staff_user)
        data = {'title': 'Test Product', 'description': 'This is a test product', 'price': 1000,"pages":356,"stock":35,"genre":1,"author":1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)