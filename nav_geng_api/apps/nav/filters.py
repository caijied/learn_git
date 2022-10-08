import django_filters

from coder.models import UserDefinedBlocklyBlock


class UserDefinedBlocklyBlockFilter(django_filters.FilterSet):
    solution = django_filters.CharFilter(field_name='solution__id')

    class Meta:
        model = UserDefinedBlocklyBlock
        fields = ['solution', ]
