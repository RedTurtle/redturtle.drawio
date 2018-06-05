# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from redturtle.drawio import _
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant
from lxml import html


class ValidateIframe(Invalid):
    __doc__ = _(u"The html is invalid")


class IDrawioItem(model.Schema):

    """ Marker interface and Dexterity Python Schema for DrawioItem
    """

    embed_code = schema.Text(
        title=_(u'Embed code'),
        required=True
    )

    @invariant
    def validateIframe(data):
        embed = getattr(data, 'html_embed', None)
        if not embed:
            return
        root = html.fromstring(embed)
        defaultMessage = _(u"You inserted a wrong embed code.")
        if root.tag != 'iframe':
            raise ValidateIframe(defaultMessage)
        if not root.get('src').startswith('https://www.draw.io/'):
            raise ValidateIframe(defaultMessage)


@implementer(IDrawioItem)
class DrawioItem(Item):

    """
    """
