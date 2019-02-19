
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render


def index(request):

    return HttpResponse('index')


class BookListView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Book list view')


class AddBookView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'add_book.html')

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get('name')
        author_name = request.POST.get('author')
        print('BookName: {}\nAuthorName: {}'.format(book_name, author_name))
        return HttpResponse('success')


class BookDetail(View):

    def get(self, request, book_id):
        print('Book id: %s' % book_id)
        context = {
            'book_id': book_id,
        }
        return render(request, 'book_detail.html', context=context)

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        return super(BookDetail, self).dispatch(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('Method not supported.')


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {
            'cellphone': '123'
        }
        return context

