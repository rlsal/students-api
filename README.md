Run application.py to use API 

Student-API routes:

Get students - /students --GET

Add student -  /students --POST

Get student - /students/:email --GET

Update student - /student/:email --PATCH

Delete student - student/:email

Get courses - /courses --GET

Add course - /courses --POST

Get course - /courses/:name --GET

Update course - /courses/:name --PATCH

Delete course - /courses/:name --DELETE

Add student to course - /coursestudent/:course_id/:student_id --POST

Add grade - /grades/:student_id/:course_id/:grade --POST

Get student grade in course - /grades/:course_id/:student_id --GET

Remove student from course - /coursestudent/:course_id/:stunent_id --DELETE