from django.http import HttpResponse
from django.template import loader


def index(request):
    # TODO: link this template, make a proper startpage
    # something is not right here...
    # template = loader.get_template('index.html')
    result = '''
    <h1>Startpage</h1>
    <form action='dandrieu'>
        <button onClick='submit'>Dandrieu Harmonization</button>
    </form>'''

    return HttpResponse(result)