import json
import datetime
import boto3

MISSING_DATA_MESSAGE = 'metric is missing'

def get_cloudwatch_metric(query_data):
    client = boto3.client('cloudwatch')
    response = client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': query_data['Namespace'],
                        'MetricName': query_data['MetricName'],
                        'Dimensions': query_data['Dimensions']
                    },
                    'Period': query_data['Period'],
                    'Stat': query_data['Stat']
                }
            }
        ],
        StartTime=datetime.datetime.now() - datetime.timedelta(minutes=5),
        EndTime=datetime.datetime.now()
    )

    if len(response['MetricDataResults'][0]['Values']) != 0:
        return response['MetricDataResults'][0]['Values'][0]
    else:
        return MISSING_DATA_MESSAGE


def lambda_handler(event, context):
    metric_value = get_cloudwatch_metric(event['query_data'])
    status_code = 200 if metric_value is not MISSING_DATA_MESSAGE else 500
    return_data = {
        'status_code': status_code,
        'value': metric_value
    }

    return json.dumps(return_data)