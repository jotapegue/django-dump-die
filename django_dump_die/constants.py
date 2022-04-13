# Constants for dump die

import datetime
import types

from decimal import Decimal

from django.conf import settings
from django.forms.boundfield import BoundField
from django.utils import timezone


# Simple types that do not need to be recursively inspected.
SIMPLE_TYPES = [
    bool,
    BoundField,
    bytes,
    Decimal,
    float,
    int,
    types.ModuleType,
    str,
]


# Intermediate types, that need some level of recursion and some level of "simple type" handling.
INTERMEDIATE_TYPES = [
    datetime.datetime,
    datetime.date,
    datetime.time,
    timezone.timezone,
    # pytz.BaseTzInfo,  # pytz timezone object. Has to be handled separately. Noted here just as a reminder.
]


# List of additional simple types defined as strings that do not need to be recursively inspected.
ADDITIONAL_SIMPLE_TYPES = getattr(settings, 'DJANGO_DD_ADDITIONAL_SIMPLE_TYPES', [])
# List of additional intermediate types defined as strings that do not need to be recursively inspected.
ADDITIONAL_INTERMEDIATE_TYPES = getattr(settings, 'DJANGO_DD_ADDITIONAL_INTERMEDIATE_TYPES', [])
# Max recursion depth to go while processing the dumped variable.
MAX_RECURSION_DEPTH = getattr(settings, 'DJANGO_DD_MAX_RECURSION_DEPTH', 20)
# Max number of iterables to recursively process before just printing the unique
# instead of recursing further. EX: if set to 20, a list of 30 will recursively
# inspect and print out 20 items and then simply print the unique for the last 10.
MAX_ITERABLE_LENGTH = getattr(settings, 'DJANGO_DD_MAX_ITERABLE_LENGTH', 20)
# Whether attributes should be included in the output.
INCLUDE_ATTRIBUTES = getattr(settings, 'DJANGO_DD_INCLUDE_ATTRIBUTES', True)
# Whether functions should be included in the output.
INCLUDE_FUNCTIONS = getattr(settings, 'DJANGO_DD_INCLUDE_FUNCTIONS', False)
# Whether function doc output should try to fit on one line, or output with original newlines.
MULTILINE_FUNCTION_DOCS = getattr(settings, 'DJANGO_DD_MULTILINE_FUNCTION_DOCS', False)
# Whether objects attribute types (Attribute, Function) should start expanded for viewing.
ATTR_TYPES_START_EXPANDED = getattr(settings, 'DJANGO_DD_ATTRIBUTE_TYPES_START_EXPANDED', False)
# Whether the attributes for an object should start expanded for viewing.
ATTRIBUTES_START_EXPANDED = getattr(settings, 'DJANGO_DD_ATTRIBUTES_START_EXPANDED', True)
# Whether the functions for an object should start expanded for viewing.
FUNCTIONS_START_EXPANDED = getattr(settings, 'DJANGO_DD_FUNCTIONS_START_EXPANDED', False)
# Whether the output should include private attributes and functions.
INCLUDE_PRIVATE_METHODS = getattr(settings, 'DJANGO_DD_INCLUDE_PRIVATE_MEMBERS', False)
# Whether the output should include magic methods.
INCLUDE_MAGIC_METHODS = getattr(settings, 'DJANGO_DD_INCLUDE_MAGIC_METHODS', False)