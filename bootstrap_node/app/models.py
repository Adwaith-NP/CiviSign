from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class Node(models.Model):
    node_name = models.CharField(max_length=30)
    node_ip = models.GenericIPAddressField(unique=True)
    node_password = models.CharField(max_length=255)
    connected_node = models.GenericIPAddressField(default="127.0.0.1")
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.node_name