from portal.utils import menu
from portal.models import ShowInfo


def get_portal_context(request):
    navigate = ShowInfo.objects.all()

    return {'menu': menu,
            'navigate': navigate}