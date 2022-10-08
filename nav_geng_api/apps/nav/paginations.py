from rest_framework import pagination


class CarPagination(pagination.PageNumberPagination):
    """
        车辆
    """

    page_size = 30
    page_size_query_param = 'page_size'


class VPMPagination(pagination.PageNumberPagination):
    """
        车队
    """

    page_size = 30
    page_size_query_param = 'page_size'


class NavigationTaskPagination(pagination.PageNumberPagination):
    """
        导航任务
    """

    page_size = 30
    page_size_query_param = 'page_size'
