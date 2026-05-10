# Generate Certificates Manually

When using client certificate authentication, you can generate certificates
manually through [`easyrsa`](https://github.com/OpenVPN/easy-rsa), [`openssl`](https://github.com/openssl/openssl) or [`cfssl`](https://github.com/cloudflare/cfssl).

### easyrsa

**easyrsa** can manually generate certificates for your cluster.

1. Download, unpack, and initialize the patched version of `easyrsa3`.

   ```
   curl -LO https://dl.k8s.io/easy-rsa/easy-rsa.tar.gz
   tar xzf easy-rsa.tar.gz
   cd easy-rsa-master/easyrsa3
   ./easyrsa init-pki
   ```
2. Generate a new certificate authority (CA). `--batch` sets automatic mode;
   `--req-cn` specifies the Common Name (CN) for the CA's new root certificate.

   ```
   ./easyrsa --batch "--req-cn=${MASTER_IP}@`date +%s`" build-ca nopass
   ```
3. Generate server certificate and key.

   The argument `--subject-alt-name` sets the possible IPs and DNS names the API server will
   be accessed with. The `MASTER_CLUSTER_IP` is usually the first IP from the service CIDR
   that is specified as the `--service-cluster-ip-range` argument for both the API server and
   the controller manager component. The argument `--days` is used to set the number of days
   after which the certificate expires.
   The sample below also assumes that you are using `cluster.local` as the default
   DNS domain name.

   ```
   ./easyrsa --subject-alt-name="IP:${MASTER_IP},"\
   "IP:${MASTER_CLUSTER_IP},"\
   "DNS:kubernetes,"\
   "DNS:kubernetes.default,"\
   "DNS:kubernetes.default.svc,"\
   "DNS:kubernetes.default.svc.cluster,"\
   "DNS:kubernetes.default.svc.cluster.local" \
   --days=10000 \
   build-server-full server nopass
   ```
4. Copy `pki/ca.crt`, `pki/issued/server.crt`, and `pki/private/server.key` to your directory.
5. Fill in and add the following parameters into the API server start parameters:

   ```
   --client-ca-file=/yourdirectory/ca.crt
   --tls-cert-file=/yourdirectory/server.crt
   --tls-private-key-file=/yourdirectory/server.key
   ```

### openssl

**openssl** can manually generate certificates for your cluster.

1. Generate a ca.key with 2048bit:

   ```
   openssl genrsa -out ca.key 2048
   ```
2. According to the ca.key generate a ca.crt (use `-days` to set the certificate effective time):

   ```
   openssl req -x509 -new -nodes -key ca.key -subj "/CN=${MASTER_IP}" -days 10000 -out ca.crt
   ```
3. Generate a server.key with 2048bit:

   ```
   openssl genrsa -out server.key 2048
   ```
4. Create a config file for generating a Certificate Signing Request (CSR).

   Be sure to substitute the values marked with angle brackets (e.g. `<MASTER_IP>`)
   with real values before saving this to a file (e.g. `csr.conf`).
   Note that the value for `MASTER_CLUSTER_IP` is the service cluster IP for the
   API server as described in previous subsection.
   The sample below also assumes that you are using `cluster.local` as the default
   DNS domain name.

   ```
   [ req ]
   default_bits = 2048
   prompt = no
   default_md = sha256
   req_extensions = req_ext
   distinguished_name = dn

   [ dn ]
   C = <country>
   ST = <state>
   L = <city>
   O = <organization>
   OU = <organization unit>
   CN = <MASTER_IP>

   [ req_ext ]
   subjectAltName = @alt_names

   [ alt_names ]
   DNS.1 = kubernetes
   DNS.2 = kubernetes.default
   DNS.3 = kubernetes.default.svc
   DNS.4 = kubernetes.default.svc.cluster
   DNS.5 = kubernetes.default.svc.cluster.local
   IP.1 = <MASTER_IP>
   IP.2 = <MASTER_CLUSTER_IP>

   [ v3_ext ]
   authorityKeyIdentifier=keyid,issuer:always
   basicConstraints=CA:FALSE
   keyUsage=keyEncipherment,dataEncipherment
   extendedKeyUsage=serverAuth,clientAuth
   subjectAltName=@alt_names
   ```
5. Generate the certificate signing request based on the config file:

   ```
   openssl req -new -key server.key -out server.csr -config csr.conf
   ```
6. Generate the server certificate using the ca.key, ca.crt and server.csr:

   ```
   openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
       -CAcreateserial -out server.crt -days 10000 \
       -extensions v3_ext -extfile csr.conf -sha256
   ```
7. View the certificate signing request:

   ```
   openssl req  -noout -text -in ./server.csr
   ```
8. View the certificate:

   ```
   openssl x509  -noout -text -in ./server.crt
   ```

Finally, add the same parameters into the API server start parameters.

### cfssl

**cfssl** is another tool for certificate generation.

1. Download, unpack and prepare the command line tools as shown below.

   Note that you may need to adapt the sample commands based on the hardware
   architecture and cfssl version you are using.

   ```
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssl_1.5.0_linux_amd64 -o cfssl
   chmod +x cfssl
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssljson_1.5.0_linux_amd64 -o cfssljson
   chmod +x cfssljson
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssl-certinfo_1.5.0_linux_amd64 -o cfssl-certinfo
   chmod +x cfssl-certinfo
   ```
2. Create a directory to hold the artifacts and initialize cfssl:

   ```
   mkdir cert
   cd cert
   ../cfssl print-defaults config > config.json
   ../cfssl print-defaults csr > csr.json
   ```
3. Create a JSON config file for generating the CA file, for example, `ca-config.json`:

   ```
   {
     "signing": {
       "default": {
         "expiry": "8760h"
       },
       "profiles": {
         "kubernetes": {
           "usages": [
             "signing",
             "key encipherment",
             "server auth",
             "client auth"
           ],
           "expiry": "8760h"
         }
       }
     }
   }
   ```
4. Create a JSON config file for CA certificate signing request (CSR), for example,
   `ca-csr.json`. Be sure to replace the values marked with angle brackets with
   real values you want to use.

   ```
   {
     "CN": "kubernetes",
     "key": {
       "algo": "rsa",
       "size": 2048
     },
     "names":[{
       "C": "<country>",
       "ST": "<state>",
       "L": "<city>",
       "O": "<organization>",
       "OU": "<organization unit>"
     }]
   }
   ```
5. Generate CA key (`ca-key.pem`) and certificate (`ca.pem`):

   ```
   ../cfssl gencert -initca ca-csr.json | ../cfssljson -bare ca
   ```
6. Create a JSON config file for generating keys and certificates for the API
   server, for example, `server-csr.json`. Be sure to replace the values in angle brackets with
   real values you want to use. The `<MASTER_CLUSTER_IP>` is the service cluster
   IP for the API server as described in previous subsection.
   The sample below also assumes that you are using `cluster.local` as the default
   DNS domain name.

   ```
   {
     "CN": "kubernetes",
     "hosts": [
       "127.0.0.1",
       "<MASTER_IP>",
       "<MASTER_CLUSTER_IP>",
       "kubernetes",
       "kubernetes.default",
       "kubernetes.default.svc",
       "kubernetes.default.svc.cluster",
       "kubernetes.default.svc.cluster.local"
     ],
     "key": {
       "algo": "rsa",
       "size": 2048
     },
     "names": [{
       "C": "<country>",
       "ST": "<state>",
       "L": "<city>",
       "O": "<organization>",
       "OU": "<organization unit>"
     }]
   }
   ```
7. Generate the key and certificate for the API server, which are by default
   saved into file `server-key.pem` and `server.pem` respectively:

   ```
   ../cfssl gencert -ca=ca.pem -ca-key=ca-key.pem \
        --config=ca-config.json -profile=kubernetes \
        server-csr.json | ../cfssljson -bare server
   ```

## Distributing Self-Signed CA Certificate

A client node may refuse to recognize a self-signed CA certificate as valid.
For a non-production deployment, or for a deployment that runs behind a company
firewall, you can distribute a self-signed CA certificate to all clients and
refresh the local list for valid certificates.

On each client, perform the following operations:

```
sudo cp ca.crt /usr/local/share/ca-certificates/kubernetes.crt
sudo update-ca-certificates
```

```
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d....
done.
```

## Certificates API

You can use the `certificates.k8s.io` API to provision
x509 certificates to use for authentication as documented
in the [Managing TLS in a cluster](/docs/tasks/tls/managing-tls-in-a-cluster/)
task page.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
