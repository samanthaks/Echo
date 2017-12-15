function changeAssignedStudent(name) {
	let assignedTo = document.querySelector("body > div > div:nth-child(5) > div:nth-child(3) > table > tbody > tr > td:nth-child(4)")
	assignedTo.innerHTML = "Student Assigned: " + name
}
