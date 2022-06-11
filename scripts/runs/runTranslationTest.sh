export BASE_URL=$1

echo "--------------------------------------------------"
echo "Url base: $BASE_URL"
echo "--------------------------------------------------"

pytest -s ../../test/integration/todoTranslationTest.py