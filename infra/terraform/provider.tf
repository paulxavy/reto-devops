terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.5.0"
}

provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project_id
  region      = var.region
}

variable "credentials_file" {
  description = "Ruta al archivo JSON de la cuenta de servicio de Google Cloud"
  type        = string
  default     = "./credentials.json"
}
