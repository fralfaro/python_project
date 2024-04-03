from diagrams import Diagram, Cluster
from diagrams.azure.analytics import Databricks
from diagrams.azure.compute import KubernetesServices
from diagrams.azure.database import SQLDatabases, DataFactory
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.security import KeyVaults
from diagrams.azure.storage import BlobStorage


if __name__ == '__main__':
    with Diagram("Azure Data Science Workflow", show=False) as diagram:
        with Cluster("Data Collection & Preprocessing"):
            data_factory = DataFactory("Data Factory")
            databricks = Databricks("Databricks")
            blob_storage = BlobStorage("Blob Storage")

            data_factory >> databricks >> blob_storage

        with Cluster("Model Development"):
            azure_machine_learning = MachineLearningServiceWorkspaces("Azure ML")
            kubernetes_services = KubernetesServices("AKS")

            azure_machine_learning >> kubernetes_services

        with Cluster("Model Evaluation"):
            application_insights = ApplicationInsights("App Insights")
            sql_databases = SQLDatabases("SQL Databases")

            azure_machine_learning >> application_insights
            azure_machine_learning >> sql_databases

        with Cluster("Deployment & Monitoring"):
            virtual_networks = VirtualNetworks("Virtual Networks")
            key_vaults = KeyVaults("Key Vaults")

            kubernetes_services >> virtual_networks
            kubernetes_services >> key_vaults