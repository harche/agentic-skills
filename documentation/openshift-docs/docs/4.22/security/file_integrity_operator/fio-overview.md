The File Integrity Operator continually runs file integrity checks on the cluster nodes. It deploys a DaemonSet that initializes and runs privileged [Advanced Intrusion Detection Environment](https://aide.github.io/) (AIDE) containers on each node, providing a log of files that have been modified since the initial run of the DaemonSet pods.

> [!NOTE]
> File Integrity Operator is not supported on HCP clusters.

For the latest updates, see the [File Integrity Operator release notes](../../security/file_integrity_operator/file-integrity-operator-release-notes.xml#file-integrity-operator-release-notes).

[Installing the File Integrity Operator](../../security/file_integrity_operator/file-integrity-operator-installation.xml#installing-file-integrity-operator)

[Updating the File Integrity Operator](../../security/file_integrity_operator/file-integrity-operator-updating.xml#file-integrity-operator-updating)

[Understanding the File Integrity Operator](../../security/file_integrity_operator/file-integrity-operator-understanding.xml#understanding-file-integrity-operator)

[Configuring the Custom File Integrity Operator](../../security/file_integrity_operator/file-integrity-operator-configuring.xml#configuring-file-integrity-operator)

[Performing advanced Custom File Integrity Operator tasks](../../security/file_integrity_operator/file-integrity-operator-advanced-usage.xml#file-integrity-operator-advanced-usage)

[Troubleshooting the File Integrity Operator](../../security/file_integrity_operator/file-integrity-operator-troubleshooting.xml#troubleshooting-file-integrity-operator)

[Uninstalling the File Integrity Operator](../../security/file_integrity_operator/fio-uninstalling.xml#fio-uninstalling)
