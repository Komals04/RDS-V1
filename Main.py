# main.py
from utils import get_rds_insights, export_to_csv

def handler(event, context):
    try:
        regions = ['us-east-1', 'us-east-2']  # Hardcoded regions
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'/tmp/rds_insights_combined_{timestamp}.csv'  # Use /tmp/ for Lambda

        fieldnames = [
            'DBIdentifier', 'Status', 'Role', 'Engine', 'Region', 'Size', 'CPU', 'vCPU',
            'ProvisionedIOPS', 'StorageType', 'Multi-AZ', 'GlobalCluster',
            'InstanceType', 'PerformanceInsightsEnabled', 'PerformanceInsightsKMSKeyId',
            'PerformanceInsightsRetentionPeriod', 'ServerlessV2ScalingConfiguration',
            'AvailabilityZone', 'PreferredMaintenanceWindow', 'BackupRetentionPeriod',
            'MultiAZ', 'PubliclyAccessible', 'VpcSecurityGroups', 'DBSubnetGroupName',
            'ReadReplicaDBClusterIdentifiers', 'ProcessorFeatures', 'CoreCount',
            'DBClusterIdentifier', 'ClusterStatus', 'ClusterEngine', 'ClusterRegion',
        ]

        with open(filename, 'w', newline='') as csvfile:
            export_to_csv(csvfile, fieldnames, regions)

        print(f'Completed checking and exporting RDS insights to {filename} for both regions.')
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e  # Propagate the exception to Lambda

if __name__ == "__main__":
    handler(None, None)  # For local testing, can be removed for deployment
