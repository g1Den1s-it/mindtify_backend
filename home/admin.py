from django.contrib import admin

from home.models import (
    Test,
    Question,
    Choice,
    TextAnswer,
    ResponseTest
)
# Register your models here.

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TextAnswer)
admin.site.register(ResponseTest)
