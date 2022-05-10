from tkinter import font
import xlwt
from datetime import datetime
from email.mime import application
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VehicleForm, ProviderForm, SuplyForm, MaintenanceForm, TrafficForm
from .models import Vehicle, Provider, Supply, Maintenance, Traffic

# Create your views here.


@login_required(login_url='login')
def index(request):
    veiculos = Vehicle.objects.all()
    fornecedores = Provider.objects.all()
    abastecimentos = Supply.objects.all()
    manutencoes = Maintenance.objects.all()
    trafegos = Traffic.objects.all()

    context = {
        'veiculos': veiculos,
        'fornecedores': fornecedores,
        'abastecimentos': abastecimentos,
        'manutencoes': manutencoes,
        'trafegos': trafegos
    }
    return render(request, 'relatorio-geral.html', context=context)



"""============================================== ABASTECIMENTO =================================================="""


@login_required(login_url='login')
def abast(request):
    form = SuplyForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            
            form.save()

            try:
                messages.info(request, 'Dados cadastrados com sucesso!')
            except messages.error:
                messages.info(request, 'Ops, algo deu errado!')

            return redirect('abast')
    
    abastecimentos = Supply.objects.all()
    form = SuplyForm()
        
    return render(request, 'abast.html', {'abastecimentos': abastecimentos, 'form': form})


@login_required(login_url='login')
def update_abast(request, id):
    abastecimento = Supply.objects.get(id=id)
    form = SuplyForm(request.POST or None, instance=abastecimento)

    if form.is_valid():
        form.save()
        
        try:
            messages.info(request, 'Dados alterados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')
            
        return redirect('abast')

    return render(request, 'abast.html', {'abastecimento': abastecimento, 'form': form})


@login_required(login_url='login')
def delete_abast(request, id):
    abastecimento = Supply.objects.get(id=id)

    if request.method == 'GET':
        abastecimento.delete()

        try:
            messages.info(request, 'Dados deletados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('abast')
    
    return render(request, 'abast.html', {'abastecimento': abastecimento})


@login_required(login_url='login')
def export_excel_abastecimento(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Expenses" + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Litros', 'Km', 'Valor', 'Pg', 'Motorista', 'Veículo', 'Marca', 'Dt.abast']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Supply.objects.values_list('id', 'amount_ofag_liters', 'milee', 'supply_value', 'payment', 'driver_name', 'vehicle', 'mark_supply', 'date_supply')

    for row in rows:
        row_num += 1

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


"""=============================================== FORNECEDOR ===================================================="""

@login_required(login_url='login')
def fornecedor(request):
    form = ProviderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            try:
                messages.info(request, 'Dados cadastrados com sucesso!')
            except messages.error:
                pass

            return redirect('fornecedor')

    fornecedores = Provider.objects.all()
    form = ProviderForm()
    
    return render(request, 'fornecedores.html', {'form': form, 'fornecedores': fornecedores})


@login_required(login_url='login')
def update_fornecedor(request, id):
    fornecedor = Provider.objects.get(id=id)
    form = ProviderForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()

        try:
            messages.info(request, 'Dados alterados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('fornecedor')

    return render(request, 'fornecedores.html', {'fornecedor': fornecedor, 'form': form})


@login_required(login_url='login')
def delete_fornecedor(request, id):
    fornecedor = Provider.objects.get(id=id)
    
    if request.method == 'GET':
        fornecedor.delete()

        try:
            messages.info(request, 'Dados deletados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('fornecedor')

    return render(request, 'fornecedores.html', {'fornecedor': fornecedor})


@login_required(login_url='login')
def export_excel_fornecedor(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Expenses" + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Nome', 'Endereço', 'Número', '', 'Bairro', 'Cidade', 'Telefone', 'Email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Provider.objects.values_list('id', 'provide_name', 'address', 'number', 'district', 'city', 'phone_number', 'email', 'date_create')

    for row in rows:
        row_num += 1

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


'''=============================================== MANUTENÇÃO ===================================================='''
@login_required(login_url='login')
def manutencao(request):
    form = MaintenanceForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
    
            form.save()

            try:
                messages.info(request, 'Dados cadastrados com sucesso!')
            except messages.error:
                messages.info(request, 'Ops, algo deu errado!')

            return redirect('manutencao')
    
    manutencoes = Maintenance.objects.all()
    form = MaintenanceForm()

    return render(request, 'manutencao.html', {'form': form, 'manutencoes': manutencoes})


@login_required(login_url='login')
def update_manutencao(request, id):
    manutencao = Maintenance.objects.get(id=id)
    form = MaintenanceForm(request.POST or None, instance=manutencao)

    if form.is_valid():
        form.save()

        try:
            messages.info(request, 'Dados alterados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('manutencao')

    return render(request, 'manutencao.html', {'manutencao': manutencao, 'form': form,})
    

@login_required(login_url='login')
def delete_manutencao(request, id):
    manutencao = Maintenance.objects.get(id=id)
    if request.method == 'GET':
        manutencao.delete()

        try:
            messages.info(request, 'Dados deletados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('manutencao')

    return render(request, 'manutencao.html', {'manutencao': manutencao})


@login_required(login_url='login')
def export_excel_manutencao(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Expenses" + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Dt.saída', 'Serviço', 'Dt.entrega', 'Fornecedor', 'Veículo', 'Marca', 'Valor', 'Prox.serviço']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Maintenance.objects.values_list('id', 'departure_date', 'service', 'delivery_date', 'provider', 'vehicle', 'mark_main', 'value', 'next_service')

    for row in rows:
        row_num += 1

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


"""=============================================== TRÁFEGO ======================================================="""
@login_required(login_url='login')
def trafego(request):
    form = TrafficForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            try:
                messages.info(request, 'Dados cadastrados com sucesso!')
            except messages.error:
                messages.info(request, 'Ops, algo deu errado!')

            return redirect('trafego')

    trafegos = Traffic.objects.all()
    form = TrafficForm()

    return render(request, 'trafego.html', {'form': form, 'trafegos': trafegos})


@login_required(login_url='login')
def update_trafego(request, id):
    trafego = Traffic.objects.get(id=id)
    form = TrafficForm(request.POST or None, instance=trafego)

    if form.is_valid():
        form.save()

        try:
            messages.info(request, 'Dados alterados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('trafego')

    return render(request, 'trafego.html', {'trafego': trafego, 'form': form})


@login_required(login_url='login')
def delete_trafego(request, id):
    trafego = Traffic.objects.get(id=id)

    if request.method == 'GET':
        trafego.delete()

        try:
            messages.info(request, 'Dados deletados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('trafego')
    
    return render(request, 'trafego.html', {'trafego': trafego})


@login_required(login_url='login')
def export_excel_trafego(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Expenses" + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Veículo', 'Marca', 'Dt.saída', 'H.saída', 'Km.saída', 'Destino', 'Dt.chegada', 'H.chegada', 'km.chegada', 'Finalidade', 'Dif', 'Motorista', 'Solicitado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Traffic.objects.values_list('id', 'vehicle', 'mark_traffic', 'departure_date', 'departure_time', 'km_of_exit', 'destiny', 'arrival_date', 'arrival_time', 'arrival_kml', 'service_purpose', 'difference', 'drivers_name', 'asked_by')

    for row in rows:
        row_num += 1

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

"""================================================= VEÍCULO ====================================================="""

@login_required(login_url='login')
def cadastro_veiculo(request):
    form = VehicleForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()

            try:
                messages.info(request, 'Dados cadastrados com sucesso!')
            except messages.error:
                messages.info(request, 'Ops, algo deu errado!')

            return redirect('cadastro_veiculo')
    
    veiculos = Vehicle.objects.all()
    form = VehicleForm()
        
    return render(request, 'veiculo.html', {'veiculos': veiculos, 'form': form})


@login_required(login_url='login')
def update_vehicle(request, id):
    veiculo = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST or None, instance=veiculo)

    if form.is_valid():
        form.save()

        try:
            messages.info(request, 'Dados alterados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')
        
        return redirect('cadastro_veiculo')

    return render(request, 'veiculo.html', {'veiculo': veiculo, 'form': form})


@login_required(login_url='login')
def delete_veiculo(request, id):
    veiculo = Vehicle.objects.get(id=id)
    
    if request.method == 'GET':
        veiculo.delete()

        try:
            messages.info(request, 'Dados deletados com sucesso!')
        except messages.error:
            messages.info(request, 'Ops, algo deu errado!')

        return redirect('cadastro_veiculo')

    
    return render(request, 'veiculo.html', {'veiculo': veiculo})


@login_required(login_url='login')
def export_excel_veiculo(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Expenses" + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id','Marca','Modelo', 'Cor', 'Placa', 'Data']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Vehicle.objects.values_list('id', 'brand','vehicle', 'color', 'plate', 'date_create')

    for row in rows:
        row_num += 1

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response

    