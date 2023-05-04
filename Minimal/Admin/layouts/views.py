from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LayoutsView(LoginRequiredMixin,TemplateView):
    pass

# Horizontal
layouts_horizontal_view = LayoutsView.as_view(template_name="layouts/layouts-horizontal.html")
# Detached
layouts_detached_view = LayoutsView.as_view(template_name="layouts/layouts-detached.html")
# Colomn
layouts_column_view = LayoutsView.as_view(template_name="layouts/layouts-two-column.html")
# Hovered
layouts_hovered_view = LayoutsView.as_view(template_name="layouts/layouts-vertical-hovered.html")
# Vertical
layouts_vertical_view =LayoutsView.as_view(template_name="layouts/layouts-vertical.html")

