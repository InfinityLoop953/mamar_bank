from django.urls import path
from .views import DepositMoneyView,TransactionReportView,WithdrawMoneyView,LoanRequestView



urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
     path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
      path("loan_request/", LoanRequestView.as_view(), name="loan_request"),

]