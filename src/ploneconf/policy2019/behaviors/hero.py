# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IHeroText(Interface):
    pass


@provider(IFormFieldProvider)
class IHeroTextBehavior(model.Schema):

    hero_text = RichTextField(
        title=_(u'Hero text'),
        description=_(u'Used in hero slot in 2019 static website'),
        required=False,
    )
    form.widget('hero_text', RichTextFieldWidget)
    model.primary('hero_text')


@implementer(IHeroTextBehavior)
@adapter(IDexterityContent)
class HeroText(object):
    def __init__(self, context):
        self.context = context

    @property
    def hero_text(self):
        return self.context.hero_text

    @hero_text.setter
    def hero_text(self, value):
        self.context.hero_text = value


class WidgetView(WidgetsView):
    schema = IHeroText
