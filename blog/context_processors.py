from .forms import PostSearchForm
from .models import Category,MainContent
def add_variable_to_context(request):
    """
    This func is return some custom variable that I access this variable in my template. With out
    passing this variable in my context dict in my view func

    """
    return {
        'categories': Category.objects.all(),
        'slide_show':MainContent.objects.all(),
        'form' : PostSearchForm(),

    }
