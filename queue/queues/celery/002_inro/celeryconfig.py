# broker_url = 'pyamqp://'  ## not set (deleted?)
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Warsaw'  ## changed

# To verify that your configuration file works properly and doesn’t contain any syntax errors, you can try to import it:
# $ python -m celeryconfig

#  route a misbehaving task to a dedicated queue:
task_routes = {
    'tasks.add': 'low-priority',
}

# Or instead of routing it you could rate limit the task instead, so that only 10 tasks of this type can be processed in a minute (10/m):
#
# task_annotations = {
#     'tasks.add': {'rate_limit': '10/m'}
# }