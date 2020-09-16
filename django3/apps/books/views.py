from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import Book
from django.views.generic import ListView
# Create your views here.

def list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'book.html',context=context)

def del_book(request,id):
    # id = request.GET.get('id')
    # print(id)
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(reverse('books:list'))

def del_book2(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(reverse('books:list'))

def create_book(request):
    for i in range(1,201):
        Book.objects.create(id='%s'%i,name='图书%s'%i,price='%s'%i)

    return HttpResponse('创建成功')


class BookView(ListView):
    model = Book
    template_name = 'book.html'
    paginate_by = 10
    context_object_name = 'books'
    page_kwarg = 'p'

    def get_context_data(self, *, object_list=None, **kwargs):
        context =super(BookView, self).get_context_data()
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        new_context = self.my_context_data(paginator,page_obj)
        context.update(new_context)

        return context

    def my_context_data(self,paginator,page_obj,around_num=2):
        # 10(8,10)
        current_num = page_obj.number
        total = paginator.num_pages
        if current_num-around_num > 2 and current_num+around_num <= total - 2:
            left_range = range(page_obj.number-around_num,page_obj.number)
            right_range = range(page_obj.number+1,page_obj.number+around_num+1)
            first_btn = True
            last_btn = True

        elif current_num-around_num<=2:
            left_range = range(1,current_num)
            right_range = range(page_obj.number+1,current_num+around_num+1)
            first_btn = False
            last_btn = True

        else:
            left_range = range(page_obj.number-around_num,page_obj.number)
            right_range = range(current_num+1,total+1)
            first_btn = True
            last_btn = False

        my_context={
            'left_range':left_range,
            'right_range':right_range,
            'first_btn':first_btn,
            'last_btn':last_btn,
            'total':total,
        }

        return my_context