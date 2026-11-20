from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Animal, Enclosure, Keeper, VetCard, FeedingSchedule
from .forms import AnimalForm, EnclosureForm, KeeperForm, VetCardForm, FeedingScheduleForm


def index_view(request):
    context = {
        'animals_count': Animal.objects.count(),
        'enclosures_count': Enclosure.objects.count(),
        'keepers_count': Keeper.objects.count(),
        'vetcards_count': VetCard.objects.count(),
        'feedings_count': FeedingSchedule.objects.count(),
    }
    return render(request, 'index.html', context)


# ================= 1. ЖИВОТНЫЕ (CRUD) =================
class AnimalListView(ListView):
    model = Animal
    template_name = 'zoo/animal_list.html'
    context_object_name = 'animals'


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'zoo/animal_detail.html'
    context_object_name = 'animal'


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'zoo/animal_form.html'
    success_url = reverse_lazy('animal_list')


class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'zoo/animal_form.html'
    success_url = reverse_lazy('animal_list')


class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'zoo/animal_confirm_delete.html'
    context_object_name = 'animal'
    success_url = reverse_lazy('animal_list')


# ================= 2. ВОЛЬЕРЫ (CRUD) =================
class EnclosureListView(ListView):
    model = Enclosure
    template_name = 'zoo/enclosure_list.html'
    context_object_name = 'enclosures'


class EnclosureDetailView(DetailView):
    model = Enclosure
    template_name = 'zoo/enclosure_detail.html'
    context_object_name = 'enclosure'


class EnclosureCreateView(CreateView):
    model = Enclosure
    form_class = EnclosureForm
    template_name = 'zoo/enclosure_form.html'
    success_url = reverse_lazy('enclosure_list')


class EnclosureUpdateView(UpdateView):
    model = Enclosure
    form_class = EnclosureForm
    template_name = 'zoo/enclosure_form.html'
    success_url = reverse_lazy('enclosure_list')


class EnclosureDeleteView(DeleteView):
    model = Enclosure
    template_name = 'zoo/enclosure_confirm_delete.html'
    context_object_name = 'enclosure'
    success_url = reverse_lazy('enclosure_list')


# ================= 3. СОТРУДНИКИ (CRUD) =================
class KeeperListView(ListView):
    model = Keeper
    template_name = 'zoo/keeper_list.html'
    context_object_name = 'keepers'


class KeeperDetailView(DetailView):
    model = Keeper
    template_name = 'zoo/keeper_detail.html'
    context_object_name = 'keeper'


class KeeperCreateView(CreateView):
    model = Keeper
    form_class = KeeperForm
    template_name = 'zoo/keeper_form.html'
    success_url = reverse_lazy('keeper_list')


class KeeperUpdateView(UpdateView):
    model = Keeper
    form_class = KeeperForm
    template_name = 'zoo/keeper_form.html'
    success_url = reverse_lazy('keeper_list')


class KeeperDeleteView(DeleteView):
    model = Keeper
    template_name = 'zoo/keeper_confirm_delete.html'
    context_object_name = 'keeper'
    success_url = reverse_lazy('keeper_list')


# ================= 4. ВЕТЕРИНАРНЫЕ КАРТЫ (CRUD) =================
class VetCardListView(ListView):
    model = VetCard
    template_name = 'zoo/vetcard_list.html'
    context_object_name = 'vetcards'


class VetCardDetailView(DetailView):
    model = VetCard
    template_name = 'zoo/vetcard_detail.html'
    context_object_name = 'vetcard'


class VetCardCreateView(CreateView):
    model = VetCard
    form_class = VetCardForm
    template_name = 'zoo/vetcard_form.html'
    success_url = reverse_lazy('vetcard_list')


class VetCardUpdateView(UpdateView):
    model = VetCard
    form_class = VetCardForm
    template_name = 'zoo/vetcard_form.html'
    success_url = reverse_lazy('vetcard_list')


class VetCardDeleteView(DeleteView):
    model = VetCard
    template_name = 'zoo/vetcard_confirm_delete.html'
    context_object_name = 'vetcard'
    success_url = reverse_lazy('vetcard_list')


# ================= 5. РАСПИСАНИЕ КОРМЛЕНИЙ (CRUD) =================
class FeedingScheduleListView(ListView):
    model = FeedingSchedule
    template_name = 'zoo/feeding_list.html'
    context_object_name = 'feedings'


class FeedingScheduleDetailView(DetailView):
    model = FeedingSchedule
    template_name = 'zoo/feeding_detail.html'
    context_object_name = 'feeding'


class FeedingScheduleCreateView(CreateView):
    model = FeedingSchedule
    form_class = FeedingScheduleForm
    template_name = 'zoo/feeding_form.html'
    success_url = reverse_lazy('feeding_list')


class FeedingScheduleUpdateView(UpdateView):
    model = FeedingSchedule
    form_class = FeedingScheduleForm
    template_name = 'zoo/feeding_form.html'
    success_url = reverse_lazy('feeding_list')


class FeedingScheduleDeleteView(DeleteView):
    model = FeedingSchedule
    template_name = 'zoo/feeding_confirm_delete.html'
    context_object_name = 'feeding'
    success_url = reverse_lazy('feeding_list')
