from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import FormMixin


class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):

        #получаем форму

        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        #list view
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404()
        

        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

