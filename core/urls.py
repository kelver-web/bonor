from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('veiculos/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('update-veiculos/<int:id>/', views.update_vehicle, name='update_vehicle'),
    path('delete-veiculo/<int:id>/', views.delete_veiculo, name='delete_veiculo'),
    path('export-veiculo/', views.export_excel_veiculo, name='export_excel_veiculo'),
    path('abastecimento/', views.abast, name='abast'),
    path('update-abastecimentos/<int:id>/', views.update_abast, name='update_abast'),
    path('delete-abastecimentos/<int:id>/', views.delete_abast, name='delete_abast'),
    path('export-abastecimento/', views.export_excel_abastecimento, name='export_excel_abastecimento'),
    path('fornecedor/', views.fornecedor, name='fornecedor'),
    path('update-fornecedor/<int:id>/', views.update_fornecedor, name='update_fornecedor'),
    path('delete-fornecedor/<int:id>/', views.delete_fornecedor, name='delete_fornecedor'),
    path('export-fornecedor/', views.export_excel_fornecedor, name='export_excel_fornecedor'),
    path('manutencao/', views.manutencao, name='manutencao'),
    path('update-manutencao/<int:id>/', views.update_manutencao, name='update_manutencao'),
    path('delete-manutencoes/<int:id>/', views.delete_manutencao, name='delete_manutencao'),
    path('export-manutencao/', views.export_excel_manutencao, name='export_excel_manutencao'),
    path('trafego/', views.trafego, name='trafego'),
    path('update-trafego/<int:id>/', views.update_trafego, name='update_trafego'),
    path('delete-trafego/<int:id>/', views.delete_trafego, name='delete_trafego'),
    path('export-trafego/', views.export_excel_trafego, name='export_excel_trafego')
]