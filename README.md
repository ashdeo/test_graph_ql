# test_graph_ql
Airstack Test

to run the code use following command 

pytest

run specific test case 
pytest tests/test_graphql_api.py::test_api_response

alluredir 
pytest --alluredir=<report_directory>
pytest --alluredir=allure_report


allure serve <report_directory>

html report 
pytest --html=<report_file_name>.html
pytest --html=html_report/report.html

xdg-open report.html  # On Linux (use "open" on macOS)
xdg-open html_report/report.html
