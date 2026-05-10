<div wrapper="1" role="_abstract">

To create containerized applications in OpenShift Container Platform without manually configuring runtime environments, you can use Source-to-Image (S2I) images. S2I images are runtime base images for languages like Node.js, Python, and Java that you can insert your code into.

</div>

You can use the [Red Hat Software Collections](https://access.redhat.com/documentation/en-us/red_hat_software_collections/3/html-single/using_red_hat_software_collections_container_images/index) images as a foundation for applications that rely on specific runtime environments such as Node.js, Perl, or Python.

You can use the [Introduction to source-to-image for OpenShift](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/11/html/using_source-to-image_for_openshift_with_red_hat_build_of_openjdk_11/openjdk-overview-s2i-openshift) documentation as a reference for runtime environments that use Java.

S2I images are also available though the [Cluster Samples Operator](../../openshift_images/configuring-samples-operator.xml#configuring-samples-operator).

# Accessing S2I builder images in the OpenShift Container Platform Developer Console

<div wrapper="1" role="_abstract">

You can access S2I builder images through the Developer Console in the web console. You need these images to build containerized applications from your source code.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console using your login credentials. The default view for the OpenShift Container Platform web console is the **Administrator** perspective.

2.  Use the perspective switcher to switch to the **Developer** perspective.

3.  In the **+Add** view, use the **Project** drop-down list to select an existing project or create a new project.

4.  Click **All services** in the **Developer Catalog** tile.

5.  Click **Builder Images** under **Type** to see the available S2I images.

</div>

# Source-to-image build process overview

<div wrapper="1" role="_abstract">

Source-to-image (S2I) is a build process in OpenShift Container Platform that injects your source code into a container image. S2I automates the creation of ready-to-run container images from your application source code without manual configuration.

</div>

S2I performs the following steps:

1.  Runs the `FROM <builder image>` command

2.  Copies the source code to a defined location in the builder image

3.  Runs the assemble script in the builder image

4.  Sets the run script in the builder image as the default command

Buildah then creates the container image.

# Additional resources

- [Configuring the Cluster Samples Operator](../../openshift_images/configuring-samples-operator.xml#configuring-samples-operator)

- [Using build strategies](../../cicd/builds/build-strategies.xml#builds-strategy-s2i-build_build-strategies)

- [Troubleshooting the Source-to-Image process](../../support/troubleshooting/troubleshooting-s2i.xml#troubleshooting-s2i)

- [Creating images from source code with source-to-image](../../openshift_images/create-images.xml#images-create-s2i_create-images)

- [About testing source-to-image images](../../openshift_images/create-images.xml#images-test-s2i_create-images)

- [Creating images from source code with source-to-image](../../openshift_images/create-images.xml#images-create-s2i_create-images)
