variable "subnets" {
  description = "List of subnets to create"
  type        = map(object({
    cidr_block = string
    az         = string
  }))
  default = {
    subnet1 = { cidr_block = "10.0.1.0/24", az = "us-east-1a" }
    subnet2 = { cidr_block = "10.0.2.0/24", az = "us-east-1a" }
    subnet3 = { cidr_block = "10.0.3.0/24", az = "us-east-1b" }
    subnet4 = { cidr_block = "10.0.4.0/24", az = "us-east-1b" }
    subnet5 = { cidr_block = "10.0.5.0/24", az = "us-east-1c" }
    subnet6 = { cidr_block = "10.0.6.0/24", az = "us-east-1c" }
  }
}
