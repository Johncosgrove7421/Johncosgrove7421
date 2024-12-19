### Application Load Balancer

resource "aws_lb" "alb" {
  name               = "Executive Presentation"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_default_security_group.sg.id]
  subnets            = [for subnet in aws_subnet.subnet : subnet.id]

  enable_deletion_protection = true

  access_logs {
    bucket  = aws_s3_bucket.s3.id
#    prefix  = "test-lb"
    enabled = true
  }

  tags = {
    Environment = "Executive Presentation"
  }
}
