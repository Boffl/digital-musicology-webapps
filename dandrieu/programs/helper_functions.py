import music21 as m21

class ParseBassError(Exception):
    def __str__(self):
        return 'Error wile trying to parse the bassline input'

    def __repr__(self):
        return str(type(self))



def parse_user_input(timeSig_str, keySig_str, bass_line_str):

    keySig = m21.key.Key(keySig_str.split(' ')[0], keySig_str.split(' ')[1])
    timeSig = m21.meter.TimeSignature(timeSig_str)
    notes = m21.converter.parse(f'tinynotation: {timeSig_str} {bass_line_str}').recurse().notes

    if len(notes) == 0:
        raise ParseBassError

    return timeSig, keySig, notes

if __name__ == '__main__':
    result = parse_user_input('3/4', 'C Major', 'asdf')
    print(result)