from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Student, Group, Exam

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'student_group', 'birthday', 'photo', 'ticket', 'notes')
        help_texts = {'birthday':'* 1995-04-25', }

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'leader')



class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('title', 'data', 'ticher_name', 'exam_group')
        help_texts = {'data':'2017-10-02 07:25:27',}


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('students:contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    from_email = forms.EmailField(label=u"Ваша Емейл Адреса")

    subject = forms.CharField(label=u"Заголовок листа", max_length=128)

    message = forms.CharField(label=u"Текст повідомлення", widget=forms.Textarea)

