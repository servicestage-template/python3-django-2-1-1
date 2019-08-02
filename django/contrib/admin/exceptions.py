from django.core.exceptions import SuspiciousOperation


class DisallowedModelAdminLookup(SuspiciousOperation):
    """Invalid filter was passed to admin views via URL querystring"""
    pass


class DisallowedModelAdminToField(SuspiciousOperation):
    """Invalid to_field was passed to admin views via URL query string"""
    pass
