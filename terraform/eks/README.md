## How To

```bash

## Initiate Terraform, only execute when you're first time running this.
make init

## Plan will show the result about what's gonna change.
make plan

## Apply will deploy to online environment which base on your plan result.
make apply

## If you changed the Terraform modules, please run update to fetch the newest module.
make update

```
 

## Access Kubernetes

```bash

## Use AWS CLI to update your kubeconfig to access this EKS cluster.
aws eks --region eu-west-2 update-kubeconfig --name demo-cluster 

## Test if it works.
kubectl get node

```

## Providers

| Name | Version |
|------|---------|
| aws | ~> 2.0 |
| terraform | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:-----:|
| AWS\_REGION | n/a | `string` | `"eu-west-2"` | no |
| cluster\_name | n/a | `any` | n/a | yes |
| enabled\_cluster\_log\_types | n/a | `list` | <pre>[<br>  "api"<br>]</pre> | no |
| endpoint\_private\_access | n/a | `string` | `"true"` | no |
| endpoint\_public\_access | n/a | `string` | `"true"` | no |
| kubernetes\_version | n/a | `string` | `"1.15"` | no |
| node\_desired\_capacity | n/a | `any` | n/a | yes |
| node\_disk\_size | n/a | `any` | n/a | yes |
| node\_instance\_type | n/a | `any` | n/a | yes |
| node\_max\_capacity | n/a | `any` | n/a | yes |
| node\_min\_capacity | n/a | `any` | n/a | yes |
| public\_access\_cidrs | White list for which CIDR can public access this cluster | `list` | <pre>[<br>  "61.220.65.15/32"<br>]</pre> | no |

## Outputs

| Name | Description |
|------|-------------|
| alb\_ingress\_role\_arn | n/a |
| aws\_iam\_openid\_connect\_provider\_arn | n/a |

