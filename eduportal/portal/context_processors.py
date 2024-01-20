from portal.models import ShowInfo


# Функция передающая в шаблон дополнительные данные
def get_portal_context(request):
    navigate = ShowInfo.objects.all()

    return {'navigate': navigate}