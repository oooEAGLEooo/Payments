from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment
import json
from datetime import datetime

def build_dashboard(request): 
    # Определяем тип графика из GET параметра
    chart_type = request.GET.get('type', 'line')
    
    if chart_type == 'line':
        # Для линейного графика - группируем по датам и суммируем
        from django.db.models import Sum
        from django.db.models.functions import TruncDate
        
        # Группируем платежи по дате (без времени) и суммируем
        daily_totals = Payment.objects.annotate(
            date_only=TruncDate('pay_date') 
        ).values('date_only').annotate(
            total_amount=Sum('amount')
        ).order_by('date_only')
        
        labels = [item['date_only'].strftime('%Y-%m-%d') for item in daily_totals]
        data = [float(item['total_amount']) for item in daily_totals]
        chart_title = "Сумма платежей по дням"
    else:
        # Для гистограммы - группируем по клиентам и суммируем платежи
        from django.db.models import Sum
        
        # Группируем платежи по клиентам и суммируем
        client_totals = Payment.objects.values(
            'payer__first_name', 
            'payer__last_name'
        ).annotate(
            total_amount=Sum('amount')
        ).order_by('payer__last_name')
        
        labels = [f"{item['payer__first_name']} {item['payer__last_name']}" for item in client_totals]
        data = [float(item['total_amount']) for item in client_totals]
        chart_title = "Общая сумма платежей по плательщикам"
    
    context = {
        'chart_type': chart_type,
        'labels': labels,
        'data': data,
        'chart_title': chart_title,
        'next_chart_type': 'bar' if chart_type == 'line' else 'line',
        'next_chart_button': 'Гистограмма' if chart_type == 'line' else 'Линейный график',
    }
    
    return render(request, 'payments_app/dashboard.html', context)
