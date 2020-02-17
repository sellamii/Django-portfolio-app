from django.db import models

class Manager(models.Manager):
    def get_all(self):
        return self.all()

    def get_detail(self, pk):
        return self.get(pk=pk)