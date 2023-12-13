from portal.utils import menu, navigate


def get_portal_context(request):
    return {'menu': menu,
            'navigate': navigate}