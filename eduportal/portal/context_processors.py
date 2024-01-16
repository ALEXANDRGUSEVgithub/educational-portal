from portal.models import ShowInfo


def get_portal_context(request):
    navigate = ShowInfo.objects.all()

    return {'navigate': navigate}