
from django.shortcuts import render
from django.http import Http404
from matplotlib.pyplot import title

# from LNK.notes.forms import NotesForm

from .forms import NotesForm
from . models import Notes
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from django.views.generic.edit import DeleteView

class NotesDeleteView(DeleteView):
    model=Notes
    success_url= '/smart/notes'
    template_name='notes/notes_delete.html '

class NotesUpdateView(UpdateView):
    model=Notes
    success_url='/smart/notes'
    form_class= NotesForm


class NotesCreateView(CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class= NotesForm

class NotesListView(ListView):
    model= Notes
    context_object_name="notes"
    template_name='notes/notes_list.html'

# def list(request):
#     all_notes=Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

class NotesDetailView(DetailView):
    model=Notes
    context_object_name="note"

# def detail(request,pk):
#     try:
#         note=Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Does not Exist")
#     return render(request,'notes/notes_detail.html',{'note':note})