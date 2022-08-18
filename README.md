Lambda-get-cloudwatch-metrics
===========================

This repository provides Lambda function for getting metrics value from CloudWatch.

Input Parameter
---------------
This Lambda function requires following json.

```json
{
    "query_data": {
        "NameSpace": NameSpace,
        "MetricName": MetricName,
        "Dimensions": Dimensions,
        "Period": Period,
        "Stat": Stat
    },
    "target": {
        "host": host,
        "key": key
    }
}
```

| First variable | Second variable | Description |
| -------------- | --------------- | ----------- |
| query_data     | NameSpace       | Specify NameSpace of CloudWatch metrics |
| query_data     | MetricName      | Specify MetricName of CloudWatch metrics |
| query_data     | Dimensions      | Specify Dimensions of CloudWatch metrics by list of metrics dimensions dictionary |
| query_data     | Period          | Specify Period for CloudWatch metrics |
| query_data     | Stat            | Specify Stat for CloudWatch metrics |
| target         | host            | Specify hostname for target in Zabbix |
| target         | key             | Specify key for target in Zabbix |

Example:
```json
{
  "query_data": {
    "Namespace": "AWS/ECS",
    "MetricName": "CPUUtilization",
    "Dimensions": [
      {
        "Name": "ClusterName",
        "Value": "Blog"
      },
      {
        "Name": "ServiceName",
        "Value": "Wordpress"
      }
    ],
    "Period": 300,
    "Stat": "Average"
  },
  "target": {
    "host": "ECS-Blog-Wordpress",
    "key": "ECS.CPUUtilization"
  }
}
```

Target Zabbix server host information is defined to [Lambda--send-value-to-zabbix](https://github.com/bynnchapu/Lambda-send-value-to-zabbix)