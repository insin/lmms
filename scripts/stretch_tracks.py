import sys

import lxml.etree as etree

def stretch_lmms_tracks(inputfile, outputfile=None, scale=4):
    if outputfile is None:
        outputfile = inputfile
    xml = open(inputfile).read()
    tree = etree.fromstring(xml)
    for note in tree.xpath('//note'):
        note.attrib['len'] = str(int(note.attrib['len']) * scale)
        note.attrib['pos'] = str(int(note.attrib['pos']) * scale)
    for time in tree.xpath('//time'):
        time.attrib['pos'] = str(int(time.attrib['pos']) * scale)
    open(outputfile, 'w').write(etree.tostring(tree))

if __name__ == '__main__':
   stretch_lmms_tracks(*sys.argv[1:])
