const API="http://localhost:5000/students";

document.getElementById("studentForm")

.addEventListener("submit",addStudent);

loadStudents();

async function loadStudents(){

const response=await fetch(API);

const students=await response.json();

let rows="";

students.forEach(student=>{

rows+=`

<tr>

<td>${student.id}</td>

<td>${student.name}</td>

<td>${student.email}</td>

<td>${student.course}</td>

<td>

<button class="edit"

onclick="editStudent(${student.id},
'${student.name}',
'${student.email}',
'${student.course}')">

Edit

</button>

<button class="delete"

onclick="deleteStudent(${student.id})">

Delete

</button>

</td>

</tr>

`;

});

document.getElementById("studentTable").innerHTML=rows;

}

async function addStudent(e){

e.preventDefault();

const name=document.getElementById("name").value;

const email=document.getElementById("email").value;

const course=document.getElementById("course").value;

await fetch(API,{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

name,

email,

course

})

});

document.getElementById("studentForm").reset();

loadStudents();

}

async function deleteStudent(id){

await fetch(API+"/"+id,{

method:"DELETE"

});

loadStudents();

}

async function editStudent(id,name,email,course){

const newName=prompt("Student Name",name);

const newEmail=prompt("Email",email);

const newCourse=prompt("Course",course);

await fetch(API+"/"+id,{

method:"PUT",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

name:newName,

email:newEmail,

course:newCourse

})

});

loadStudents();

}

function searchStudent(){

const filter=document.getElementById("search")

.value.toUpperCase();

const rows=document

.getElementById("studentTable")

.getElementsByTagName("tr");

for(let i=0;i<rows.length;i++){

let td=rows[i].getElementsByTagName("td")[1];

if(td){

let txt=td.textContent;

rows[i].style.display=

txt.toUpperCase().indexOf(filter)>-1?

"": "none";

}

}

}