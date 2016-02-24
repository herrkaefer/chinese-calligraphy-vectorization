#-*- coding: UTF-8 -*-
# Copyright LIU Yang <gloolar@gmail.com>

"""
Chinese Calligraphy Vectorization (CCV) Project

written by: LIU Yang, gloolar@gmail.com
first version: July 2009
modification: July 2014
"""

import os.path
from xml.dom import minidom


xmlns = 'http://www.w3.org/2000/svg'
xmlversion = 1.1
desc = 'created by ccv'


def __get_xylist(d):
    (xlist, ylist) = ([], [])

    # if d[0]=='m': d[0]='M'
    # d = d.upper()
    # print d

    # M
    s = d.split('M ')
    # print s
    for a in s[1:]:
        b = ','.join(a.split()).split(',')
        xlist.append(float(b[0]))
        ylist.append(float(b[1]))

    # m
    # s = d.split('m ')
    # for a in s[1:]:
        # b = ','.join(a.split()).split(',')
        # xlist.append(float(b[0]))
        # ylist.append(float(b[1]))

    # C
    s = d.split('C ')
    for a in s[1:]:
        b = ','.join(a.split()).split(',')
        xlist.append(float(b[4]))
        ylist.append(float(b[5]))

    # c
    # s = d.split('c ')
    # for a in s[1:]:
        # b = ','.join(a.split()).split(',')
        # xlist.append(float(b[4]))
        # ylist.append(float(b[5]))

    # L
    s = d.split('L ')
    for a in s[1:]:
        b = ','.join(a.split()).split(',')
        xlist.append(float(b[0]))
        ylist.append(float(b[1]))


    return (xlist, ylist)


def save_copybook(doc, filename):

    fname = filename.split('.svg')[0]+'.svg'
    fout = open(fname,'w')
    doc.writexml(fout,indent='\n',encoding='utf-8')
    fout.close()


def purify(dirname):

    svgfiles = [f for f in os.listdir(dirname) if f.endswith('.svg')]

    # make directory 'purified' under dirname
    resultdir = os.path.join(dirname,'purified')
    try:
        os.mkdir(resultdir)
    except WindowsError:
        print 'folder purified exists.'
        pass

    for f in svgfiles:
        print f
        doc = minidom.Document()

        # svg
        SVG = doc.createElement('svg')
        SVG.setAttribute('width', str(chrwidth))
        SVG.setAttribute('height', str(chrwidth))
        SVG.setAttribute('xmlns', xmlns)
        SVG.setAttribute('version', str(version))
        doc.appendChild(SVG)

        # title
#       TITlE = doc.createElement('title')
#       TITlE.appendChild(doc.createTextNode(f.encode('utf_8')))
#       SVG.appendChild(TITlE)

        # desc
#       DESC = doc.createElement('desc')
#       DESC.appendChild(doc.createTextNode(desc))
#       SVG.appendChild(DESC)

        # path
        pathinfile = minidom.parse(os.path.join(dirname,f)).getElementsByTagName('path')
        for p in pathinfile:
            PATH = doc.createElement('path')
            PATH.setAttribute('d',p.attributes['d'].value)
            SVG.appendChild(PATH)

        svg_savefile(doc, os.path.join(resultdir,f))


def typeset(dirname, title='demo', nrow=7, direction='v', chrratio=0.8, grid='on', canvaswidth=1024):

    if os.path.isdir(dirname):
        svgfiles = [f for f in os.listdir(dirname) if f.endswith('.svg')]
        if len(svgfiles) == 0:
            print 'No svg file in folder %s' % dirname
            return
    else:
        print '%s is not a correct directory.' % dirname
        return

    svgfiles.sort()
    num = len(svgfiles)
    ncol = (num-1)/nrow + 1
    if direction.lower() == 'v':
        # canvaswidth = chrwidth*ncol
        chrwidth = canvaswidth / ncol
        canvasheight = chrwidth * nrow

    elif direction.lower() == 'h':
        # canvaswidth = chrwidth*nrow
        chrwidth = canvaswidth / nrow
        canvasheight = chrwidth * ncol
    else:
        print 'direction error.'
        return None

    doc = minidom.Document()

    # svg
    SVG = doc.createElement('svg')
    SVG.setAttribute('width', str(canvaswidth))
    SVG.setAttribute('height', str(canvasheight))
    SVG.setAttribute('xmlns', xmlns)
    SVG.setAttribute('version', str(xmlversion))
    doc.appendChild(SVG)

    # title
    TITlE = doc.createElement('title')
    TITlE.appendChild(doc.createTextNode(title))
    SVG.appendChild(TITlE)

    # desc
    DESC = doc.createElement('desc')
    DESC.appendChild(doc.createTextNode(desc))
    SVG.appendChild(DESC)

    # get path from character file and add translate & scale attribute
    for i in xrange(len(svgfiles)):
        filename = svgfiles[i]
        print(filename),

        nr = i % nrow
        nc = i / nrow

        if direction.lower() == 'v':
            x = chrwidth * (ncol - nc - 1)
            y = chrwidth * nr
        elif direction.lower() == 'h':
            x = chrwidth * nr
            y = chrwidth * nc

        # grid
        if grid == 'on':
            BOARDER = doc.createElement('rect')
            BOARDER.setAttribute('x', str(x))
            BOARDER.setAttribute('y', str(y))
            BOARDER.setAttribute('width', str(chrwidth))
            BOARDER.setAttribute('height', str(chrwidth))
            BOARDER.setAttribute('fill', 'white')
            BOARDER.setAttribute('stroke', 'red')
            BOARDER.setAttribute('stroke-width', str(chrwidth/500+2))
            SVG.appendChild(BOARDER)

            LINE = doc.createElement('line')
            LINE.setAttribute('x1', str(x))
            LINE.setAttribute('y1', str(y))
            LINE.setAttribute('x2', str(x+chrwidth))
            LINE.setAttribute('y2', str(y+chrwidth))
            LINE.setAttribute('stroke', 'red')
            LINE.setAttribute('stroke-width', str((chrwidth/500+2)/2))
            SVG.appendChild(LINE)

            LINE = doc.createElement('line')
            LINE.setAttribute('x1', str(x+chrwidth))
            LINE.setAttribute('y1', str(y))
            LINE.setAttribute('x2', str(x))
            LINE.setAttribute('y2', str(y+chrwidth))
            LINE.setAttribute('stroke', 'red')
            LINE.setAttribute('stroke-width', str((chrwidth/400+2)/2))
            SVG.appendChild(LINE)

            LINE = doc.createElement('line')
            LINE.setAttribute('x1', str(x))
            LINE.setAttribute('y1', str(y+chrwidth/2))
            LINE.setAttribute('x2', str(x+chrwidth))
            LINE.setAttribute('y2', str(y+chrwidth/2))
            LINE.setAttribute('stroke', 'red')
            LINE.setAttribute('stroke-width', str((chrwidth/400+2)/2))
            SVG.appendChild(LINE)

            LINE = doc.createElement('line')
            LINE.setAttribute('x1', str(x+chrwidth/2))
            LINE.setAttribute('y1', str(y))
            LINE.setAttribute('x2', str(x+chrwidth/2))
            LINE.setAttribute('y2', str(y+chrwidth))
            LINE.setAttribute('stroke', 'red')
            LINE.setAttribute('stroke-width', str((chrwidth/400+2)/2))
            SVG.appendChild(LINE)

        # transform
        G = doc.createElement('g')

        # path
        pathinfile = minidom.parse(os.path.join(dirname,filename)).getElementsByTagName('path')
        (xlist, ylist) = ([], [])
        for p in pathinfile:
            PATH = doc.createElement('path')
            d = p.attributes['d'].value

            PATH.setAttribute('d', d)
        #   PATH.setAttribute('style',"fill:#ffffff;fill-opacity:0;stroke:#000000;stroke-opacity:1;opacity:1;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none")
            G.appendChild(PATH)
            (xlistd, ylistd) = __get_xylist(d)
            xlist.extend(xlistd)
            ylist.extend(ylistd)

        (xmin, xmax, ymin, ymax) = (min(xlist), max(xlist), min(ylist), max(ylist))
        scale = chrwidth * chrratio / max(xmax-xmin, ymax-ymin)

        G.setAttribute('transform', 'translate(%f,%f) scale(%f)' % (x+chrwidth/2-(xmax+xmin)/2*scale, y+chrwidth/2-(ymax+ymin)/2*scale, scale))
        SVG.appendChild(G)

    return doc


def produce_copybook(character_dir='calligraphy/lantingxu/svg', title='demo', rows=7, direction='v', character_ratio=0.8, grid='on', canvas_width=300):

    #   purify('D:\\MyWork\\InProgress\\[Project]CCV\\SVG')
    doc = typeset(character_dir, title, rows, direction, character_ratio, grid, canvas_width)
    if doc is not None:
        save_copybook(doc, os.path.join(os.getcwd(), 'copybooks', title))


def test():

    produce_copybook( character_dir   = os.path.join(os.getcwd(), 'calligraphy', 'lantingxu', 'svg'),
                      title           = 'lantingxu-withgrid',
                      rows            = 8,
                      direction       = 'v',
                      character_ratio = 0.75,
                      grid            = 'on',
                      canvas_width    = 1366 )

    produce_copybook( character_dir   = os.path.join(os.getcwd(), 'calligraphy', 'lantingxu', 'svg'),
                      title           = 'lantingxu-nogrid',
                      rows            = 8,
                      direction       = 'v',
                      character_ratio = 0.75,
                      grid            = 'off',
                      canvas_width    = 1366 )


if __name__ == "__main__":

    test()


# Todo list:
#
# - computer and add scale attribute accordding to margin setting (percentage)
# - direction: horizontal/vertical
# -> UI (with pyQt) (parameter selection, display svg, etc.)
# -> touch board support
