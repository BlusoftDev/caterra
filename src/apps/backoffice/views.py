from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Slider, Video, MonthOffer, Post
from .forms import SliderForm, VideoForm, MonthOfferForm, PostForm
from apps.users.decorators import allowed_users
from apps.users.models import User, Admin, Editor, Seller
from apps.users.forms import CustomUserChangeForm, UserCreationForm, UserForm
from apps.ecommerce.models import Order


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class DasboardView(TemplateView):
    template_name = "backoffice/dashboard.html"


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class SliderListView(ListView):
    template_name = "backoffice/sliders/list.html"
    model = Slider

    def get_context_data(self, **kwargs):
        context = super(SliderListView, self).get_context_data(**kwargs)
        context["title"] = "Sliders"
        context["subtitle"] = "Sliders"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class SliderCreateView(CreateView):
    template_name = "backoffice/sliders/create.html"
    model = Slider
    form_class = SliderForm
    success_url = reverse_lazy("backoffice:sliders")

    def get_context_data(self, **kwargs):
        context = super(SliderCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo Slider"
        context["subtitle"] = "Nuevo Slider"

        return context

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class SliderUpdateView(UpdateView):
    template_name = "backoffice/sliders/update.html"
    form_class = SliderForm
    model = Slider
    success_url = reverse_lazy("backoffice:sliders")

    def get_context_data(self, **kwargs):
        context = super(SliderUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar Slider"
        context["subtitle"] = "Actualizar Slider"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class SliderDeleteView(DeleteView):
    template_name = "backoffice/sliders/slider_confirm_delete.html"
    model = Slider
    success_url = reverse_lazy("backoffice:sliders")


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class VideoUpdateView(UpdateView):
    template_name = "backoffice/video/update.html"
    form_class = VideoForm
    model = Video
    success_url = reverse_lazy("backoffice:video")

    def get_object(self):
        video = Video.objects.first()

        return video

    def get_context_data(self, **kwargs):
        context = super(VideoUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Video"
        context["subtitle"] = "Actualizar Video"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class MonthOfferListView(ListView):
    template_name = "backoffice/month-offers/list.html"
    model = MonthOffer

    def get_context_data(self, **kwargs):
        context = super(MonthOfferListView, self).get_context_data(**kwargs)
        context["title"] = "Ofertas del mes"
        context["subtitle"] = "Ofertas del mes"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class MonthOfferCreateView(CreateView):
    template_name = "backoffice/month-offers/create.html"
    model = MonthOffer
    form_class = MonthOfferForm
    success_url = reverse_lazy("backoffice:offers")

    def get_context_data(self, **kwargs):
        context = super(MonthOfferCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nueva oferta del mes"
        context["subtitle"] = "Nueva ofertas del mes"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class MonthOfferUpdateView(UpdateView):
    template_name = "backoffice/month-offers/update.html"
    model = MonthOffer
    form_class = MonthOfferForm
    success_url = reverse_lazy("backoffice:offers")

    def get_context_data(self, **kwargs):
        context = super(MonthOfferUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar oferta del mes"
        context["subtitle"] = "Actualizar ofertas del mes"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class MonthOfferDeleteView(DeleteView):
    template_name = "backoffice/month-offers/month-offer-confirm-delete.html"
    model = MonthOffer
    success_url = reverse_lazy("backoffice:offers")


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class PostListView(ListView):
    template_name = "backoffice/posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["title"] = "Blog"
        context["subtitle"] = "Blog"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class PostCreateView(CreateView):
    template_name = "backoffice/posts/create.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("backoffice:posts")

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo post"
        context["subtitle"] = "Nuevo post"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class PostUpdateView(UpdateView):
    template_name = "backoffice/posts/update.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("backoffice:posts")

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar post"
        context["subtitle"] = "Actualizar post"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class PostDeleteView(DeleteView):
    template_name = "backoffice/posts/post-confirm-delete.html"
    model = Post
    success_url = reverse_lazy("backoffice:posts")


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class EditorUserListView(ListView):
    model = Editor
    template_name = "backoffice/users/list.html"

    def get_context_data(self, **kwargs):
        context = super(EditorUserListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios editores"
        context["subtitle"] = "Usuarios editores"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class AdminListView(ListView):
    template_name = "backoffice/users/list.html"
    model = Admin
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios administradores"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class SellerListView(ListView):
    template_name = "backoffice/users/list.html"
    model = Seller
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        return super(SellerListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SellerListView, self).get_context_data(**kwargs)
        context["title"] = "Usuarios Vendedores"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class UserDetailView(DetailView):
    template_name = "backoffice/users/details.html"
    model = User
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        return super(UserDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["title"] = "Detalles de usuario"

        return context


class UserCreateView(CreateView):
    template_name = "backoffice/users/create.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("backoffice:users_editors")

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nuevo usuario"
        context["subtitle"] = "Nuevo usuario"

        return context


class UserUpdateView(UpdateView):
    template_name = "backoffice/users/update.html"
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("backoffice:users_editors")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Actualizar usuario"
        context["subtitle"] = "Actualizar usuario"

        return context


class UserDeleteView(DeleteView):
    template_name = "backoffice/users/user-confirm-delete.html"
    model = User
    success_url = reverse_lazy("backoffice:users_editors")


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class OrderListView(ListView):
    template_name = "backoffice/orders/list.html"
    model = Order
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context["subtitle"] = "Pedidos"

        return context


@method_decorator(allowed_users(allowed_roles=["ADMIN", "SELLER", "EDITOR"]), name="dispatch")
class OrderDetailView(DetailView):
    template_name = "backoffice/orders/detail.html"
    model = Order
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context["subtitle"] = "Pedidos"

        return context


class OrderDeleteView(DeleteView):
    template_name = "backoffice/orders/order-delete-confirmation.html"
    model = Order
    success_url = reverse_lazy("backoffice:orders_list")
