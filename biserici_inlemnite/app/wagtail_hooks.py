from django.urls import resolve
from urllib.parse import urlparse
from wagtail.core import hooks
from wagtail.core.models import Page


# @hooks.register('construct_image_chooser_queryset')
# def show_images_for_specific_collections_on_page_editing(images, request):

#     # first - pull out the referrer for this current AJAX call
#     http_referrer = request.META.get('HTTP_REFERER', None) or '/'

#     # second - use django utils to find the matched view
#     match = resolve(urlparse(http_referrer)[2])
#     print('---')
#     print(match)
#     print(request.META)
#     print('---')
#     # if we are editing a page we can restrict the available images
#     if (match.app_name is 'wagtailadmin_pages') and (match.url_name is 'edit'):
#         page = Page.objects.get(pk=match.kwargs['page_id'])

#         # important: wrap in a try/except as this may not be implemented on all pages
#         image_collection_id = page.specific_class.get_image_collection()

#         # return filtered images
#         return images.filter(collection=image_collection_id)

#     return images


#     {'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http', 'wsgi.input': <_io.BufferedReader name=9>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'SERVER_SOFTWARE': 'Werkzeug/1.0.1', 'REQUEST_METHOD': 'GET', 'SCRIPT_NAME': '', 'PATH_INFO': '/cms/images/chooser/', 'QUERY_STRING': '', 'REQUEST_URI': '/cms/images/chooser/', 'RAW_URI': '/cms/images/chooser/', 'REMOTE_ADDR': '172.19.0.1', 'REMOTE_PORT': 56346, 'SERVER_NAME': '0.0.0.0', 'SERVER_PORT': '8000', 'SERVER_PROTOCOL': 'HTTP/1.1', 'HTTP_HOST': '0.0.0.0:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_ACCEPT': 'text/plain, */*; q=0.01', 'HTTP_DNT': '1', 'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36', 'HTTP_REFERER': 'http://0.0.0.0:8000/cms/pages/1152/edit/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_ACCEPT_LANGUAGE': 'en-GB,en-US;q=0.9,en;q=0.8,ro;q=0.7', 'HTTP_COOKIE': 'csrftoken=WRue5WGAlpAFaliEzSPUrN1ODmyoeSpP8A0OWVnt7mcQtIO7Aj2vK8uu1yDrrdiO; sessionid=rydwmswl87e0t229ytnp3n1dbas220us', 'werkzeug.request': <BaseRequest 'http://0.0.0.0:8000/cms/images/chooser/' [GET]>, 'CSRF_COOKIE': 'WRue5WGAlpAFaliEzSPUrN1ODmyoeSpP8A0OWVnt7mcQtIO7Aj2vK8uu1yDrrdiO'}