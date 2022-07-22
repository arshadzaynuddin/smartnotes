
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from matplotlib.pyplot import title

# from LNK.notes.forms import NotesForm

from .forms import NotesForm
from . models import Notes
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url= '/smart/notes'
    template_name='notes/notes_delete.html'
    login_url="/login"

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=Notes
    success_url='/smart/notes'
    form_class= NotesForm
    login_url="/login"


class NotesCreateView(LoginRequiredMixin,CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class= NotesForm
    login_url="/login"

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())    

  


class NotesListView(LoginRequiredMixin,ListView):
    model= Notes
    context_object_name="notes"
    template_name='notes/notes_list.html'
    login_url="/login"

    def get_queryset(self):
        return self.request.user.notes.all()



        

# def list(request):
#     all_notes=Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

class NotesDetailView(DetailView):
    model=Notes
    context_object_name="note"
    # login_url="/admin"

# def detail(request,pk):
#     try:
#         note=Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Does not Exist")
#     return render(request,'notes/notes_detail.html',{'note':note})
