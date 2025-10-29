variable "project_id" {
  description = "ID del proyecto en Google Cloud"
  type        = string
}

variable "region" {
  description = "Región donde se desplegará el clúster"
  type        = string
  default     = "us-central1"
}

variable "cluster_name" {
  description = "Nombre del clúster de Kubernetes"
  type        = string
  default     = "devops-cluster"
}

variable "node_count" {
  description = "Cantidad de nodos en el clúster"
  type        = number
  default     = 2
}

variable "machine_type" {
  description = "Tipo de máquina para los nodos"
  type        = string
  default     = "e2-medium"
}
