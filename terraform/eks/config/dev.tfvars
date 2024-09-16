## Global
AWS_REGION = "eu-west-2"


## EKS
cluster_name = "demo-cluster"
kubernetes_version = "1.15"
enabled_cluster_log_types = ["api"]
endpoint_private_access = "true"
endpoint_public_access = "true"
public_access_cidrs = [ "0.0.0.0/0" ]


## EKS Node Group
node_desired_capacity = 2
node_max_capacity = 4
node_min_capacity = 2


## Node Group Instance
node_disk_size = 20
node_instance_type = "t3.medium"


## Key Pair Name
key_pair_name = "deleteit"
