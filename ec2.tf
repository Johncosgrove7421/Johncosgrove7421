### Elastic IP Address

resource "aws_eip" "eip" {
  instance = aws_instance.ec2.id
  domain   = "vpc"
}

### EC2

resource "aws_instance" "ec2" {
  ami           = "ami-005e54dee72cc1d00" #CHANGE_ME
  instance_type = "t2.micro"

#  network_interface {
#    network_interface_id = aws_network_interface.network_interface.id
#    device_index         = 1
#  }

  credit_specification {
    cpu_credits = "unlimited"
  }
 # depends_on = [aws_network_interface.network_interface]
}

### Network Interface

resource "aws_network_interface" "network_interface" {
  subnet_id       = aws_subnet.subnet.id
  private_ips     = ["10.0.1.0"]
  security_groups = [aws_security_group.sg.id]

  attachment {
    instance     = aws_instance.ec2.id
    device_index = 1
  }
}
