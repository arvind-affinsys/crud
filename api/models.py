from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " | " + str(self.completed)


class Log(models.Model):
    request_body = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    ip_address = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.path + " | " + str(self.status)
