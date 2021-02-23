from .forms import PostSearchForm
from .models import Category,MainContent
def add_variable_to_context(request):
    return {
        'categories': Category.objects.all(),
        'slide_show':MainContent.objects.all(),
        'form' : PostSearchForm(),

    }
