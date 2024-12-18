### Subnets

resource "aws_subnet" "subnet" {
  vpc_id            = aws_vpc.vpc.id
  for_each          = var.subnets
  cidr_block        = each.vaule.cidr_block
  availability_zone = each.vaule.az

  tags = {
    Name = "Executive Presentation"
  }
}
