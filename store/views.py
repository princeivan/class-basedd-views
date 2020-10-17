from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Book


@method_decorator(login_required, name='dispatch')

class BookListview(ListView):

    model = Book
    template_name = 'store/list.html'
    context_object_name = 'books'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(BookListview, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        
        try:
            books= paginator.page(page)

        except PageNotAnInteger:

            books = paginator.page(1)

        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books']
        return context

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'store/create.html'
    fields = ('name', 'isbn_number')
    success_url = reverse_lazy('book-list')


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'store/detail.html'
    context_object_name = 'book'


@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):

    model = Book
    template_name = 'store/update.html'
    context_object_name = 'book'
    fields = ('name', 'isbn_number')

    def get_success_url(self):
        return reverse_lazy('book-detail',kwargs={'pk':self.object.id})

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'store/delete.html'
    success_url = reverse_lazy('book-list')





