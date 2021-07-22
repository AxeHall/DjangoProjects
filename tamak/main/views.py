from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import CustomUserCreationForm, CommentForm
from django.contrib import messages
from .models import Comment, Feedback
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class MainView(View):
    def get(self, request):
        return render(request, template_name="main/main.html")

class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")

class RegistrationView (View):
    def get(self, request):
        register_form = CustomUserCreationForm()
        return render(request,template_name="main/registration.html", context={"register_form": register_form})

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your account has been created successfully")
            return redirect("login")
        errors = register_form.errors
        register_form = CustomUserCreationForm()

        return render(request,template_name="main/registration.html", context={"register_form": register_form, "errors": errors})

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name="main/feedback_create.html"
    model = Feedback
    fields = ["feedback_text"]

    def get_success_url(self) -> str:
        return reverse("feedback_list")
    
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = self.request.user
        return super(FeedbackCreateView, self).form_valid(form)

class FeedbackListView(ListView):
    template_name = "main/feedback_list.html"
    model = Feedback

class FeedbackDetailView(DetailView):
    template_name = "main/feedback_details.html"
    model = Feedback

    def get_context_data(self, **kwargs):
        form = CommentForm()
        feedback = self.get_object()
        feedback_comments = Comment.objects.filter(feedback=feedback).order_by('-date_created')
        kwargs["form"] = form
        kwargs["comments"] = feedback_comments
        return super().get_context_data(**kwargs)
    
    def post(self, request, pk):
        form = CommentForm(request.POST)
        feedback = Feedback.objects.get(id=pk)
        feedback_comments = Comment.objects.filter(feedback=feedback).order_by('-date_created')
        form.save(commit=False)
        form.instance.creater = request.user
        form.instance.feedback = feedback

        if form.is_valid():
            form.save()
        form = CommentForm()
        return render(request, template_name="main/feedback_details.html", context={"form": form, "comments": feedback_comments})

class FeedbackUpdateView(UserPassesTestMixin, UpdateView):
    template_name = "main/feedback_update.html"
    model = Feedback
    fields = ["feedback_text"]

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False

class FeedbackDeleteView(UserPassesTestMixin, DeleteView):
    template_name = "main/feedback_delete.html"
    model = Feedback

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False

    def get_success_url(self) -> str:
        return reverse("feedback_list")