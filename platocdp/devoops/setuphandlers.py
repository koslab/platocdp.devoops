from collective.grok import gs
from platocdp.devoops import MessageFactory as _

@gs.importstep(
    name=u'platocdp.devoops', 
    title=_('platocdp.devoops import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('platocdp.devoops.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
