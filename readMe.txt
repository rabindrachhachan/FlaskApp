Requirement:
1.python2.7
2.MySQL5.7
3.flask
4.Rest API


Steps:
1.create databse employees, employees table,insert some value into table
2.configure MYSQL configuration in Python source file
3.Implement REST API for HTTP methods
4.Handle REST API Request,Response


App Route: run these url to perform the operation.

http://localhost:5000/GetAllRecord

http://localhost:5000/GetRecord?id=4

http://localhost:5000/AddRecord?id=10&expense_date=20120220&expense_category=travel&type=credit&amount=1300

http://localhost:5000/UpdateRecord?id=6&amount=1400

http://localhost:5000/DeleteRecord?id=9

