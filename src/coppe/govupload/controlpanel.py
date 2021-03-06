# -*- coding: utf-8 -*-

from plone.app.registry.browser import controlpanel

from coppe.govupload import _
from coppe.govupload.interfaces import IUploadSettings


class UploadSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IUploadSettings
    label = _(u"Upload Settings")
    description = _(u"Here you can modify the settings for coppe.govupload")

    def updateFields(self):
        super(UploadSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(UploadSettingsEditForm, self).updateWidgets()


class UploadSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = UploadSettingsEditForm
