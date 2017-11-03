# -*- coding: utf-8 -*-

# Future imports
from __future__ import unicode_literals, absolute_import

# Django imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2017, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.0.3/LICENSE"
__version__ = "1.0.3"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


# TODO: Document role definitions.
ROLES = [
    'technical_admin',
    'manager',
    'reviewer',
]

ROLE_CHOICES = list(zip(ROLES, ROLES))


@python_2_unicode_compatible
class User(AbstractUser):
    """User object

    User object, as defined and customized for project implementation.

    TODO: Document common patterns for User customization.
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    role = models.CharField(_('Role'), max_length=30, choices=ROLE_CHOICES, default='reviewer')
    organization = models.CharField(_('Organization'), max_length=100, blank=True, null=True)

    class Meta(object):
        ordering = ('username',)

    def __str__(self):
        return self.get_full_name()

    @property
    def role_abbr(self):
        return ''.join([word[0].upper() for word in self.role.split('_  ')])

    @property
    def is_admin(self):
        return self.role == 'technical_admin'

    @property
    def is_manager(self):
        return self.role == 'manager'

    @property
    def is_reviewer(self):
        return self.role == 'reviewer'

    def can_view_document(self, document):
        return self.is_superuser or self.is_manager or self.taskqueue_set. \
            filter(documents=document).exists()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between
        or username
        """
        if self.name:
            return self.name
        if self.first_name and self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()
        return self.username