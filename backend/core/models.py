from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_images(self):
        items = Image.objects.filter(human_id=self.id)
        return [{'id': item.id, 'image': item.image.url} for item in items]


class Image(models.Model):
    human = models.ForeignKey(
        Human, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='human')

    def __str__(self):
        return self.human.name
