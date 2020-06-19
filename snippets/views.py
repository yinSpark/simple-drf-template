# from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import renderers
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework import generics
from rest_framework import permissions
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

# 使用 ViewSets 把 SnippetList、 SnippetDetail和 SnippetHighlight 重构为 SnippetViewSet
# ModelViewSet 提供完整读写操作
# 具有 'list'、'create'、'retrieve'、'update'、'destory' 动作
# 另外添加 'highlight' 动作
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# 使用 ViewSets 把 UserList 和 UserDetail 重构为 UserViewSet
# ReadOnlyModelViewSet 这个类提供“只读”操作，具有 'list' 和 'detail' 动作
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# DefaultRouter 会自动创建 API 根视图，因此此视图注释
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format),
#     })