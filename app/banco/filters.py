import django_filters
from banco.models import Agencia

class FiltroAgencia(django_filters.FilterSet):
    id_banco = django_filters.CharFilter(lookup_expr='icontains')
    agencia = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Agencia
        fields=['id_banco','agencia']