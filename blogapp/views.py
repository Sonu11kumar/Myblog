from django.shortcuts import render,get_object_or_404
from .form import PostForm, JoinForm
from .models import Post, Postman
from django.views.generic import FormView
from django.http import HttpResponseRedirect,JsonResponse,request
from .mixin import AjaxFormMixin
from django.contrib import messages


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Profile details updated.')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'form': form}

    return render(request, 'blogapp/blog.html', context)


def list(request):
    post = Postman.objects.all()
    context = {'post': post, }
    return render(request, 'blogapp/list.html', context)


def details(request, id=None):
    post = get_object_or_404(Postman, pk=id)
    context = {
        'title': post.title,
        'description': post.description,
        'publish': post.publish,
        'slug': post.slug,
        'post': post, }
    return render(request, 'blogapp/details.html', context)


class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = 'blogapp/ajax.html'
    success_url = '/form-success/'

    def form_invalid ( self,form ):
        response = super(JoinFormView,self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors,status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView,self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {'message': "Successfully submitted form data."}
            return JsonResponse(data)
        else:
            return response


