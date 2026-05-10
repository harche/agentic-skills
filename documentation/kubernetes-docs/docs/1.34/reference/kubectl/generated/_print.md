This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/generated/).

# kubectl reference

* 1: [kubectl](#pg-402909613e0ae370b616c0caac29621f)
* 2: [kubectl annotate](#pg-36ff86c01e1c63f208a2d2d1db6b6a4f)

* 3: [kubectl api-resources](#pg-8ecdd5ca9c4f7724f144aa46a98e0ec9)

* 4: [kubectl api-versions](#pg-5f872ac31510d52a53ab72cea7fa29cf)

* 5: [kubectl apply](#pg-3eea9e13de34e9bb4ad11c9c30bd249c)

+ 5.1: [kubectl apply edit-last-applied](#pg-641acfde6e8164afe190eb62ae5c205d)
+ 5.2: [kubectl apply set-last-applied](#pg-e1a3553640a80681da6b4bbe66760ab3)
+ 5.3: [kubectl apply view-last-applied](#pg-c4d0a4727091a0e42ffa9cf8a0ad2329)

* 6: [kubectl attach](#pg-0e29e49eae92a6e42de742686ece8e59)

* 7: [kubectl auth](#pg-5c6cdd7674d19af1f0ed5161db1abb07)

+ 7.1: [kubectl auth can-i](#pg-9fd383dbd061a4bd429962c0884141dc)
+ 7.2: [kubectl auth reconcile](#pg-b63cd4df7b8fc6f18e4e048aca007433)
+ 7.3: [kubectl auth whoami](#pg-55334cff1ad1de8913da0e79bd424c99)

* 8: [kubectl autoscale](#pg-b4d81752c4bebc716cf5a6621248ddbf)

* 9: [kubectl certificate](#pg-b0655c69bc929ffef16ad59fb060e9b0)

+ 9.1: [kubectl certificate approve](#pg-7470128dc60bc72d430ee382f36ef6d3)
+ 9.2: [kubectl certificate deny](#pg-c27805149b129dc7843215976f95fc68)

* 10: [kubectl cluster-info](#pg-35437a08dd53ca5d9e79117020a6856a)

+ 10.1: [kubectl cluster-info dump](#pg-2b6cbcd733c21832d8ebf57781964754)

* 11: [kubectl completion](#pg-1c563fdb012166230fcf8d4b4ae572cd)

* 12: [kubectl config](#pg-e93d0796f4e6f7df1ab6fe9f32d32af3)

+ 12.1: [kubectl config current-context](#pg-5014b54facef233a63885234ce91c3aa)
+ 12.2: [kubectl config delete-cluster](#pg-aecc079c7de2d3be561601daf1d6684c)
+ 12.3: [kubectl config delete-context](#pg-b5f24b4e3009ebba0a0f4ad35af0d4ab)
+ 12.4: [kubectl config delete-user](#pg-d77b4cbd068f250f86cff5c2e75dabda)
+ 12.5: [kubectl config get-clusters](#pg-1176518e0a720b52609f27e88abef8eb)
+ 12.6: [kubectl config get-contexts](#pg-f96682991dc356384f3888c21b013cd6)
+ 12.7: [kubectl config get-users](#pg-3a4916efcdffdb896b4619a1a5cbd87b)
+ 12.8: [kubectl config rename-context](#pg-4f49ec6f9e1def05f72cfd83d8e26f34)
+ 12.9: [kubectl config set](#pg-fddfa538835c3f9a09666f6713f07278)
+ 12.10: [kubectl config set-cluster](#pg-c6f09b5a087eb07fce8acb3d3db38e22)
+ 12.11: [kubectl config set-context](#pg-2500189be627eaffa4b161af5dd9a178)
+ 12.12: [kubectl config set-credentials](#pg-b3b6ccdb55698e26fcd43bf215002c58)
+ 12.13: [kubectl config unset](#pg-f82900d692231ec20a5fc6465c06e298)
+ 12.14: [kubectl config use-context](#pg-f6ec7b5627422d529c65ee106681fea2)
+ 12.15: [kubectl config view](#pg-3bfacbe2914206676749a842aa0d00f2)

* 13: [kubectl cordon](#pg-114515632079608ac9c1631e3bd46aaa)

* 14: [kubectl cp](#pg-281884941d738cd8fa58091afa664824)

* 15: [kubectl create](#pg-953771ff28f42694f3cccf8b294bbee0)

+ 15.1: [kubectl create clusterrole](#pg-bc9f354d308d4b7b92bd1e2c199dd4d1)
+ 15.2: [kubectl create clusterrolebinding](#pg-b580bc796e16cf5c330344854759b767)
+ 15.3: [kubectl create configmap](#pg-d7a078683e8028884681580d3da9c355)
+ 15.4: [kubectl create cronjob](#pg-8623e760bcd816213276f920925c7c9f)
+ 15.5: [kubectl create deployment](#pg-85938a5e506af5d05edc154a7ba45ee7)
+ 15.6: [kubectl create ingress](#pg-454f37b7a4a10acbcb73ee1faefe7ba6)
+ 15.7: [kubectl create job](#pg-962e637e4ac9ca350d8717c056c77268)
+ 15.8: [kubectl create namespace](#pg-8b99d360d189a763d8828d8dad70db8a)
+ 15.9: [kubectl create poddisruptionbudget](#pg-1e27a1c88d08b9addd57196b0559c087)
+ 15.10: [kubectl create priorityclass](#pg-ba25e70aa569d978cd2bec9f32ce0dba)
+ 15.11: [kubectl create quota](#pg-e28159f2e6cb8aa3120d1e88a2e3e404)
+ 15.12: [kubectl create role](#pg-01fc591ca5a786b8d3ed390ef6b72ad5)
+ 15.13: [kubectl create rolebinding](#pg-df4b1aa40a6f6a6f8645261cacb35972)
+ 15.14: [kubectl create secret](#pg-de61418fe2b7a032a7336d6c27fb27be)
+ 15.15: [kubectl create secret docker-registry](#pg-76970ddfe96bc2cf910756946387250e)
+ 15.16: [kubectl create secret generic](#pg-68b32a259fda3582817081388caa0330)
+ 15.17: [kubectl create secret tls](#pg-4033b20aaa417f9e2081d96419a6ee45)
+ 15.18: [kubectl create service](#pg-e0cf2bf7674d167398f315e6a67e1379)
+ 15.19: [kubectl create service clusterip](#pg-8b94cb3a05077a406591bf6b1886edc2)
+ 15.20: [kubectl create service externalname](#pg-d5f597b1de53f09bf2bea1855a981247)
+ 15.21: [kubectl create service loadbalancer](#pg-a1edd453dd57d18385eb35c8e33431a4)
+ 15.22: [kubectl create service nodeport](#pg-a0df1e98366de5c5261e1414770c68f9)
+ 15.23: [kubectl create serviceaccount](#pg-811bd5ff9c057c6c3e7755acabbc824a)
+ 15.24: [kubectl create token](#pg-ee534c7541a0919bdd14e6411d8067b8)

* 16: [kubectl debug](#pg-b034a7678879340ad25bafdd9551d22a)

* 17: [kubectl delete](#pg-ab346c76d590e8ad07e20fccaa45c980)

* 18: [kubectl describe](#pg-b2c625f46a85287d2c0551154b769024)

* 19: [kubectl diff](#pg-7eaa64344ffe7b4fb8fb0752f1b97d9f)

* 20: [kubectl drain](#pg-aa964bf4ff4621badcc87e1cd0e32681)

* 21: [kubectl edit](#pg-8cf21077f8795e0b16fde83d11567578)

* 22: [kubectl events](#pg-a88e5c3601e2bf7b0293034f5e81e821)

* 23: [kubectl exec](#pg-882aa52820297ac9293dd44da8672f3e)

* 24: [kubectl explain](#pg-41e90bac90aec872d864dcc94d5b90f8)

* 25: [kubectl expose](#pg-5775bf192e6208ef0a2b85dfc8a7d38a)

* 26: [kubectl get](#pg-34144509b7c5215e39120b601448cc40)

* 27: [kubectl kustomize](#pg-92353483fed3c33db48f9bc79e3d023c)

* 28: [kubectl label](#pg-f5c069064e2fcd06616d62599428f308)

* 29: [kubectl logs](#pg-ac35b1a6ed39fbe561feef25dc882275)

* 30: [kubectl options](#pg-b2b46c4956d34ec270e4c76b5d05c493)

* 31: [kubectl patch](#pg-30e2662613e2fd6dd67f08bc734a6ad5)

* 32: [kubectl plugin](#pg-997eb0d8f0bb60112e8d0b0b0d46ef14)

+ 32.1: [kubectl plugin list](#pg-4025c6d57b4a953ffeb1dbaf8a201201)

* 33: [kubectl port-forward](#pg-6d0ce5cb4810fe1ec32c075d9b8e31ba)

* 34: [kubectl proxy](#pg-9133e2fab485b02227c141ef2c8b86f1)

* 35: [kubectl replace](#pg-836e50cbd85466dc75e3134956ff3aea)

* 36: [kubectl rollout](#pg-e8086f0539497d9723d72fa8b5f54952)

+ 36.1: [kubectl rollout history](#pg-feee355d0921a2dae193326b4569c1c4)
+ 36.2: [kubectl rollout pause](#pg-a45554a76bb1970815575b0d0eb8eb78)
+ 36.3: [kubectl rollout restart](#pg-dff2e5df7176c0f397625767a6624bf4)
+ 36.4: [kubectl rollout resume](#pg-a2718a937a9d531c87d0c31ba738c112)
+ 36.5: [kubectl rollout status](#pg-5162a0abebfda06de0129978dff33fa3)
+ 36.6: [kubectl rollout undo](#pg-decea050af73d7440fc036efb9ff569f)

* 37: [kubectl run](#pg-7e05911b36fcf1c8870f9debcb704446)

* 38: [kubectl scale](#pg-e363c273030dec7915a0dcd2f0e5a4f0)

* 39: [kubectl set](#pg-366c76c7b3d5aaa4bfbb45015d99bf15)

+ 39.1: [kubectl set env](#pg-8efccafb687ee15419a3c10a01f52499)
+ 39.2: [kubectl set image](#pg-5f280fa194c35dcc401bf7a8b16df02d)
+ 39.3: [kubectl set resources](#pg-bd8b811c676cdb149ca3cad198624d9f)
+ 39.4: [kubectl set selector](#pg-affb9944665fc880f3ebb6edf7673214)
+ 39.5: [kubectl set serviceaccount](#pg-3118ff763cfaafe03d807a502e48e967)
+ 39.6: [kubectl set subject](#pg-e9c5704d912a656bcc627016d1045699)

* 40: [kubectl taint](#pg-584242a5667621cd3d0ce458d12e10bc)

* 41: [kubectl top](#pg-de8407a2eccd93c98c5b0eca954fb881)

+ 41.1: [kubectl top node](#pg-24aaff2b409245e171479e8dd8790013)
+ 41.2: [kubectl top pod](#pg-765f5bf8510a311aaa87e1027328a2ef)

* 42: [kubectl uncordon](#pg-8c1849e7de1aec914e31a94c032a0f6a)

* 43: [kubectl version](#pg-ad13feebe933b7228fb9472fc822a3c0)

* 44: [kubectl wait](#pg-1bf01c4ed4581610178c3f20a5cd043f)
