# coding:utf-8
from django.conf.urls import patterns, include, url
from vmmanager.views import *

urlpatterns = patterns('',
                       url(r'^list/$', VM_list, name='VM_list'),
                       url(r'^apply/$', apply_machine, name='apply_machine'),
                       url(r'^resource/$', resource_view, name='resource_view'),
                       url(r'^saving_resource/$', saving_resource_view,
                           name='saving_resource_view'),
                       url(r'^ajax_show_apply_machinedetail',
                           show_apply_machinedetail, name='show_apply_machinedetail'),
                       url(r'^ajax_confirm_machine_detail/$', modify_machine_detail,
                           name='modify_machine_detail'),
                       url(r'^ajax_agree_apply/$', agree_apply, name='agree_apply'),
                       url(r'^ajax_delete_apply/$', delete_apply, name='delete_apply'),
                       url(r'^ajax_submit_saving_resource/$',
                           submit_saving_resource, name='submit_saving_resource'),
                       url(r'^set_vm/$',set_vm,name='set_vm'),
                       url(r'^ajax_get_agree_form/$',ajax_get_agree_form,name='ajax_get_agree_form'),
                       url(r'^ajax_get_cluster/$',ajax_get_cluster,name='ajax_get_cluster'),
                       url(r'^ajax_select_template/$',ajax_select_template,name='ajax_select_template'),
                       url(r'^ajax_get_resource/$',ajax_get_resource,name='ajax_get_resource'),
                       url(r'^ajax_get_process/$',ajax_get_process,name='ajax_get_process'),
                       url(r'^ajax_get_storage/$',ajax_get_storage,name='ajax_get_storage'),
                       url(r'^ajax_select_IP/$',ajax_select_IP,name='ajax_select_IP'),
                       url(r'^get_sheetfield/$', get_sheetfield, name='get_sheetfield'),
                       url(r'^get_env/$', get_env, name='get_env'),
                       url(r'^ajax_add_env/$',ajax_add_env,name='ajax_add_env'),
                       url(r'^ajax_add_vc/$',ajax_add_vc,name='ajax_add_vc'),
                       url(r'^ajax_modify_vc/$',ajax_modify_vc,name='ajax_modify_vc'),
                       url(r'^ajax_sync_vc/$', ajax_sync_vc, name='ajax_sync_vc'),
                       url(r'^ajax_delete_vc/$', ajax_delete_vc, name='ajax_delete_vc'),
                       url(r'^ajax_add_ip/$',ajax_add_ip,name='ajax_add_ip'),
                       url(r'^ajax_initial_network/$',ajax_initial_network,name='ajax_initial_network'),
                       url(r'^get_templates/$', get_templates, name='get_templates'),
                       url(r'^ajax_delete_template/$', ajax_delete_template, name='ajax_delete_template'),
                       url(r'^ajax_add_template/$', ajax_add_template, name='ajax_add_template'),
                       url(r'^ajax_update_env/$',ajax_update_env,name='ajax_update_env'),
                       url(r'^ajax_delete_env/$',ajax_delete_env,name='ajax_delete_env'),
                       url(r'^ajax_get_os_types/$', ajax_get_os_types, name='ajax_get_os_types'),
                       url(r'^ajax_get_os_version/$', ajax_get_os_version, name='ajax_get_os_version'),
                       url(r'^add_os_version/$', add_os_version, name='add_os_version'),
                       url(r'^del_os_version/$', del_os_version, name='del_os_version'),
                       url(r'^generate_machine/$',generate_machine,name='generate_machine'),
                       url(r'^modify_saving_detail/$',modify_saving_detail,name='modify_saving_detail'),
                       url(r'^show_approv_machinedetail/$',show_approv_machinedetail,name='show_approv_machinedetail'),
                       )
