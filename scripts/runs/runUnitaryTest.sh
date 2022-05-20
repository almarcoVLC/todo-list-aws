export PYTHONPATH="$PYTHONPATH:/home/ubuntu/environment/todo-list-aws"
export DYNAMODB_TABLE=todoUnitTestsTable

echo "---------------------"
echo "$PYTHONPATH"
echo "$DYNAMODB_TABLE"
echo "---------------------"

python3.7 ../../test/unit/TestToDo.py