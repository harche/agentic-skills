<div wrapper="1" role="_abstract">

OpenShift Container Platform offers a set of command-line interface (CLI) tools that enable users to perform various administration and development operations from the terminal. These tools expose simple commands to manage the applications, as well as interact with each component of the system.

</div>

For example, you can use the CLI to complete the following operations:

- Manage clusters

- Build, deploy, and manage applications

- Manage deployment processes

- Create and maintain Operator catalogs

# List of CLI tools

<div wrapper="1" role="_abstract">

Review the primary command-line interface (CLI) tools available for OpenShift Container Platform, including tools for cluster administration, application development, and Operator management.

</div>

Use the following tools to manage your cluster from the terminal:

- [OpenShift CLI (`oc`)](../cli_reference/openshift_cli/getting-started-cli.xml#cli-getting-started): This is the most commonly used CLI tool by OpenShift Container Platform users. It helps both cluster administrators and developers to perform end-to-end operations across OpenShift Container Platform using the terminal. Unlike the web console, it allows the user to work directly with the project source code using command scripts.

- [Knative CLI (kn)](../cli_reference/kn-cli-tools.xml#kn-cli-tools): The Knative (`kn`) CLI tool provides simple and intuitive terminal commands that can be used to interact with OpenShift Serverless components, such as Knative Serving and Eventing.

- [Pipelines CLI (tkn)](../cli_reference/tkn_cli/installing-tkn.xml#installing-tkn): OpenShift Pipelines is a continuous integration and continuous delivery (CI/CD) solution in OpenShift Container Platform, which internally uses Tekton. The `tkn` CLI tool provides simple and intuitive commands to interact with OpenShift Pipelines using the terminal.

- [opm CLI](../cli_reference/opm/cli-opm-install.xml#cli-opm-install): The `opm` CLI tool helps the Operator developers and cluster administrators to create and maintain the catalogs of Operators from the terminal.
