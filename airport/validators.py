from django.core.exceptions import ValidationError


def fields_cant_be_same(a, b):
    if a == b:
        raise ValidationError(f"{a.name} and {b.name} cannot be the same.")
