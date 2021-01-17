from django.core.files import File
from PIL import Image
from io import BytesIO
from django.db import models


def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    image = models.ImageField(
        upload_to=user_directory_path, default='images/default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, *args, **kwargs):
        if self.image:
            compImage = self.image
            if compImage.size > 0.3*1024*1024:  # if size greater than 300kb then it will send to compress image function
                self.image = compress_image(compImage)
        super(Images, self).save(*args, **kwargs)


def compress_image(image):
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality=30, optimize=True)
    new_image = File(im_io, name=image.name)
    return new_image
