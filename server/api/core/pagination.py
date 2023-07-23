from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultSetPagination(PageNumberPagination):
    """自定义分页"""
    page_size = 10
    page_query_param = 'page'
    max_page_size = 1000

    def get_paginated_response(self, data):
        """自定义返回信息"""
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'results': data
        })


class ArticleListPagination(PageNumberPagination):
    """自定义分页"""
    page_size = 10
    page_query_param = 'page'
    max_page_size = 1000

    def get_paginated_response(self, data):
        """自定义返回信息"""

        statistics = {}
        tags = {}
        statistics['tags'] = tags

        for article in data:
            for tag in article['tags']:
                if tag in tags:
                    tags[tag] += 1
                else:
                    tags[tag] = 1

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'statistics': statistics,
            'results': data
        })
