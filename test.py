import boto.ec2
import os

#access_key_id = 'AKIAIVPVTS6RC5RS4DJQ'
#secret_access_key = '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'

#Making connection by using key

conn = boto.ec2.connect_to_region('us-west-2',
                                  aws_access_key_id='AKIAIVPVTS6RC5RS4DJQ',
                                  aws_secret_access_key='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')
print conn

createInstance = conn.run_instances('ami-f0091d91',
                                    key_name = 'xyz',
                                    instance_type = 't2.micro',
                                    security_groups=['launch-wizard-5'])

print createInstance