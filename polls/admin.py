from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    """Lets the admin add choices on the same page as the question."""
    model = Choice
    extra = 3  # shows 3 empty choice rows by default


class QuestionAdmin(admin.ModelAdmin):
    """Customises how Question appears in the admin panel."""
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)