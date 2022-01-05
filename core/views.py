from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def index(request):
    return render(
        request=request,
        template_name='index.html',
        context={'data': 'Django LMS Kokkin'}
    )


class UpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    @classmethod
    def update_student(cls, request, pk):
        obj = get_object_or_404(cls.model, id=pk)

        if request.method == "GET":
            form = cls.form_class(instance=obj)
        elif request.method == "POST":
            form = cls.form_class(data=request.POST, instance=obj)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(cls.success_url))

        return render(
            request,
            cls.template_name,
            context={"form": form}
        )
