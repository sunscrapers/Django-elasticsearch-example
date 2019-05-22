from elasticsearch_dsl.connections import connections


def wait_elasticsearch_availability():
    good_statuses = ['green', 'yellow']
    while True:
        try:
            respone = connections.get_connection().cluster.health()
            if respone.get('status') in good_statuses:
                return
        except Exception:
            pass
