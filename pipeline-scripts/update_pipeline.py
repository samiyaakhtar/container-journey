from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import sys

# Does a look up based on imageTag for the release pipeline to update its details
def update_pipeline(account_name, account_key, table_name, filter_name, filter_value, name1, value1, name2=None, value2=None):
    table_service = TableService(account_name=account_name, account_key=account_key)
    tasks = table_service.query_entities(table_name, filter=filter_name + " eq '"+ filter_value + "'")
    for task in tasks:
        print(task.RowKey)
        print(task.PartitionKey)

        print(task)
        task[name1] = value1
        if name2 != None and value2 != None:
            task[name2] = value2
        table_service.update_entity(table_name, task)
        print("Updated")
        break

    print("Done")

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) == 8:
        update_pipeline(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    elif len(sys.argv) == 10:
        update_pipeline(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])