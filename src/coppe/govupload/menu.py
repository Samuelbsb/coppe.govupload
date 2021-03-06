# -*- coding:utf-8 -*-
from coppe.govupload import _
from coppe.govupload.config import ICON
from plone.app.contentmenu.menu import FactoriesMenu as BaseMenu
from plone.app.contentmenu.menu import FactoriesSubMenuItem as BaseMenuItem
from plone.app.contentmenu.interfaces import IFactoriesSubMenuItem
from zope.interface import implements
from zope.component import getMultiAdapter


class FactoriesSubMenuItem(BaseMenuItem):
    implements(IFactoriesSubMenuItem)

    submenuId = 'coppe_upload_contentmenu_factory'


class FactoriesMenu(BaseMenu):
    """ Customized version of FactoriesMenu
    """

    def getMenuItems(self, context, request):
        # menuitems is a list of tal-friendly dictionaries
        
        menuitems = super(FactoriesMenu, self).getMenuItems(context, request)
        allowed_content_types = ['ArquivoBiblioteca', 'Image']

        context_state = getMultiAdapter((context, request), name='plone_context_state')

        obj = context_state.folder()

        if set([x.id for x in obj.allowedContentTypes()]) & set(allowed_content_types):
            url = obj.absolute_url()
            new_menu = {'extra': {'separator': None,
                                  'id': 'multiple-files',
                                  'class': 'contenttype-multiple-files'},
                        'submenu': None,
                        'description': _(u'A form to upload multiple files.'),
                        'title': _(u'Multiple Files'),
                        'action': '%s/@@coppe_media_uploader' % url,
                        'selected': False,
                        'id': 'Multiple Files',
                        'icon': ICON}
            menuitems.insert(-1, new_menu)

        return menuitems
