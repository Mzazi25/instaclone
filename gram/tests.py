from django.test import TestCase
from .models import Image,Profile,Comment

# Create your tests here.
class ImageTestClass(TestCase):
    # testing image
    def setUp(self):
        self.image= Image(name = 'James', description ='image')
    # Testing  profile
    def setUp(self):
        self.profile= Profile(profile="Mzazi")
        # Testing comments
    def setUp(self):
        self.Comment= Comment(comment="news")
    
    # Testing Save Method
    def test_save_method(self):
        self.image.save()
        self.profile.save()
        self.Comment.save()

    def tearDown(self):        
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()

        