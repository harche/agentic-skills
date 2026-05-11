<div wrapper="1" role="_abstract">

OpenShift Container Platform provides a secure, scalable foundation for running artificial intelligence (AI) workloads across training, inference, and data science workflows.

</div>

# Operators for running AI workloads

<div wrapper="1" role="_abstract">

You can use Operators to run artificial intelligence (AI) and machine learning (ML) workloads on OpenShift Container Platform. With Operators, you can build a customized environment that meets your specific AI/ML requirements while continuing to use OpenShift Container Platform as the core platform for your applications.

</div>

OpenShift Container Platform provides several Operators that can help you run AI workloads:

Red Hat build of Kueue
You can use Red Hat build of Kueue to provide structured queues and prioritization so that workloads are handled fairly and efficiently. Without proper prioritization, important jobs might be delayed while less critical jobs occupy resources.

For more information, see "Introduction to Red Hat build of Kueue".

Leader Worker Set Operator
You can use the Leader Worker Set Operator to enable large-scale AI inference workloads to run reliably across nodes with synchronization between leader and worker processes. Without proper coordination, large training runs might fail or stall.

For more information, see "Leader Worker Set Operator overview".

JobSet Operator (Technology Preview)
You can use the JobSet Operator to easily manage and run large-scale, coordinated workloads like high-performance computing (HPC) and AI training. The JobSet Operator can help you gain fast recovery and efficient resource use through features like multi-template job support and stable networking.

For more information, see "JobSet Operator overview".

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Introduction to Red Hat build of Kueue](../ai_workloads/kueue/about-kueue.xml#about-kueue)

- [Leader Worker Set Operator overview](../ai_workloads/leader_worker_set/index.xml#lws-about)

- [JobSet Operator overview](../ai_workloads/jobset_operator/index.xml#js-about)

</div>
