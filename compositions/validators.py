def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mid', '.midi', '.mp3', '.mpeg', '.m4a', '.ogg', '.flac', '.x - flac', '.wav', '.x - wav', '.amr']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Not an audio file.')