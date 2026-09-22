output "instance_public_ip" {
	value = aws_instance.flask-service.public_ip
	description = "instance public ip"
}
output "instance_arn" {
	value = aws_instance.flask-service.arn
	description = "instance arn"
}
