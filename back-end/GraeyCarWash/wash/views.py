from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum, ExpressionWrapper, DecimalField, Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from user.models import User
# @TODO: Add Manager Method For Washer Listing
from wash.forms import OrderForm
from wash.models import Order


def washer_list_view(request: WSGIRequest) -> HttpResponse:
    washer_q = Q()
    order_q = Q()
    q = request.GET.get('q')

    if q:
        washer_q &= Q(first_name__icontains=q[-1]) | Q(last_name__icontains=q[-1])
        order_q &= Q(employee__first_name__icontains=q[-1]) | Q(employee__last_name__icontains=q[-1])

    profit_q = ExpressionWrapper(
        F('price') * (1 - F('employee__salary') / Decimal('100.0')),
        output_field=DecimalField()
    )
    order_info: Dict[str, Optional[Decimal]] = Order.objects.filter(end_date__isnull=False).filter(order_q) \
        .annotate(profit_per_order=profit_q) \
        .aggregate(profit=Sum('profit_per_order'), total=Count('id'))

    context = {
        'washers': User.objects.filter(status=User.Status.washer.value).filter(washer_q).annotate(
            washed_count=Count('orders')),
        # **order_info
    }
    context.update(order_info)

    return render(request=request, template_name='wash/washer-list.html', context=context)


# Dispatch (type) -> view

class WasherDetail(DetailView):
    form = OrderForm
    template_name='wash/washer-detail.html'
    context_object_name = 'washer'
    queryset = User.objects.filter(status=User.Status.washer)
    model = User

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        order_form = self.form(request.POST)
        if order_form.is_valid():
            order: Order = order_form.save(commit=False)
            order.employee_id = self.object.pk
            try:
                start_date = datetime.strptime(
                    " ".join([
                        order_form.cleaned_data['start_date_day'],
                        order_form.cleaned_data['start_date_time']
                    ]),
                    '%d/%m/%Y %H:%M'
                )
                order.start_date = start_date
                order.save()
                order_form = self.form
            except ValueError:
                order_form.add_error('start_date_day', 'პაპს ნუ ატყუებ')
        return render(request, self.template_name, self.get_context_data(
            form=order_form
        ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        earned_money_q = ExpressionWrapper(
            F('price') * F('employee__salary') / Decimal('100.0'),
            output_field=DecimalField()
        )
        now = timezone.now()
        washer_salary_info: Dict[str, Optional[Decimal]] = self.object.orders.filter(end_date__isnull=False) \
            .annotate(earned_per_order=earned_money_q) \
            .aggregate(
            earned_money_year=Sum(
                'earned_per_order',
                filter=Q(end_date__gte=now - timezone.timedelta(days=365))
            ),
            washed_last_year=Count(
                'id',
                filter=Q(end_date__gte=now - timezone.timedelta(days=365))
            ),
            earned_money_month=Sum(
                'earned_per_order',
                filter=Q(end_date__gte=now - timezone.timedelta(weeks=4))
            ),
            washed_last_month=Count(
                'id',
                filter=Q(end_date__gte=now - timezone.timedelta(weeks=4))
            ),
            earned_money_week=Sum(
                'earned_per_order',
                filter=Q(end_date__gte=now - timezone.timedelta(days=7))
            ),
            washed_last_week=Count(
                'id',
                filter=Q(end_date__gte=now - timezone.timedelta(days=7))
            )
        )
        form = kwargs.get('form', self.form)
        return {**context, **washer_salary_info, 'order_form': form}
