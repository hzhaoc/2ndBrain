## **Ch11: SQL Programming (PHP)**

- _PHP is one technique for programming dynamic features into Web pages._
- _A PHP interpreter provides a Hypertext Preprocessor that execute PHP commands in a text file and create desired HTML file._
- _PHP are executed on the Web server computer, in contrast to some others like JavaScript that is executed on client computer._

_A simple PHP example walkthrough_
```
//Program Segment P1:
0) \&lt;?php // start tag
1) // Printing a welcome message if the user submitted their name
// through the HTML form
2) if ( **$\_POST** [&#39;user\_name&#39;]) {
3) print(&quot;Welcome, &quot;) ;
4) print($\_POST[&#39;user\_name&#39;]);
// associative array
5) }
6) else {
7) // Printing the form to enter the user
// name since no name has
// been entered yet
8) print **\&lt;\&lt;\&lt;\_HTML\_**
9) \&lt;FORM method=&quot;post&quot;
action=&quot;$\_SERVER[&#39;PHP\_SELF&#39;]&quot;\&gt;
10) Enter your name: \&lt;input type=&quot;text&quot;
name=&quot;user\_name&quot;\&gt;
11) \&lt;BR/\&gt;
12) \&lt;INPUT type=&quot;submit&quot; value=&quot;SUBMIT
NAME&quot;\&gt;
13) \&lt;/FORM\&gt;
14) \_ **HTML\_;**
15) }
16) ?\&gt;
```

_PHP Basic Features_

- _Double-quoted strings: interpreter identifies variable names within double-quoted strings by $._
- _Numeric array, associative array (key-value pair)_
- _PHP functions_

```
//example to explain PHP function
0) function display\_welcome() {
1) print(&quot;Welcome, &quot;) ;
2) print($\_POST[&#39;user\_name&#39;]);
3) }
4)
5) function display\_empty\_form(); {
6) print \&lt;\&lt;\&lt;\_HTML\_
7) \&lt;FORM method=&quot;post&quot;
action=&quot;$\_SERVER[&#39;PHP\_SELF&#39;]&quot;\&gt;
8) Enter your name: \&lt;INPUT
type=&quot;text&quot; name=&quot;user\_name&quot;\&gt;
9) \&lt;BR/\&gt;
10) \&lt;INPUT type=&quot;submit&quot;
value=&quot;Submit name&quot;\&gt;
11) \&lt;/FORM\&gt;
12) \_HTML\_;
13) }
14) if ($\_POST[&#39;user\_name&#39;]) {
15) display\_welcome();
16) }
17) else {
18) display\_empty\_form();
19) }
```

- _PHP server Variables and Forms_

_PHP accessing database using PEAR DB_

_ **1. Connect to database** _
```
0) require &#39;DB.php&#39;;
1) $d = DB::connect(&#39;oci8://acct1:pass12@www.host.com/d
b1&#39;);
2) if (DB::isError($d)) { die(&quot;cannot connect –
&quot; . $d-\&gt;getMessage());}
...
3) $q = $d-\&gt;query(&quot;CREATE TABLE EMPLOYEE
4) (Emp\_id INT,
5) Name VARCHAR(15),
6) Job VARCHAR(10),
7) Dno INT);&quot; );
8) if (DB::isError($q)) { die(&quot;table creation
not successful − &quot; .
$q-\&gt;getMessage()); }
...

9) $d-\&gt;setErrorHandling(PEAR\_ERROR\_DIE);
...
```

_ **2. Collect data from Forms and Insert records** _
```
10) $eid = $d-\&gt;nextID(&#39;EMPLOYEE&#39;);
11) $q = $d-\&gt;query(&quot;INSERT INTO EMPLOYEE VALUES
12) ($eid, $\_POST[&#39;emp\_name&#39;],
$\_POST[&#39;emp\_job&#39;], $\_POST[&#39;emp\_dno&#39;])&quot; );
...
13) $eid = $d-\&gt;nextID(&#39;EMPLOYEE&#39;);
14) $q = $d-\&gt;query(&#39;INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?)&#39;,
15) array($eid, $\_POST[&#39;emp\_name&#39;],
$\_POST[&#39;emp\_job&#39;], $\_POST[&#39;emp\_dno&#39;]) );
```