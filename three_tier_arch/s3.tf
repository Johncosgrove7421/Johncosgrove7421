### S3

resource "aws_s3_bucket" "s3" {
  bucket = "executive-presentation-7421"

  tags = {
    Name        = "executive-presentation-7421"
    Environment = "Dev"
  }
}
