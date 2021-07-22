#from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.contrib.auth.views import redirect_to_login
from propuestas.forms import CrearPropuestaForm



# class UserAccessMixin(PermissionRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if (not self.request.user.is_authenticated):
#             return redirect_to_login(self.request.get_full_path(),
#                                     self.get_login_url(), self.get_redirect_field_name())
#         if not self.has_permission():
#             return redirect('/home')
#         return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)



class CrearPropuestaView(UserAccessMixin, FormView):
    form_class = CrearPropuestaForm
    template_name = 'crearpropuesta.html'
    success_url = '/propuestacreada/'
    raise_exception = True
    permission_required = ('propuestas.add_propuesta')
