# coding: utf-8

from __future__ import unicode_literals

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required

from photo.models import Photo
from photo.forms import PhotoEditForm


def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    return render(
        request,
        'photo.html',
        {
            'photo': photo,
        }
    )


@login_required
def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save(commit=False)
            new_photo.user = request.user
            new_photo.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'new_photo.html',
        {
            'form': edit_form,
        }
    )
