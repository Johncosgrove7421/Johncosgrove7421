### Autoscaling Group

resource "aws_autoscaling_group" "asg" {
  name                      = "Executive Presentation"
  max_size                  = 5
  min_size                  = 2
  health_check_grace_period = 300
  health_check_type         = "ELB"
  desired_capacity          = 2
  force_delete              = true
  placement_group           = aws_placement_group.test.id
  launch_configuration      = aws_launch_configuration.launch_temp.name
  vpc_zone_identifier       = [aws_subnet.subnet.id]

  instance_maintenance_policy {
    min_healthy_percentage = 90
    max_healthy_percentage = 120
  }
}
