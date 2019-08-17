from django.shortcuts import render
from django.views.generic import TemplateView , CreateView
from django.views import View
from .models import First_Topic , Second_Topic , Third_Topic , Board_Message
from .forms import CreateTitleForm , BoardMessageForm , CreateTopicForm , SearchForm
from django.shortcuts import redirect


class Index(TemplateView):
    template_name = 'board/index.html'
board_index = Index.as_view()

class First_Topic_Page(View):
    def get(self, request, *args, **kwargs):
        first_topic = First_Topic.objects.all()
        return  render(request, 'board/first_topic.html', {'first_topic': first_topic,})
first_topic_page = First_Topic_Page.as_view()


class Second_Topic_Page(View):
    def get(self, request, first_topic_name, *args, **kwargs):
        form = CreateTopicForm(request.POST)
        searchform = SearchForm(request.POST)
        sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
        even_second_first_topic = Second_Topic.objects.filter(first_topic=sel_first_topic)[0::2]
        odd_second_first_topic = Second_Topic.objects.filter(first_topic=sel_first_topic)[1::2]
        return  render(request, 'board/second_topic.html', {'sel_first_topic': sel_first_topic,'form': form,'searchform':searchform,'even_second_first_topic': even_second_first_topic,'odd_second_first_topic': odd_second_first_topic,})
    #トピック作成
    def post(self, request, first_topic_name , *args, **kwargs):
        if request.POST['mode'] == '__create_topic__':
            sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
            form = CreateTopicForm(data=request.POST)
            if not form.is_valid():
                raise ValueError('Invailed form')
            second_topic = Second_Topic()
            second_topic.first_topic = sel_first_topic
            second_topic.second_topic = form.cleaned_data['second_topic']
            second_topic.save()
            return redirect(request.META['HTTP_REFERER'])
            return render(request, 'board/second_topic.html', {'form': form,'sel_first_topic': sel_first_topic,})
second_topic_page = Second_Topic_Page.as_view()


class Third_Topic_Page(CreateView):
    def get(self, request, first_topic_name ,second_topic_name, *args, **kwargs):
        form = CreateTitleForm(request.POST)
        searchform = SearchForm(request.POST)
        sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
        sel_second_topic = Second_Topic.objects.filter(second_topic=second_topic_name)
        sel_second_topic = sel_second_topic.get(first_topic=sel_first_topic)
        third_second_first_topic = Third_Topic.objects.filter(second_topic=sel_second_topic)
        even_third_second_first_topic = Third_Topic.objects.filter(second_topic=sel_second_topic)[0::2]
        odd_third_second_first_topic = Third_Topic.objects.filter(second_topic=sel_second_topic)[1::2]
        return  render(request, 'board/third_topic.html', {'third_second_first_topic': third_second_first_topic,'form': form,'sel_second_topic': sel_second_topic,'searchform':searchform,'even_third_second_first_topic': even_third_second_first_topic,'odd_third_second_first_topic': odd_third_second_first_topic,})
    #タイトル作成
    def post(self, request, first_topic_name ,second_topic_name, *args, **kwargs):
        if request.POST['mode'] == '__create_title__':
            sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
            sel_second_topic = Second_Topic.objects.filter(second_topic=second_topic_name)
            sel_second_topic = sel_second_topic.get(first_topic=sel_first_topic)
            form = CreateTitleForm(data=request.POST)
            if not form.is_valid():
                raise ValueError('Invailed form')
            third_topic = Third_Topic()
            third_topic.second_topic = sel_second_topic
            third_topic.third_topic = form.cleaned_data['third_topic']
            third_topic.save()
            return redirect(request.META['HTTP_REFERER'])
            return render(request, 'board/third_topic.html', {'form': form,'sel_second_topic': sel_second_topic,})
third_topic_page = Third_Topic_Page.as_view()

class Board(View):
    def get(self, request, first_topic_name ,second_topic_name, third_topic_name , *args, **kwargs):
        form = BoardMessageForm(request.POST)
        searchform = SearchForm(request.POST)
        sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
        sel_second_topic = Second_Topic.objects.filter(second_topic=second_topic_name)
        sel_second_topic = sel_second_topic.get(first_topic=sel_first_topic)
        sel_third_topic = Third_Topic.objects.filter(third_topic=third_topic_name)
        sel_third_topic = sel_third_topic.get(second_topic=sel_second_topic)
        sel_third_topic.views += 1
        message = Board_Message.objects.filter(third_topic=sel_third_topic).order_by('pub_date')
        message_count = Board_Message.objects.filter(third_topic=sel_third_topic).order_by('pub_date').count()
        sel_third_topic.talk_count = message_count
        sel_third_topic.save()
        return  render(request, 'board/board.html', {'message': message,'third_topic_name':third_topic_name,'form':form,'sel_third_topic':sel_third_topic,'message_count':message_count,'searchform':searchform,})
    #メッセージ入力
    def post(self, request, first_topic_name ,second_topic_name, third_topic_name , *args, **kwargs):
        if request.POST['mode'] == '__message_form__':
            sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
            sel_second_topic = Second_Topic.objects.filter(second_topic=second_topic_name)
            sel_second_topic = sel_second_topic.get(first_topic=sel_first_topic)
            sel_third_topic = Third_Topic.objects.filter(third_topic=third_topic_name)
            sel_third_topic = sel_third_topic.get(second_topic=sel_second_topic)
            form = BoardMessageForm(data=request.POST)
            if not form.is_valid():
                raise ValueError('Invailed form')
            msg = Board_Message()
            msg.screenname = form.cleaned_data['screenname']
            msg.content = form.cleaned_data['content']
            msg.first_topic = sel_first_topic
            msg.second_topic = sel_second_topic
            msg.third_topic = sel_third_topic
            msg.save()
            return redirect(request.META['HTTP_REFERER'])
        if request.POST['mode'] == '__search_form__':
            searchform = SearchForm(data=request.POST)
            form = BoardMessageForm(request.POST)
            sel_first_topic = First_Topic.objects.get(first_topic=first_topic_name)
            sel_second_topic = Second_Topic.objects.filter(second_topic=second_topic_name)
            sel_second_topic = sel_second_topic.get(first_topic=sel_first_topic)
            sel_third_topic = Third_Topic.objects.filter(third_topic=third_topic_name)
            sel_third_topic = sel_third_topic.get(second_topic=sel_second_topic)
            if not searchform.is_valid():
                raise ValueError('Invailed form')
            search_word = searchform.cleaned_data['search']
            message = Board_Message.objects.filter(third_topic=sel_third_topic).filter(content__contains=search_word)
            return  render(request, 'board/board.html', {'searchform':searchform,'message':message,'search_word':search_word,'form':form,'sel_third_topic':sel_third_topic,})
board = Board.as_view()

#タイトル検索
class Search_Result(View):
    def get(self, request ,search_word , *args, **kwargs):
        searchform = SearchForm(request.POST)
        even_search_result = Third_Topic.objects.filter(third_topic__contains=search_word)[0::2]
        odd_search_result = Third_Topic.objects.filter(third_topic__contains=search_word)[1::2]
        return  render(request, 'board/search_result.html', {'searchform':searchform,'even_search_result':even_search_result,'search_word':search_word,'odd_search_result':odd_search_result,})
    def post(self, request ,search_word , *args, **kwargs):
        if request.POST['mode'] == '__search_form__':
            searchform = SearchForm(data=request.POST)
            if not searchform.is_valid():
                raise ValueError('Invailed form')
            search_word = searchform.cleaned_data['search']
            return redirect('search_result' , search_word=search_word)
search_result = Search_Result.as_view()       
