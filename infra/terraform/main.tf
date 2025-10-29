resource "google_container_cluster" "primary" {
  name     = var.cluster_name
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = "default"
  subnetwork = "default"

  resource_labels = {
    environment = "devops"
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "${var.cluster_name}-pool"
  location   = var.region
  cluster    = google_container_cluster.primary.name
  node_count = var.node_count

  node_config {
  machine_type = var.machine_type
  oauth_scopes = [
    "https://www.googleapis.com/auth/cloud-platform"
  ]
  disk_type    = "pd-standard"
  disk_size_gb = 30
  labels = {
    role = "general"
  }
}
}

output "cluster_name" {
  value = google_container_cluster.primary.name
}

output "endpoint" {
  value = google_container_cluster.primary.endpoint
}
