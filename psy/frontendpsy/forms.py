from django import forms
from django.forms import formset_factory
import datetime
from material import *
#from material.forms import Form
from django.forms import fields, models, formsets, widgets

class noFS_Form(forms.Form):

    campo1 = forms.CharField(label='campo1', max_length=100)
    campo2 = forms.CharField(label='campo2')
    campo3 = forms.CharField(label='campo3')
    campo4 = forms.EmailField(label='email', required=False)
    campo5 = forms.IntegerField(label='numero intero')
    campo6 = forms.DateField(initial = datetime.date.today)
    campo7 = forms.CharField(widget=forms.Textarea)
    campo8 = forms.ComboField(label='combo', fields=[forms.CharField(max_length=20), forms.EmailField()])

class ArticleForm(forms.Form):
    campo1cf = forms.CharField()
    campo2df = forms.DateField()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class BankForm(forms.Form):
    branch_name = forms.CharField()
    """ Personal Details """
    person_title = forms.ChoiceField(choices=(('Mr', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')), label='Title')
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    parent_name = forms.CharField(label='Nel caso di iscrizione ad un albo indicare quale')
    nationality = forms.ChoiceField(choices=())
    mobile_no = forms.CharField()
    existing_bank_account = forms.CharField()
    partner_name = forms.CharField(label='Descrizione dell Ordine')

    """ Residential address """
    flat_bulding = forms.CharField(label='Numero di iscrizione e tipo di sezione')
    road_no = forms.CharField(label='Numero di ...')
    area_and_landmark = forms.CharField(label='Luogo di esercizio')
    telephone_residence = forms.CharField()
    city = forms.CharField()
    office = forms.CharField()
    fax = forms.CharField()
    pin_code = forms.CharField()

    """ Mailing Address """
    mailing_company_details = forms.CharField(label="Denominazione dello studio")
    mailing_road_no = forms.CharField(label='Road no./name')
    mailing_area_and_landmark = forms.CharField(label='Area and landmark')
    mailing_city = forms.CharField(label='City')
    mailing_mobile = forms.CharField(label='Mobile No.')
    mailing_telephone_residence = forms.CharField(label='Telephone Residence')
    mailing_office = forms.CharField(label='Office')
    mailing_fax = forms.CharField(label='Fax')
    mailing_pin_code = forms.CharField(label='Pin Code')
    mailing_email = forms.EmailField(label='E-mail')

    """ Details of Introduction by Existing Customer """
    introducer_name = forms.CharField(label='Customer Name')
    introducer_account_no = forms.CharField(label='Account No.')
    introducer_signature = forms.CharField(label="Introducer's signature")

    """ Account Details """
    account_type = forms.ChoiceField(
        choices=(('S', 'Savings'), ('C', 'Current'), ('F', 'Fixed deposits')),
        label='Choice of account',
        widget=forms.RadioSelect)
    account_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    account_amount = forms.FloatField(label='Amount')

    """ Details of Fixed Deposit """
    deposit_type = forms.ChoiceField(
        choices=(('O', 'Ordinary'), ('C', 'Cumulative')),
        label='Types of deposit',
        widget=forms.RadioSelect)
    deposit_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    deposit_amount = forms.FloatField(label='Amount')
    deposit_no = forms.CharField(label='No. of deposits')
    deposit_individual_amount = forms.FloatField(label='Individual Deposit Amount')

    """ Personal Details """
    occupation = forms.ChoiceField(
        choices=(('NE', 'Non-executive'), ('HW', 'Housewife'), ('RT', 'Retired'),
                 ('ST', 'Student'), ('OT', 'Other'), ('UN', 'Unemployed')),
        widget=forms.RadioSelect)
    job_title = forms.CharField()
    department = forms.CharField()
    nature_of_business = forms.CharField()
    education = forms.ChoiceField(
        choices=(('UG', 'Under graduate'), ('GR', 'Graduate'), ('OT', 'Others')),
        widget=forms.RadioSelect)
    montly_income = forms.ChoiceField(
        choices=(('000', 'Zero Income'), ('L10', 'Less than $10,000'), ('G10', '$10,000+')),
        widget=forms.RadioSelect)
    martial_status = forms.ChoiceField(
        choices=(('M', 'Married'), ('S', 'Single')),
        widget=forms.RadioSelect)
    spouse_name = forms.CharField()

    """ Other existing bank accounts, if any """
    other_account1 = forms.CharField(label='Name of the Bank / branch')
    other_account2 = forms.CharField(label='Name of the Bank / branch')

    """ Reason for Account opening """
    reason = forms.CharField(label="Please specify", widget=forms.Textarea)

    """ Terms And Conditions """
    terms_accepted = forms.BooleanField(
        label="I/We confirm having read and understood the account rules of The Banking Corporation Limited"
        " ('the Bank'), and hereby agree to be bound by the terms and conditions and amendments governing the"
        " account(s) issued by the Bank from time-to-time.")

    
    layout = Layout(
        Fieldset("Please open an account at",
                 'branch_name'),
        Fieldset("Personal Details (Sole/First Accountholder/Minor)",
                 Row(Span2('person_title'), Span10('full_name')),
                 Row(Column('date_of_birth',
                            'email',
                            'parent_name'),
                     Column('nationality',
                            Row('mobile_no', 'existing_bank_account'),
                            'partner_name'))),
        Fieldset('Residential address',
                 Row('flat_bulding', 'road_no'),
                 Row(Span10('area_and_landmark'), Span2('city')),
                 Row('telephone_residence', 'office', 'fax', 'pin_code')),
        Fieldset("Mailing Address (If different from the First Accountholder's address)",
                 'mailing_company_details',
                 Row('mailing_road_no', 'mailing_area_and_landmark', 'mailing_city', 'mailing_mobile'),
                 Row('mailing_telephone_residence', 'mailing_office', 'mailing_fax', 'mailing_pin_code'),
                 'mailing_email'),
        Fieldset("Details of Introduction by Existing Customer (If applicable)",
                 Row('introducer_name', 'introducer_account_no'),
                 'introducer_signature'),
        Fieldset("Account Details",
                 Row('account_type', 'account_mode'),
                 'account_amount'),
        Fieldset("Details of Fixed Deposit",
                 Row('deposit_type', 'deposit_mode'),
                 Row(Span6('deposit_amount'), Span3('deposit_no'), Span3('deposit_individual_amount'))),
        Fieldset("Personal Details",
                 Row('occupation', 'education', 'montly_income'),
                 'job_title',
                 Row('department', 'nature_of_business'),
                 Row('martial_status', 'spouse_name')),
        Fieldset("Other existing bank accounts, if any",
                 Row('other_account1', 'other_account2')),
        Fieldset("Reason for Account opening",
                 'reason'),
        Fieldset("Terms And Conditions",
                 'terms_accepted')
    )



CONTACT_INFO_TYPES = (
    ('Phone', 'Phone'),
    ('Fax', 'Fax'),
    ('Email', 'Email'),
    ('AIM', 'AIM'),
    ('Gtalk', 'Gtalk/Jabber'),
    ('Yahoo', 'Yahoo'),
)

class ContactInfoForm(forms.Form):
    type = fields.ChoiceField(choices=CONTACT_INFO_TYPES)
    value = fields.CharField(max_length=200)
    preferred = fields.BooleanField(required=False)

ContactFormset = formsets.formset_factory(ContactInfoForm)
# Define a formset, which will allow a maximum of 5 contacts, no more:
MaxFiveContactsFormset = formsets.formset_factory(ContactInfoForm, extra=5, max_num=5)
# Define the same formset, with no forms (so we can demo the form template):
EmptyContactFormset = formsets.formset_factory(ContactInfoForm, extra=0)
try:
    # Define the same formset, which will require a minimum of 2 contacts, no extra
    MinTwoContactsFormset = formsets.formset_factory(ContactInfoForm, extra=0, min_num=2)
except:
    pass # django pre 1.7



#fin qui nessuna novità



#ArticleFormSet = formset_factory(ArticleForm)
