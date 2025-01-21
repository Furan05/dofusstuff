from django.shortcuts import render
from django.views.generic import CreateView
from .models import BuildRequest, Character
from .forms import BuildRequestForm

class BuildRequestView(CreateView):
    model = BuildRequest
    form_class = BuildRequestForm
    template_name = 'optimizer/index.html'
    success_url = '/'

    def form_valid(self, form):
        # Créer d'abord le personnage
        character = Character.objects.create(
            character_class=form.cleaned_data['character_class'],
            level=form.cleaned_data['level']
        )

        # Créer la demande de build
        build_request = BuildRequest.objects.create(character=character)

        # Ajouter les stats
        build_request.primary_stats.set(form.cleaned_data['primary_stats'])
        build_request.secondary_stats.set(form.cleaned_data['secondary_stats'])

        return super().form_valid(form)
