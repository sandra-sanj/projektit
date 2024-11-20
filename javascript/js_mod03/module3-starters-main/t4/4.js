'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const element = document.querySelector('#target');

for (const student of students) {
  console.log(student);
  const newElement = document.createElement('option');
  newElement.textContent = student.name;
  newElement.value = student.id;
  element.appendChild(newElement);
}
