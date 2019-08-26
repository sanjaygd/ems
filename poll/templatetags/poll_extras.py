from django import template
from poll.models import Question

register = template.Library()


def upper(value):
    """Converts string into all uppercase """
    return value.upper()

register.filter('upper',upper)


@register.simple_tag
def recent_polls(n=5, **kwargs):
    """return recent n poll"""
    name = kwargs.get("name", "Arguement is not passed")
    print("recent poll kwargs check :", name)
    questions = Question.objects.all().order_by('-created_at')
    return questions