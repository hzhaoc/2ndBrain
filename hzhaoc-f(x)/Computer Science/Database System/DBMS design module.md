## **Module: IFD, EER, task decomp, constraint, data format**
__Forward__

_Software_ process includes:

1. Business process design
2. **Analysis**
3. **Specification**
4. **Design**
5. **Implementation**
6. Testing
7. Operation
8. Maintenance
 Step 2 – Step 5 are unique for database development. DATA FIRST! 
 ![[software_design_data_1st.png]]
 
 _DBMS design with examples_
 
 **Step 1: IFD** Example shown below 
 ![[ifd.png]]
 
**Step 2: ER/EER**
![[eer_diag.png]]

**Step 3: Specs: Data formats**

**Step 4: Specs: Constraints**
![[eer_const.png]]

**Step 5: Task decomposition** _
- Rules of thumb
	- Lock (schema construct) types
	- Lock numbers
	- Consistency
	- Mother task
	- Subtask
Example of decomposing task &quot;View Profile&quot;: 
![[eer_task_decpm.png]]

**Step 6: Abstract Code** Example of &quot;edit profile&quot; 
![[eer_task_edit_file_example.png]]

## **Module: schema create SQL, task SQL**
- _EER to relational table_
- _Relational table create statement_
- _Task, abstract code, SQL codes_

## **Module: Application Implementation**

- _**AMP Stack (PHP+Apache+MySQL)**_

## **Module: Physical file structure**
![[dbms_physical_file_structure.png]]