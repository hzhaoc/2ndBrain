## Ch7: More SQL

_More commands_

- Nested queries
- &quot;EXIST&quot;, &quot;UNIQUE&quot;
- &quot;JOIN… ON&quot;, &quot;NATURAL JOIN&quot;, &quot;LEFT OUTER JOIN… ON&quot;…
- Aggregate functions such as &quot;SUM&quot;, &quot;MAX&quot;
- &quot;HAVING&quot;, &quot;GROUP BY&quot;
- &quot;WITH&quot;, &quot;CASE&quot;
- Recursive queries
- Specifying Constraints as Assertions
- Specifying Constraints as Triggers
- Views
- A view is considered to be a virtual table.
  1. Implementation: Update, …
  2. Views as authorization mechanisms: views hide certain attributes or tuples form unauthorized users.

_Schema change statements in SQL_

- DROP
- ALTER
- …

**Module: SQL**

- _Insert_

- _Delete_

- _Update_

By default, &quot;FROM&quot; does cross product.

- _Sketchy SQL semantic notes_
	- Select Distinct(a) – **without Distinct, tables may have duplicates**
	- Where like &quot;a%&quot; -\&gt; match character a followed by any number of any characters
	- Where like &#39;A\_ \_ \_ \_ \_&#39; -\&gt; match character A with exactly 5 random characters
	- Union – return set
	- Union All – return all
	- Intersect (all) – similar to Union
	- Except (all) – set difference, similar to union
	- **Having** – condition on the **group**
	- Nested queries – in/not in, all
	- Nested correlated queries – think of it as a sub-query evaluated once for each row of the outer query