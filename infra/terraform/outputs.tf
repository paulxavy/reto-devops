output "gke_cluster_name" {
  description = "Nombre del clúster creado"
  value       = google_container_cluster.primary.name
}

output "gke_endpoint" {
  description = "Endpoint del clúster"
  value       = google_container_cluster.primary.endpoint
}

output "region" {
  description = "Región del clúster"
  value       = var.region
}
