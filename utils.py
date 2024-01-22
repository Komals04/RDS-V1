# utils.py
import boto3
import csv
from datetime import datetime
from botocore.exceptions import ClientError

def extract_core_count(processor_features):
    # ... (unchanged)

def get_instance_configuration(rds_client, db_instance):
    # ... (unchanged)

def get_role_information(rds_client, db_instance):
    # ... (unchanged)

def get_rds_insights(rds_client, db_instance):
    # ... (unchanged)

def get_db_cluster_info(rds_client, db_cluster_identifier):
    # ... (unchanged)

def export_to_csv(csvfile, fieldnames, regions):
    for region in regions:
        rds_client = boto3.client('rds', region_name=region)

        response_instances = rds_client.describe_db_instances()
        instances = response_instances['DBInstances']

        response_clusters = rds_client.describe_db_clusters()
        clusters = response_clusters['DBClusters']

        for instance in instances:
            insights = get_rds_insights(rds_client, instance['DBInstanceIdentifier'])
            if insights:
                csvfile.writerow(insights)

        for cluster in clusters:
            cluster_info = get_db_cluster_info(rds_client, cluster['DBClusterIdentifier'])
            if cluster_info:
                csvfile.writerow(cluster_info)
