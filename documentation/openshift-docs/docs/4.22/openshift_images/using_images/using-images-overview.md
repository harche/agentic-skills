<div wrapper="1" role="_abstract">

To build and deploy containerized applications in OpenShift Container Platform, you can use Source-to-Image (S2I), database, and other container images. These images provide the base components you need to run applications on your cluster.

</div>

Red Hat official container images are provided in the Red Hat Registry at [registry.redhat.io](https://registry.redhat.io). OpenShift Container Platform’s supported S2I, database, and Jenkins images are provided in the `openshift4` repository in the Red Hat Quay Registry. For example, `quay.io/openshift-release-dev/ocp-v4.0-<address>` is the name of the OpenShift Application Platform image.

The xPaaS middleware images are provided in their respective product repositories on the Red Hat Registry but suffixed with a `-openshift`. For example, `registry.redhat.io/jboss-eap-6/eap64-openshift` is the name of the JBoss EAP image.

All Red Hat supported images covered in this section are described in the [Container images section of the Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/explore). For every version of each image, you can find details on its contents and usage. Browse or search for the image that interests you.

> [!IMPORTANT]
> The newer versions of container images are not compatible with earlier versions of OpenShift Container Platform. Verify and use the correct version of container images, based on your version of OpenShift Container Platform.
