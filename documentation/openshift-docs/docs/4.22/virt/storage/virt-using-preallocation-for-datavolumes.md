<div wrapper="1" role="_abstract">

The Containerized Data Importer (CDI) can preallocate disk space to improve write performance when creating data volumes. You can enable preallocation for specific data volumes.

</div>

# About preallocation

<div wrapper="1" role="_abstract">

The Containerized Data Importer (CDI) can use the QEMU preallocate mode for data volumes to improve write performance. You can use preallocation mode for importing and uploading operations and when creating blank data volumes.

</div>

If preallocation is enabled, CDI uses the better preallocation method depending on the underlying file system and device type:

`fallocate`
If the file system supports it, CDI uses the operating system’s `fallocate` call to preallocate space by using the `posix_fallocate` function, which allocates blocks and marks them as uninitialized.

`full`
If `fallocate` mode cannot be used, `full` mode allocates space for the image by writing data to the underlying storage. Depending on the storage location, all the empty allocated space might be zeroed.

# Enabling preallocation for a data volume

<div wrapper="1" role="_abstract">

You can enable preallocation for specific data volumes by including the `spec.preallocation` field in the data volume manifest. You can enable preallocation mode in either the web console or by using the OpenShift CLI (`oc`).

</div>

Preallocation mode is supported for all CDI source types. However, preallocation is ignored for cloning operations.

<div>

<div class="title">

Procedure

</div>

- Specify the `spec.preallocation` field in the data volume manifest:

  ``` yaml
  apiVersion: cdi.kubevirt.io/v1beta1
  kind: DataVolume
  metadata:
    name: preallocated-datavolume
  spec:
    source:
      registry:
        url: <image_url>
    storage:
      resources:
        requests:
          storage: 1Gi
    preallocation: true
  # ...
  ```

  where:

  `<image_url>`
  Specifies the URL of the data source in your registry.

</div>
