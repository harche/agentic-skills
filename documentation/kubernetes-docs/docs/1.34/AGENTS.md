# Kubernetes Documentation Index

> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led
> reasoning for Kubernetes tasks. Read the referenced files rather
> than relying on training data which may be outdated.

## How to Use This Index

This is a compressed documentation map. Each entry lists topic
files using pipe-delimited format: `|section/subsection:{file1.md,file2.md}`.
Retrieve the specific file you need rather than reading everything.

Root: ./

## Documentation Map

### concepts

|concepts:{_print.md,architecture.md,cluster-administration.md,configuration.md,containers.md,extend-kubernetes.md,overview.md,policy.md,scheduling-eviction.md,security.md,services-networking.md,storage.md,windows.md,workloads.md}
|concepts/architecture:{_print.md,cgroups.md,cloud-controller.md,control-plane-node-communication.md,controller.md,garbage-collection.md,leases.md,mixed-version-proxy.md,nodes.md,self-healing.md}
|concepts/cluster-administration:{_print.md,addons.md,admission-webhooks-good-practices.md,certificates.md,compatibility-version.md,coordinated-leader-election.md,dra.md,flow-control.md,kube-state-metrics.md,logging.md,networking.md,node-autoscaling.md,node-shutdown.md,observability.md,proxies.md,swap-memory-management.md,system-logs.md,system-metrics.md,system-traces.md}
|concepts/configuration:{_print.md,configmap.md,liveness-readiness-startup-probes.md,manage-resources-containers.md,organize-cluster-access-kubeconfig.md,secret.md,windows-resource-management.md}
|concepts/containers:{_print.md,container-environment.md,container-lifecycle-hooks.md,cri.md,images.md,runtime-class.md}
|concepts/extend-kubernetes:{_print.md,api-extension.md,compute-storage-net.md,operator.md}
|concepts/extend-kubernetes/api-extension:{_print.md,apiserver-aggregation.md,custom-resources.md}
|concepts/extend-kubernetes/compute-storage-net:{_print.md,device-plugins.md,network-plugins.md}
|concepts/overview:{_print.md,components.md,kubernetes-api.md,working-with-objects.md}
|concepts/overview/working-with-objects:{_print.md,annotations.md,common-labels.md,field-selectors.md,finalizers.md,labels.md,names.md,namespaces.md,object-management.md,owners-dependents.md}
|concepts/policy:{_print.md,limit-range.md,node-resource-managers.md,pid-limiting.md,resource-quotas.md}
|concepts/scheduling-eviction:{_print.md,api-eviction.md,assign-pod-node.md,dynamic-resource-allocation.md,kube-scheduler.md,node-pressure-eviction.md,pod-overhead.md,pod-priority-preemption.md,pod-scheduling-readiness.md,resource-bin-packing.md,scheduler-perf-tuning.md,scheduling-framework.md,taint-and-toleration.md,topology-spread-constraints.md}
|concepts/security:{_print.md,api-server-bypass-risks.md,application-security-checklist.md,cloud-native-security.md,controlling-access.md,linux-kernel-security-constraints.md,linux-security.md,multi-tenancy.md,pod-security-admission.md,pod-security-policy.md,pod-security-standards.md,rbac-good-practices.md,secrets-good-practices.md,security-checklist.md,service-accounts.md,windows-security.md}
|concepts/security/hardening-guide:{authentication-mechanisms.md,scheduler.md}
|concepts/services-networking:{_print.md,cluster-ip-allocation.md,dns-pod-service.md,dual-stack.md,endpoint-slices.md,gateway.md,ingress-controllers.md,ingress.md,network-policies.md,service-traffic-policy.md,service.md,topology-aware-routing.md,windows-networking.md}
|concepts/storage:{_print.md,dynamic-provisioning.md,ephemeral-storage.md,ephemeral-volumes.md,persistent-volumes.md,projected-volumes.md,storage-capacity.md,storage-classes.md,storage-limits.md,volume-attributes-classes.md,volume-health-monitoring.md,volume-pvc-datasource.md,volume-snapshot-classes.md,volume-snapshots.md,volumes.md,windows-storage.md}
|concepts/windows:{_print.md,intro.md,user-guide.md}
|concepts/workloads:{_print.md,autoscaling.md,controllers.md,management.md,pods.md}
|concepts/workloads/autoscaling:{vertical-pod-autoscale.md}
|concepts/workloads/controllers:{_print.md,cron-jobs.md,daemonset.md,deployment.md,job.md,replicaset.md,replicationcontroller.md,statefulset.md,ttlafterfinished.md}
|concepts/workloads/pods:{_print.md,disruptions.md,downward-api.md,ephemeral-containers.md,init-containers.md,pod-hostname.md,pod-lifecycle.md,pod-qos.md,sidecar-containers.md,user-namespaces.md}
### contribute

|contribute:{_print.md,advanced.md,analytics.md,blog.md,docs.md,generate-ref-docs.md,localization.md,new-content.md,participate.md,review.md,style.md,suggesting-improvements.md}
|contribute/blog:{_print.md,article-mirroring.md,article-submission.md,guidelines.md,release-comms.md,writing-buddy.md}
|contribute/generate-ref-docs:{_print.md,contribute-upstream.md,kubectl.md,kubernetes-api.md,kubernetes-components.md,metrics-reference.md,prerequisites-ref-docs.md,quickstart.md}
|contribute/new-content:{_print.md,case-studies.md,new-features.md,open-a-pr.md}
|contribute/participate:{_print.md,issue-wrangler.md,pr-wranglers.md,roles-and-responsibilities.md}
|contribute/review:{_print.md,for-approvers.md,reviewing-prs.md}
|contribute/style:{_print.md,content-guide.md,content-organization.md,diagram-guide.md,hugo-shortcodes.md,page-content-types.md,style-guide.md,write-new-topic.md}
### home

|home:{_print.md,supported-doc-versions.md}
### reference

|reference:{_print.md,access-authn-authz.md,command-line-tools-reference.md,config-api.md,debug-cluster.md,external-api.md,instrumentation.md,issues-security.md,kubectl.md,kubernetes-api.md,labels-annotations-taints.md,networking.md,node.md,scheduling.md,setup-tools.md,tools.md,using-api.md}
|reference/access-authn-authz:{_print.md,abac.md,admission-controllers.md,authentication.md,authorization.md,bootstrap-tokens.md,certificate-signing-requests.md,extensible-admission-controllers.md,kubelet-authn-authz.md,kubelet-tls-bootstrapping.md,mutating-admission-policy.md,node.md,psp-to-pod-security-standards.md,rbac.md,service-accounts-admin.md,validating-admission-policy.md,webhook.md}
|reference/command-line-tools-reference:{_print.md,feature-gates-removed.md,feature-gates.md,kube-apiserver.md,kube-controller-manager.md,kube-proxy.md,kube-scheduler.md,kubelet.md}
|reference/config-api:{_print.md,apiserver-admission.v1.md,apiserver-audit.v1.md,apiserver-config.v1.md,apiserver-config.v1alpha1.md,apiserver-config.v1beta1.md,apiserver-eventratelimit.v1alpha1.md,apiserver-webhookadmission.v1.md,client-authentication.v1.md,client-authentication.v1beta1.md,imagepolicy.v1alpha1.md,kube-controller-manager-config.v1alpha1.md,kube-proxy-config.v1alpha1.md,kube-scheduler-config.v1.md,kubeadm-config.v1beta3.md,kubeadm-config.v1beta4.md,kubeconfig.v1.md,kubelet-config.v1.md,kubelet-config.v1alpha1.md,kubelet-config.v1beta1.md,kubelet-credentialprovider.v1.md,kuberc.v1alpha1.md,kuberc.v1beta1.md}
|reference/debug-cluster:{_print.md,flow-control.md}
|reference/external-api:{_print.md,custom-metrics.v1beta2.md,external-metrics.v1beta1.md,metrics.v1beta1.md}
|reference/instrumentation:{_print.md,cri-pod-container-metrics.md,metrics.md,node-metrics.md,slis.md,understand-psi-metrics.md,zpages.md}
|reference/issues-security:{_print.md,issues.md,official-cve-feed.md,security.md}
|reference/kubectl:{_print.md,conventions.md,docker-cli-to-kubectl.md,generated.md,introduction.md,jsonpath.md,kubectl-cmds.md,kubectl.md,kuberc.md,quick-reference.md}
|reference/kubectl/generated:{_print.md,kubectl.md,kubectl_annotate.md,kubectl_api-resources.md,kubectl_api-versions.md,kubectl_apply.md,kubectl_attach.md,kubectl_auth.md,kubectl_autoscale.md,kubectl_certificate.md,kubectl_cluster-info.md,kubectl_completion.md,kubectl_config.md,kubectl_cordon.md,kubectl_cp.md,kubectl_create.md,kubectl_debug.md,kubectl_delete.md,kubectl_describe.md,kubectl_diff.md,kubectl_drain.md,kubectl_edit.md,kubectl_events.md,kubectl_exec.md,kubectl_explain.md,kubectl_expose.md,kubectl_get.md,kubectl_kustomize.md,kubectl_label.md,kubectl_logs.md,kubectl_options.md,kubectl_patch.md,kubectl_plugin.md,kubectl_port-forward.md,kubectl_proxy.md,kubectl_replace.md,kubectl_rollout.md,kubectl_run.md,kubectl_scale.md,kubectl_set.md,kubectl_taint.md,kubectl_top.md,kubectl_uncordon.md,kubectl_version.md,kubectl_wait.md}
|reference/kubectl/generated/kubectl_annotate:{_print.md}
|reference/kubectl/generated/kubectl_api-resources:{_print.md}
|reference/kubectl/generated/kubectl_api-versions:{_print.md}
|reference/kubectl/generated/kubectl_apply:{_print.md,kubectl_apply_edit-last-applied.md,kubectl_apply_set-last-applied.md,kubectl_apply_view-last-applied.md}
|reference/kubectl/generated/kubectl_attach:{_print.md}
|reference/kubectl/generated/kubectl_auth:{_print.md,kubectl_auth_can-i.md,kubectl_auth_reconcile.md,kubectl_auth_whoami.md}
|reference/kubectl/generated/kubectl_autoscale:{_print.md}
|reference/kubectl/generated/kubectl_certificate:{_print.md,kubectl_certificate_approve.md,kubectl_certificate_deny.md}
|reference/kubectl/generated/kubectl_cluster-info:{_print.md,kubectl_cluster-info_dump.md}
|reference/kubectl/generated/kubectl_completion:{_print.md}
|reference/kubectl/generated/kubectl_config:{_print.md,kubectl_config_current-context.md,kubectl_config_delete-cluster.md,kubectl_config_delete-context.md,kubectl_config_delete-user.md,kubectl_config_get-clusters.md,kubectl_config_get-contexts.md,kubectl_config_get-users.md,kubectl_config_rename-context.md,kubectl_config_set-cluster.md,kubectl_config_set-context.md,kubectl_config_set-credentials.md,kubectl_config_set.md,kubectl_config_unset.md,kubectl_config_use-context.md,kubectl_config_view.md}
|reference/kubectl/generated/kubectl_cordon:{_print.md}
|reference/kubectl/generated/kubectl_cp:{_print.md}
|reference/kubectl/generated/kubectl_create:{_print.md,kubectl_create_clusterrole.md,kubectl_create_clusterrolebinding.md,kubectl_create_configmap.md,kubectl_create_cronjob.md,kubectl_create_deployment.md,kubectl_create_ingress.md,kubectl_create_job.md,kubectl_create_namespace.md,kubectl_create_poddisruptionbudget.md,kubectl_create_priorityclass.md,kubectl_create_quota.md,kubectl_create_role.md,kubectl_create_rolebinding.md,kubectl_create_secret.md,kubectl_create_secret_docker-registry.md,kubectl_create_secret_generic.md,kubectl_create_secret_tls.md,kubectl_create_service.md,kubectl_create_service_clusterip.md,kubectl_create_service_externalname.md,kubectl_create_service_loadbalancer.md,kubectl_create_service_nodeport.md,kubectl_create_serviceaccount.md,kubectl_create_token.md}
|reference/kubectl/generated/kubectl_debug:{_print.md}
|reference/kubectl/generated/kubectl_delete:{_print.md}
|reference/kubectl/generated/kubectl_describe:{_print.md}
|reference/kubectl/generated/kubectl_diff:{_print.md}
|reference/kubectl/generated/kubectl_drain:{_print.md}
|reference/kubectl/generated/kubectl_edit:{_print.md}
|reference/kubectl/generated/kubectl_events:{_print.md}
|reference/kubectl/generated/kubectl_exec:{_print.md}
|reference/kubectl/generated/kubectl_explain:{_print.md}
|reference/kubectl/generated/kubectl_expose:{_print.md}
|reference/kubectl/generated/kubectl_get:{_print.md}
|reference/kubectl/generated/kubectl_kustomize:{_print.md}
|reference/kubectl/generated/kubectl_label:{_print.md}
|reference/kubectl/generated/kubectl_logs:{_print.md}
|reference/kubectl/generated/kubectl_options:{_print.md}
|reference/kubectl/generated/kubectl_patch:{_print.md}
|reference/kubectl/generated/kubectl_plugin:{_print.md,kubectl_plugin_list.md}
|reference/kubectl/generated/kubectl_port-forward:{_print.md}
|reference/kubectl/generated/kubectl_proxy:{_print.md}
|reference/kubectl/generated/kubectl_replace:{_print.md}
|reference/kubectl/generated/kubectl_rollout:{_print.md,kubectl_rollout_history.md,kubectl_rollout_pause.md,kubectl_rollout_restart.md,kubectl_rollout_resume.md,kubectl_rollout_status.md,kubectl_rollout_undo.md}
|reference/kubectl/generated/kubectl_run:{_print.md}
|reference/kubectl/generated/kubectl_scale:{_print.md}
|reference/kubectl/generated/kubectl_set:{_print.md,kubectl_set_env.md,kubectl_set_image.md,kubectl_set_resources.md,kubectl_set_selector.md,kubectl_set_serviceaccount.md,kubectl_set_subject.md}
|reference/kubectl/generated/kubectl_taint:{_print.md}
|reference/kubectl/generated/kubectl_top:{_print.md,kubectl_top_node.md,kubectl_top_pod.md}
|reference/kubectl/generated/kubectl_uncordon:{_print.md}
|reference/kubectl/generated/kubectl_version:{_print.md}
|reference/kubectl/generated/kubectl_wait:{_print.md}
|reference/kubernetes-api:{_print.md,authentication-resources.md,authorization-resources.md,cluster-resources.md,common-definitions.md,config-and-storage-resources.md,extend-resources.md,other-resources.md,policy-resources.md,service-resources.md,workload-resources.md}
|reference/kubernetes-api/authentication-resources:{_print.md,certificate-signing-request-v1.md,cluster-trust-bundle-v1beta1.md,pod-certificate-request-v1alpha1.md,self-subject-review-v1.md,service-account-v1.md,token-request-v1.md,token-review-v1.md}
|reference/kubernetes-api/authorization-resources:{_print.md,cluster-role-binding-v1.md,cluster-role-v1.md,local-subject-access-review-v1.md,role-binding-v1.md,role-v1.md,self-subject-access-review-v1.md,self-subject-rules-review-v1.md,subject-access-review-v1.md}
|reference/kubernetes-api/cluster-resources:{_print.md,api-service-v1.md,component-status-v1.md,event-v1.md,ip-address-v1.md,lease-candidate-v1beta1.md,lease-v1.md,namespace-v1.md,node-v1.md,runtime-class-v1.md,service-cidr-v1.md}
|reference/kubernetes-api/common-definitions:{_print.md,delete-options.md,label-selector.md,list-meta.md,local-object-reference.md,node-selector-requirement.md,object-field-selector.md,object-meta.md,object-reference.md,patch.md,quantity.md,resource-field-selector.md,status.md,typed-local-object-reference.md}
|reference/kubernetes-api/common-parameters:{common-parameters.md}
|reference/kubernetes-api/config-and-storage-resources:{_print.md,config-map-v1.md,csi-driver-v1.md,csi-node-v1.md,csi-storage-capacity-v1.md,persistent-volume-claim-v1.md,persistent-volume-v1.md,secret-v1.md,storage-class-v1.md,storage-version-migration-v1alpha1.md,volume-attachment-v1.md,volume-attributes-class-v1.md,volume.md}
|reference/kubernetes-api/extend-resources:{_print.md,custom-resource-definition-v1.md,device-class-v1.md,mutating-webhook-configuration-v1.md,validating-webhook-configuration-v1.md}
|reference/kubernetes-api/other-resources:{_print.md,mutating-admission-policy-binding-list-v1beta1.md}
|reference/kubernetes-api/policy-resources:{_print.md,flow-schema-v1.md,limit-range-v1.md,mutating-admission-policy-binding-v1alpha1.md,mutating-admission-policy-v1beta1.md,network-policy-v1.md,pod-disruption-budget-v1.md,priority-level-configuration-v1.md,resource-quota-v1.md,validating-admission-policy-binding-v1.md,validating-admission-policy-v1.md}
|reference/kubernetes-api/service-resources:{_print.md,endpoint-slice-v1.md,endpoints-v1.md,ingress-class-v1.md,ingress-v1.md,service-v1.md}
|reference/kubernetes-api/workload-resources:{_print.md,binding-v1.md,controller-revision-v1.md,cron-job-v1.md,daemon-set-v1.md,deployment-v1.md,device-taint-rule-v1alpha3.md,horizontal-pod-autoscaler-v1.md,horizontal-pod-autoscaler-v2.md,job-v1.md,pod-template-v1.md,pod-v1.md,priority-class-v1.md,replica-set-v1.md,replication-controller-v1.md,resource-claim-template-v1.md,resource-claim-v1.md,resource-slice-v1.md,stateful-set-v1.md}
|reference/labels-annotations-taints:{_print.md,audit-annotations.md}
|reference/networking:{_print.md,ports-and-protocols.md,service-protocols.md,virtual-ips.md}
|reference/node:{_print.md,device-plugin-api-versions.md,kernel-version-requirements.md,kubelet-checkpoint-api.md,kubelet-config-directory-merging.md,kubelet-files.md,node-labels.md,node-status.md,seccomp.md,swap-behavior.md,systemd-watchdog.md,topics-on-dockershim-and-cri-compatible-runtimes.md}
|reference/scheduling:{_print.md,config.md,policies.md}
|reference/setup-tools:{_print.md,kubeadm.md}
|reference/setup-tools/kubeadm:{_print.md,generated.md,implementation-details.md,kubeadm-alpha.md,kubeadm-certs.md,kubeadm-config.md,kubeadm-init-phase.md,kubeadm-init.md,kubeadm-join-phase.md,kubeadm-join.md,kubeadm-kubeconfig.md,kubeadm-reset-phase.md,kubeadm-reset.md,kubeadm-token.md,kubeadm-upgrade-phase.md,kubeadm-upgrade.md,kubeadm-version.md}
|reference/setup-tools/kubeadm/generated:{_print.md,kubeadm.md,kubeadm_certs.md,kubeadm_completion.md,kubeadm_config.md,kubeadm_init.md,kubeadm_join.md,kubeadm_kubeconfig.md,kubeadm_reset.md,kubeadm_token.md,kubeadm_upgrade.md,kubeadm_version.md,readme.md}
|reference/setup-tools/kubeadm/generated/kubeadm_certs:{_print.md,kubeadm_certs_certificate-key.md,kubeadm_certs_check-expiration.md,kubeadm_certs_generate-csr.md,kubeadm_certs_renew.md,kubeadm_certs_renew_admin.conf.md,kubeadm_certs_renew_all.md,kubeadm_certs_renew_apiserver-etcd-client.md,kubeadm_certs_renew_apiserver-kubelet-client.md,kubeadm_certs_renew_apiserver.md,kubeadm_certs_renew_controller-manager.conf.md,kubeadm_certs_renew_etcd-healthcheck-client.md,kubeadm_certs_renew_etcd-peer.md,kubeadm_certs_renew_etcd-server.md,kubeadm_certs_renew_front-proxy-client.md,kubeadm_certs_renew_scheduler.conf.md,kubeadm_certs_renew_super-admin.conf.md}
|reference/setup-tools/kubeadm/generated/kubeadm_completion:{_print.md}
|reference/setup-tools/kubeadm/generated/kubeadm_config:{_print.md,kubeadm_config_images.md,kubeadm_config_images_list.md,kubeadm_config_images_pull.md,kubeadm_config_migrate.md,kubeadm_config_print.md,kubeadm_config_print_init-defaults.md,kubeadm_config_print_join-defaults.md,kubeadm_config_print_reset-defaults.md,kubeadm_config_print_upgrade-defaults.md,kubeadm_config_validate.md}
|reference/setup-tools/kubeadm/generated/kubeadm_init:{_print.md,kubeadm_init_phase.md,kubeadm_init_phase_addon.md,kubeadm_init_phase_addon_all.md,kubeadm_init_phase_addon_coredns.md,kubeadm_init_phase_addon_kube-proxy.md,kubeadm_init_phase_bootstrap-token.md,kubeadm_init_phase_certs.md,kubeadm_init_phase_certs_all.md,kubeadm_init_phase_certs_apiserver-etcd-client.md,kubeadm_init_phase_certs_apiserver-kubelet-client.md,kubeadm_init_phase_certs_apiserver.md,kubeadm_init_phase_certs_ca.md,kubeadm_init_phase_certs_etcd-ca.md,kubeadm_init_phase_certs_etcd-healthcheck-client.md,kubeadm_init_phase_certs_etcd-peer.md,kubeadm_init_phase_certs_etcd-server.md,kubeadm_init_phase_certs_front-proxy-ca.md,kubeadm_init_phase_certs_front-proxy-client.md,kubeadm_init_phase_certs_sa.md,kubeadm_init_phase_control-plane.md,kubeadm_init_phase_control-plane_all.md,kubeadm_init_phase_control-plane_apiserver.md,kubeadm_init_phase_control-plane_controller-manager.md,kubeadm_init_phase_control-plane_scheduler.md,kubeadm_init_phase_etcd.md,kubeadm_init_phase_etcd_local.md,kubeadm_init_phase_kubeconfig.md,kubeadm_init_phase_kubeconfig_admin.md,kubeadm_init_phase_kubeconfig_all.md,kubeadm_init_phase_kubeconfig_controller-manager.md,kubeadm_init_phase_kubeconfig_kubelet.md,kubeadm_init_phase_kubeconfig_scheduler.md,kubeadm_init_phase_kubeconfig_super-admin.md,kubeadm_init_phase_kubelet-finalize.md,kubeadm_init_phase_kubelet-finalize_all.md,kubeadm_init_phase_kubelet-finalize_enable-client-cert-rotation.md,kubeadm_init_phase_kubelet-start.md,kubeadm_init_phase_mark-control-plane.md,kubeadm_init_phase_preflight.md,kubeadm_init_phase_show-join-command.md,kubeadm_init_phase_upload-certs.md,kubeadm_init_phase_upload-config.md,kubeadm_init_phase_upload-config_all.md,kubeadm_init_phase_upload-config_kubeadm.md,kubeadm_init_phase_upload-config_kubelet.md,kubeadm_init_phase_wait-control-plane.md}
|reference/setup-tools/kubeadm/generated/kubeadm_join:{_print.md,kubeadm_join_phase.md,kubeadm_join_phase_control-plane-join.md,kubeadm_join_phase_control-plane-join_all.md,kubeadm_join_phase_control-plane-join_etcd.md,kubeadm_join_phase_control-plane-join_mark-control-plane.md,kubeadm_join_phase_control-plane-prepare.md,kubeadm_join_phase_control-plane-prepare_all.md,kubeadm_join_phase_control-plane-prepare_certs.md,kubeadm_join_phase_control-plane-prepare_control-plane.md,kubeadm_join_phase_control-plane-prepare_download-certs.md,kubeadm_join_phase_control-plane-prepare_kubeconfig.md,kubeadm_join_phase_kubelet-start.md,kubeadm_join_phase_preflight.md,kubeadm_join_phase_wait-control-plane.md}
|reference/setup-tools/kubeadm/generated/kubeadm_kubeconfig:{_print.md,kubeadm_kubeconfig_user.md}
|reference/setup-tools/kubeadm/generated/kubeadm_reset:{_print.md,kubeadm_reset_phase.md,kubeadm_reset_phase_cleanup-node.md,kubeadm_reset_phase_preflight.md,kubeadm_reset_phase_remove-etcd-member.md}
|reference/setup-tools/kubeadm/generated/kubeadm_token:{_print.md,kubeadm_token_create.md,kubeadm_token_delete.md,kubeadm_token_generate.md,kubeadm_token_list.md}
|reference/setup-tools/kubeadm/generated/kubeadm_upgrade:{_print.md,kubeadm_upgrade_apply.md,kubeadm_upgrade_apply_phase.md,kubeadm_upgrade_apply_phase_addon.md,kubeadm_upgrade_apply_phase_addon_all.md,kubeadm_upgrade_apply_phase_addon_coredns.md,kubeadm_upgrade_apply_phase_addon_kube-proxy.md,kubeadm_upgrade_apply_phase_bootstrap-token.md,kubeadm_upgrade_apply_phase_control-plane.md,kubeadm_upgrade_apply_phase_kubelet-config.md,kubeadm_upgrade_apply_phase_post-upgrade.md,kubeadm_upgrade_apply_phase_preflight.md,kubeadm_upgrade_apply_phase_upload-config.md,kubeadm_upgrade_apply_phase_upload-config_all.md,kubeadm_upgrade_apply_phase_upload-config_kubeadm.md,kubeadm_upgrade_apply_phase_upload-config_kubelet.md,kubeadm_upgrade_diff.md,kubeadm_upgrade_node.md,kubeadm_upgrade_node_phase.md,kubeadm_upgrade_node_phase_addon.md,kubeadm_upgrade_node_phase_addon_all.md,kubeadm_upgrade_node_phase_addon_coredns.md,kubeadm_upgrade_node_phase_addon_kube-proxy.md,kubeadm_upgrade_node_phase_control-plane.md,kubeadm_upgrade_node_phase_kubelet-config.md,kubeadm_upgrade_node_phase_post-upgrade.md,kubeadm_upgrade_node_phase_preflight.md,kubeadm_upgrade_plan.md}
|reference/setup-tools/kubeadm/generated/kubeadm_version:{_print.md}
|reference/tools:{_print.md}
|reference/using-api:{_print.md,api-concepts.md,cel.md,client-libraries.md,declarative-validation.md,deprecation-guide.md,deprecation-policy.md,health-checks.md,server-side-apply.md}
### setup

|setup:{_print.md,best-practices.md,learning-environment.md,production-environment.md}
|setup/best-practices:{_print.md,certificates.md,cluster-large.md,enforcing-pod-security-standards.md,multiple-zones.md,node-conformance.md}
|setup/learning-environment:{_print.md}
|setup/production-environment:{_print.md,container-runtimes.md,tools.md,turnkey-solutions.md}
|setup/production-environment/tools:{_print.md,kubeadm.md}
|setup/production-environment/tools/kubeadm:{_print.md,control-plane-flags.md,create-cluster-kubeadm.md,dual-stack-support.md,ha-topology.md,high-availability.md,install-kubeadm.md,kubelet-integration.md,setup-ha-etcd-with-kubeadm.md,troubleshooting-kubeadm.md}
### tasks

|tasks:{_print.md,access-application-cluster.md,administer-cluster.md,configmap-secret.md,configure-pod-container.md,debug.md,extend-kubernetes.md,inject-data-application.md,job.md,manage-daemon.md,manage-kubernetes-objects.md,network.md,run-application.md,tls.md,tools.md}
|tasks/access-application-cluster:{_print.md,access-cluster-services.md,access-cluster.md,communicate-containers-same-pod-shared-volume.md,configure-access-multiple-clusters.md,configure-dns-cluster.md,connecting-frontend-backend.md,create-external-load-balancer.md,list-all-running-container-images.md,port-forward-access-application-cluster.md,service-access-application-cluster.md,web-ui-dashboard.md}
|tasks/administer-cluster:{_print.md,access-cluster-api.md,certificates.md,change-default-storage-class.md,change-pv-access-mode-readwriteoncepod.md,change-pv-reclaim-policy.md,cluster-upgrade.md,configure-feature-gates.md,configure-upgrade-etcd.md,controller-manager-leader-migration.md,coredns.md,cpu-management-policies.md,declare-network-policy.md,decrypt-data.md,developing-cloud-controller-manager.md,dns-custom-nameservers.md,dns-debugging-resolution.md,dns-horizontal-autoscaling.md,enable-disable-api.md,encrypt-data.md,extended-resource-node.md,guaranteed-scheduling-critical-addon-pods.md,ip-masq-agent.md,kms-provider.md,kubeadm.md,kubelet-config-file.md,kubelet-credential-provider.md,kubelet-in-userns.md,limit-storage-consumption.md,manage-resources.md,memory-manager.md,migrating-from-dockershim.md,namespaces.md,network-policy-provider.md,node-overprovisioning.md,nodelocaldns.md,quota-api-object.md,reserve-compute-resources.md,running-cloud-controller.md,safely-drain-node.md,securing-a-cluster.md,switch-to-evented-pleg.md,sysctl-cluster.md,topology-manager.md,use-cascading-deletion.md,verify-signed-artifacts.md}
|tasks/administer-cluster/kubeadm:{_print.md,adding-linux-nodes.md,adding-windows-nodes.md,change-package-repository.md,configure-cgroup-driver.md,kubeadm-certs.md,kubeadm-reconfigure.md,kubeadm-upgrade.md,upgrading-linux-nodes.md,upgrading-windows-nodes.md}
|tasks/administer-cluster/manage-resources:{_print.md,cpu-constraint-namespace.md,cpu-default-namespace.md,memory-constraint-namespace.md,memory-default-namespace.md,quota-memory-cpu-namespace.md,quota-pod-namespace.md}
|tasks/administer-cluster/migrating-from-dockershim:{_print.md,change-runtime-containerd.md,check-if-dockershim-removal-affects-you.md,find-out-runtime-you-use.md,migrating-telemetry-and-security-agents.md,troubleshooting-cni-plugin-related-errors.md}
|tasks/administer-cluster/network-policy-provider:{_print.md,antrea-network-policy.md,calico-network-policy.md,cilium-network-policy.md,kube-router-network-policy.md,romana-network-policy.md,weave-network-policy.md}
|tasks/configmap-secret:{_print.md,managing-secret-using-config-file.md,managing-secret-using-kubectl.md,managing-secret-using-kustomize.md}
|tasks/configure-pod-container:{_print.md,assign-cpu-resource.md,assign-memory-resource.md,assign-pod-level-resources.md,assign-pods-nodes-using-node-affinity.md,assign-pods-nodes.md,assign-resources.md,attach-handler-lifecycle-event.md,configure-gmsa.md,configure-liveness-readiness-startup-probes.md,configure-persistent-volume-storage.md,configure-pod-configmap.md,configure-pod-initialization.md,configure-projected-volume-storage.md,configure-runasusername.md,configure-service-account.md,configure-volume-storage.md,create-hostprocess-pod.md,enforce-standards-admission-controller.md,enforce-standards-namespace-labels.md,extended-resource.md,image-volumes.md,migrate-from-psp.md,pull-image-private-registry.md,quality-service-pod.md,resize-container-resources.md,security-context.md,share-process-namespace.md,static-pod.md,translate-compose-kubernetes.md,user-namespaces.md}
|tasks/configure-pod-container/assign-resources:{_print.md,allocate-devices-dra.md,set-up-dra-cluster.md}
|tasks/debug:{_print.md,debug-application.md,debug-cluster.md,logging.md,monitoring.md}
|tasks/debug/debug-application:{_print.md,debug-init-containers.md,debug-pods.md,debug-running-pod.md,debug-service.md,debug-statefulset.md,determine-reason-pod-failure.md,get-shell-running-container.md}
|tasks/debug/debug-cluster:{_print.md,audit.md,crictl.md,kubectl-node-debug.md,local-debugging.md,monitor-node-health.md,resource-metrics-pipeline.md,resource-usage-monitoring.md,troubleshoot-kubectl.md,windows.md}
|tasks/debug/logging:{_print.md}
|tasks/debug/monitoring:{_print.md}
|tasks/extend-kubectl:{kubectl-plugins.md}
|tasks/extend-kubernetes:{_print.md,configure-aggregation-layer.md,configure-multiple-schedulers.md,custom-resources.md,http-proxy-access-api.md,setup-extension-api-server.md,setup-konnectivity.md,socks5-proxy-access-api.md}
|tasks/extend-kubernetes/custom-resources:{_print.md,custom-resource-definition-versioning.md,custom-resource-definitions.md}
|tasks/inject-data-application:{_print.md,define-command-argument-container.md,define-environment-variable-container.md,define-environment-variable-via-file.md,define-interdependent-environment-variables.md,distribute-credentials-secure.md,downward-api-volume-expose-pod-information.md,environment-variable-expose-pod-information.md}
|tasks/job:{_print.md,automated-tasks-with-cron-jobs.md,coarse-parallel-processing-work-queue.md,fine-parallel-processing-work-queue.md,indexed-parallel-processing-static.md,job-with-pod-to-pod-communication.md,parallel-processing-expansion.md,pod-failure-policy.md}
|tasks/manage-daemon:{_print.md,create-daemon-set.md,pods-some-nodes.md,rollback-daemon-set.md,update-daemon-set.md}
|tasks/manage-gpus:{scheduling-gpus.md}
|tasks/manage-hugepages:{scheduling-hugepages.md}
|tasks/manage-kubernetes-objects:{_print.md,declarative-config.md,imperative-command.md,imperative-config.md,kustomization.md,storage-version-migration.md,update-api-object-kubectl-patch.md}
|tasks/network:{_print.md,customize-hosts-file-for-pods.md,extend-service-ip-ranges.md,reconfigure-default-service-ip-ranges.md,validate-dual-stack.md}
|tasks/run-application:{_print.md,access-api-from-pod.md,configure-pdb.md,delete-stateful-set.md,force-delete-stateful-set-pod.md,horizontal-pod-autoscale-walkthrough.md,horizontal-pod-autoscale.md,run-replicated-stateful-application.md,run-single-instance-stateful-application.md,run-stateless-application-deployment.md,scale-stateful-set.md}
|tasks/tls:{_print.md,certificate-issue-client-csr.md,certificate-rotation.md,managing-tls-in-a-cluster.md,manual-rotation-of-ca-certificates.md}
|tasks/tools:{_print.md,install-kubectl-linux.md,install-kubectl-macos.md,install-kubectl-windows.md}
### tutorials

|tutorials:{_print.md,cluster-management.md,configuration.md,hello-minikube.md,kubernetes-basics.md,security.md,services.md,stateful-application.md,stateless-application.md}
|tutorials/cluster-management:{_print.md,install-use-dra.md,kubelet-standalone.md,namespaces-walkthrough.md,provision-swap-memory.md}
|tutorials/configuration:{_print.md,configure-redis-using-configmap.md,pod-sidecar-containers.md,updating-configuration-via-a-configmap.md}
|tutorials/kubernetes-basics:{_print.md,create-cluster.md,deploy-app.md,explore.md,expose.md,scale.md,update.md}
|tutorials/kubernetes-basics/create-cluster:{_print.md,cluster-intro.md}
|tutorials/kubernetes-basics/deploy-app:{_print.md,deploy-intro.md}
|tutorials/kubernetes-basics/explore:{_print.md,explore-intro.md}
|tutorials/kubernetes-basics/expose:{_print.md,expose-intro.md}
|tutorials/kubernetes-basics/scale:{_print.md,scale-intro.md}
|tutorials/kubernetes-basics/update:{_print.md,update-intro.md}
|tutorials/security:{_print.md,apparmor.md,cluster-level-pss.md,ns-level-pss.md,seccomp.md}
|tutorials/services:{_print.md,connect-applications-service.md,pods-and-endpoint-termination-flow.md,source-ip.md}
|tutorials/stateful-application:{_print.md,basic-stateful-set.md,cassandra.md,mysql-wordpress-persistent-volume.md,zookeeper.md}
|tutorials/stateless-application:{_print.md,expose-external-ip-address.md,guestbook.md}

