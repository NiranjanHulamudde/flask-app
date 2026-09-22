data "aws_ami" "ubuntu" {
	most_recent = true
	filter {
		name = "name"
		values	= ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
}	
	owners = ["099720109477"]
}

resource "aws_security_group" "flask-sg" {
	name = "flask-app-sg"
	description = "ssh traffic"
	
	ingress {
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
}
	ingress {
                from_port = 5000 #application traffic
                to_port = 5000
                protocol = "tcp"
                cidr_blocks = ["0.0.0.0/0"]
}
	egress {
		from_port = 0
		to_port = 0
		protocol = "-1"
		cidr_blocks = ["0.0.0.0/0"]
}

}


resource "aws_instance" "flask-service" {
	ami	= data.aws_ami.ubuntu.id
	instance_type = "t3.micro"


	key_name = "passkey"
	
	user_data = <<-EOF
              #!/bin/bash
              # 1. Install and start Docker
              sudo apt-get update -y
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo usermod -aG docker ubuntu

              # 2. Pull your custom Flask app from Docker Hub
              sudo docker pull niranjanhulamudde/flask-app:latest

              # 3. Run the container, mapping host port 5000 to container port 5000
              # --restart always ensures the app boots back up if the server reboots
              sudo docker run -d -p 5000:5000 --restart always --name flask-web-app niranjanhulamudde/flask-app:latest
              EOF

	tags = {
		Name = "flask-app-server"
}
}

