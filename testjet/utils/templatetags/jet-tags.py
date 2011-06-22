from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

register = template.Library()

class EditLinkNode(template.Node):

    def __init__(self, obj_str):
        self.obj_str = obj_str
    
    def render(self, context):
        obj = context[self.obj_str]
        ct = ContentType.objects.get_for_model(obj)

        return reverse("admin:%s_%s_change" % (ct.app_label, ct.model), args=(obj.pk,))

def do_edit_link(parser, token):
    try:
        tag_name, obj_str = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" 
                                            % token.contents.split()[0])

    return EditLinkNode(obj_str)

register.tag('edit_link', do_edit_link)
