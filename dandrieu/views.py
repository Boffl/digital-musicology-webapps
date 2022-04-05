from django.http import HttpResponse
from django.template import loader
from dandrieu.programs.helper_functions import parse_user_input
from dandrieu.programs.Dandrieu_rules import dandrieu_octave_rule
from dandrieu.programs.Dandrieu_rules import realize_fb


def index(request):
    template = loader.get_template('dandrieu/index.html')
    return HttpResponse(template.render())


def harmonize(request):
    template = loader.get_template('dandrieu/harmonize.html')
    timeSig_str = request.GET['timeSig']
    keySig_str = request.GET['keySig']
    bass_line_str = request.GET['bass_line']

    timeSig, keySig, notes = parse_user_input(timeSig_str, keySig_str, bass_line_str)
    fbLine = dandrieu_octave_rule(notes, keySig, timeSig, seventh=True) # atm adding a seven everytime it can
    musicxml_str = realize_fb(fbLine)

    # stuff to return
    context = {
        'timeSig_str': timeSig_str,
        'keySig_str': keySig_str,
        'bass_line_str': bass_line_str,
        'musicxml_str': musicxml_str,
    }
    return HttpResponse(template.render(context))

