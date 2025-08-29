export default function updateStudentGradeByCity(students, city, newGrades) {
    const filter = students.filter(student => student.location == city);
    return filter.map(student => {
        let gradeResult = "N/A";
        for (const grade of newGrades) {
            if (grade.studentId == student.id) {
                gradeResult = grade.grade;
                break;
            }
        }
        return {
            id: student.id,
            firstName: student.firstName,
            location: student.location,
            grade: gradeResult
        };
    });
}