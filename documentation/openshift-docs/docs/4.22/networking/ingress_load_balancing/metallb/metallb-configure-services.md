<div wrapper="1" role="_abstract">

To ensure predictable network endpoints, control how MetalLB assigns IP addresses to services of type `LoadBalancer`. Requesting specific addresses or pools ensures that your applications receive valid IP assignments that align with your specific network addressing plan.

</div>

# Request a specific IP address

<div wrapper="1" role="_abstract">

To assign a specific, static IP address to a service, configure the `spec.loadBalancerIP` parameter in the service specification.

</div>

MetalLB attempts to assign the requested address from the configured address pools, ensuring that your service is reachable at a designated, static network endpoint. If the requested IP address is not within any range, MetalLB reports a warning.

<div class="formalpara">

<div class="title">

Example service YAML for a specific IP address

</div>

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: <service_name>
  annotations:
    metallb.io/address-pool: <address_pool_name>
spec:
  selector:
    <label_key>: <label_value>
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  type: LoadBalancer
  loadBalancerIP: <ip_address>
```

</div>

If MetalLB cannot assign the requested IP address, the `EXTERNAL-IP` for the service reports `<pending>` and running `oc describe service <service_name>` includes an event like the following example:

<div class="formalpara">

<div class="title">

Example event when MetalLB cannot assign a requested IP address

</div>

``` terminal
  ...
Events:
  Type     Reason            Age    From                Message
  ----     ------            ----   ----                -------
  Warning  AllocationFailed  3m16s  metallb-controller  Failed to allocate IP for "default/invalid-request": "4.3.2.1" is not allowed in config
```

</div>

# Request an IP address from a specific pool

<div wrapper="1" role="_abstract">

To ensure predictable network endpoints, control how MetalLB assigns IP addresses to services of type `LoadBalancer`. Requesting specific addresses or pools ensures that your applications receive valid IP assignments that align with your specific network addressing plan.

</div>

<div class="formalpara">

<div class="title">

Example service YAML for an IP address from a specific pool

</div>

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: <service_name>
  annotations:
    metallb.io/address-pool: <address_pool_name>
spec:
  selector:
    <label_key>: <label_value>
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  type: LoadBalancer
```

</div>

If the address pool that you specify for `<address_pool_name>` does not exist, MetalLB attempts to assign an IP address from any pool that permits automatic assignment.

# Accept any IP address

<div wrapper="1" role="_abstract">

To automatically allocate IP addresses to services without manual specification, configure MetalLB address pools to permit automatic assignment. MetalLB dynamically assigns available addresses from these pools, ensuring seamless service deployment and network connectivity.

</div>

<div class="formalpara">

<div class="title">

Example service YAML for accepting any IP address

</div>

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: <service_name>
spec:
  selector:
    <label_key>: <label_value>
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  type: LoadBalancer
```

</div>

# Share a specific IP address

<div wrapper="1" role="_abstract">

To colocate multiple services on a single IP address, apply the `metallb.io/allow-shared-ip` annotation to your service specifications. Configuring this annotation authorizes MetalLB to assign the same IP to multiple services, enabling efficient address usage while distinguishing traffic by port.

</div>

By default, services do not share IP addresses.

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: service-http
  annotations:
    metallb.io/address-pool: doc-example
    metallb.io/allow-shared-ip: "web-server-svc"
spec:
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 8080
  selector:
    <label_key>: <label_value>
  type: LoadBalancer
  loadBalancerIP: 172.31.249.7
# ...
---
apiVersion: v1
kind: Service
metadata:
  name: service-https
  annotations:
    metallb.io/address-pool: doc-example
    metallb.io/allow-shared-ip: "web-server-svc"
spec:
  ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: 8080
  selector:
    <label_key>: <label_value>
  type: LoadBalancer
  loadBalancerIP: 172.31.249.7
# ...
```

where:

`metallb.io/allow-shared-ip`
Specifies the same value for the `metallb.io/allow-shared-ip` annotation. This value is referred to as the *sharing key*.

`name.port`
Specifies different port numbers for the services.

`spec.selector`
Specifies identical pod selectors if you must specify `externalTrafficPolicy: local` so the services send traffic to the same set of pods. If you use the `cluster` external traffic policy, then the pod selectors do not need to be identical.

`spec.loadBalancerIP`
Optional parameter. If you specify the three preceding items, MetalLB might colocate the services on the same IP address. To ensure that services share an IP address, specify the IP address to share.

By default, Kubernetes does not allow multiprotocol load balancer services. This limitation would normally make it impossible to run a service like DNS that needs to listen on both TCP and UDP. To work around this limitation of Kubernetes with MetalLB, create two services:

- For one service, specify TCP and for the second service, specify UDP.

- In both services, specify the same pod selector.

- Specify the same sharing key and `spec.loadBalancerIP` value to colocate the TCP and UDP services on the same IP address.

# Configuring a service with MetalLB

<div wrapper="1" role="_abstract">

To expose an application to external network traffic, configure a load-balancing service. MetalLB assigns an external IP address from a configured address pool, ensuring that your application is reachable from outside the cluster.

</div>

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Install the MetalLB Operator and start MetalLB.

- Configure at least one address pool.

- Configure your network to route traffic from the clients to the host network for the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `<service_name>.yaml` file. In the file, set the `spec.type` parameter to `LoadBalancer`.

    Refer to the examples for information about how to request the external IP address that MetalLB assigns to the service.

2.  Create the service:

    ``` terminal
    $ oc apply -f <service_name>.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    service/<service_name> created
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Describe the service:

  ``` terminal
  $ oc describe service <service_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

      Name:                     <service_name>
      Namespace:                default
      Labels:                   <none>
      Annotations:              metallb.io/address-pool: doc-example
      Selector:                 app=service_name
      Type:                     LoadBalancer
      IP Family Policy:         SingleStack
      IP Families:              IPv4
      IP:                       10.105.237.254
      IPs:                      10.105.237.254
      LoadBalancer Ingress:     192.168.100.5
      Port:                     <unset>  80/TCP
      TargetPort:               8080/TCP
      NodePort:                 <unset>  30550/TCP
      Endpoints:                10.244.0.50:8080
      Session Affinity:         None
      External Traffic Policy:  Cluster
      Events:
        Type    Reason        Age                From             Message
        ----    ------        ----               ----             -------
        Normal  nodeAssigned  32m (x2 over 32m)  metallb-speaker  announcing from node "<node_name>"

  </div>

  where:

  `Annotations`
  Specifies the annotation that is present if you request an IP address from a specific pool.

  `Type`
  Specifies the service type that must indicate `LoadBalancer`.

  `LoadBalancer Ingress`
  Specifies the indicates the external IP address if the service is assigned correctly.

  `Events`
  Specifies the events parameter that indicates the node name that is assigned to announce the external IP address. If you experience an error, the events parameter indicates the reason for the error.

</div>
