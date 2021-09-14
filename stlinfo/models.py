from django.db import models
from django.core.validators import FileExtensionValidator
# from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/media/stls/')

# def upload_file_path(filename):
#     return "/%Y/%m/%d/" + filename

class StlInfo(models.Model):
    name            = models.CharField(blank = True, max_length=100)
    # a basic file extension validation is put into action. File type validation is better
    stl_file        = models.FileField(upload_to='stls/', 
        validators= [FileExtensionValidator(allowed_extensions = ['stl'])])#, storage = fs)
    volume          = models.FloatField(blank = True, null = True)
    length          = models.FloatField(blank = True, null = True)
    width           = models.FloatField(blank = True, null = True)
    height          = models.FloatField(blank = True, null = True)
    diameter        = models.FloatField(blank = True, null = True)
    area            = models.FloatField(blank = True, null = True)

    def __str__(self):
        return f'{self.name}'
