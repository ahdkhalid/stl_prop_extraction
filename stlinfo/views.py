from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import random

from .models import StlInfo
from .forms import StlInfoFrom #, StlInfoUpdateFrom #, UploadFileForm

from .lib.stl_extraction import StlPropExtraction

def update_stl_obj():
    '''
    # As far our stl processing tool (numpy-stl) doesn't accept InMemoryUploadedFile
    # as input, we need to save the object first (done in create_view), then, get 
    # the file-system-stored file and process it. 
    # For that, since newly saved object will have the latest id, we find it that way
    '''
    stl_obj     = StlInfo.objects.latest('id') # get the last obj (newly uploaded one)
    stl_file    = stl_obj.stl_file.path
    mesh        = StlPropExtraction(stl_file) # mesh object
    stl_prop    = mesh.get_stl_properties()   # getting properties - dict

    stl_obj.volume      = stl_prop['volume']
    stl_obj.length      = stl_prop['length']
    stl_obj.width       = stl_prop['width']
    stl_obj.height      = stl_prop['height']
    stl_obj.diameter    = stl_prop['diameter']
    stl_obj.area        = stl_prop['area']
    stl_obj_id          = stl_obj.id
    stl_obj.save()

    return stl_obj_id # passing it to detail view

def stlinfo_create_view(request, *args, **kwargs):
    '''Home page view, which is rendering template and getting uploaded file and
    create the stl object and save to db.

    Args:
        request ([object]): http request - GET/ POST

    Returns:
        [object]: rendering template / redirect to stl/id
    '''
    if request.method == 'POST':
        form = StlInfoFrom(request.POST, request.FILES)
        if form.is_valid():
            uploaded_stl_file = request.FILES['stl_file']
            instance = StlInfo(
                name        = uploaded_stl_file.name,
                stl_file    = uploaded_stl_file,
                )
            instance.save()
            obj_id = update_stl_obj()
            return HttpResponseRedirect('stl/' + str(obj_id))
    else:
        form = StlInfoFrom()
    return render(request, 'pages/home.html', {'form': form})

def stlinfo_detail_view(request,stl_id, *args, **kwarg):
    data = {
        'id': stl_id,
    }
    try:
        obj             = StlInfo.objects.get(id= stl_id)
        data['name']    = obj.name
        data['stl_file']= obj.stl_file.url
        data['volume']  = obj.volume
        data['area']    = obj.area
        data['length']  = obj.length
        data['width']   = obj.width
        data['height']  = obj.height
        data['diameter']= obj.diameter
    except:
        data['message'] = 'Not Found'
        return render(request, 'pages/stl-detail.html', data)
    return render(request, 'pages/stl-detail.html', data)