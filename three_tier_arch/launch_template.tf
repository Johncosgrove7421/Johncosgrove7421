### Launch Template

resource "aws_launch_configuration" "launch_template" {
  name_prefix   = "Executive Presentation"
  image_id      = "ami-123456789" # CHANGE ME
  instance_type = "t2.micro"

  lifecycle {
    create_before_destroy = true
  }
# user_data = filebase64("${path.module}/example.sh")
}
