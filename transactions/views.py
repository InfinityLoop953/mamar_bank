from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT
from transactions.forms import DepositForm
from transactions.models import Transaction


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'account': self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': self.title})
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        return {'transaction_type': DEPOSIT}

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        # Update account balance
        account.balance += amount
        account.save(update_fields=['balance'])

        # Create a transaction record
        Transaction.objects.create(
            account=account,
            amount=amount,
            balance_after_transaction=account.balance,
            transaction_type=DEPOSIT
        )

        messages.success(
            self.request,
            f'${amount:.2f} was deposited to your account successfully'
        )

        return super().form_valid(form)




class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    context_object_name = 'object_list'

    def get_queryset(self):
        # Fetch only the latest 10 transactions for simplicity
        return Transaction.objects.filter(account=self.request.user.account).order_by('-timestamp')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user.account
        return context