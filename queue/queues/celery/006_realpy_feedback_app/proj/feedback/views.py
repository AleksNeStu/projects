from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from feedback.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    # Line 12 defines .form_valid(), which FeedbackFormView automatically calls on a successful form submission. In line 13, you finally call .send_email().
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
