# coding=utf-8
from django.shortcuts import HttpResponse, get_object_or_404
import models


def must_be_org_user(function):
    def wrapper(request, *args, **kwargs):
        managed_libraries = []
        for user_library in models.UserLibrary.objects.filter(user=request.user):
            if user_library.is_active:
                managed_libraries.append(user_library.library)
                if user_library.descendants_rights:
                    managed_libraries += user_library.library.get_descendants()

        if not request.user.is_superuser and not managed_libraries:
            return HttpResponse(u'Вы не являетесь сотрудиком организации', status=403)

        nkwargs = dict({
            'managed_libraries': managed_libraries,
        }, **kwargs)
        return function(request, **nkwargs)

    return wrapper

