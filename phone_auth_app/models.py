from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=10, blank=True, null=True)
    used_invite_codes = models.ManyToManyField("self", symmetrical=False, related_name="invited_by", blank=True)

    def __str__(self):
        return self.phone_number
