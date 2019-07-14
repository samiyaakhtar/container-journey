from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import sys

# Does a look up based on hldCommitId for the build pipeline to update its details
def update_manifest_pipeline(account_name, account_key, table_name, hld_commit_id, name1, value1, name2=None, value2=None):
    table_service = TableService(account_name=account_name, account_key=account_key)
    tasks = table_service.query_entities(table_name, filter="hldCommitId eq '"+ hld_commit_id + "'")
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
    if len(sys.argv) == 7:
        update_manifest_pipeline(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif len(sys.argv) == 9:
        update_manifest_pipeline(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])